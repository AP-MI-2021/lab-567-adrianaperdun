from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin, create
from Logic.crud import add, get_by_id, delete, modify
from Logic.functions import Upgrade, reduce, max_price, ordo, undo, redo, get_by_name, get_by_checkin, suma


def testadd():
    '''
    testeaza daca aduga o rezervare
    '''
    lista = add('1', 'Adriana', 'economy', 200, 'Da', [])
    assert get_id(get_by_id("1", lista)) == '1'
    assert get_nume(get_by_id("1", lista)) == "Adriana"
    assert get_clasa(get_by_id("1", lista)) == 'economy'
    assert get_pret(get_by_id("1", lista)) == 200
    assert get_checkin(get_by_id("1", lista)) == "Da"


def testdelete():
    '''
    testeaza daca sterge o rezervare
    '''
    undoList = []
    redoList = []
    lista = add('1', 'Adriana', 'economy', 200, 'Da', [])
    lista = add('2', 'Andreea', 'economy', 200, 'Nu', lista)
    lista = delete('1', lista)
    assert len(lista) == 1
    assert get_by_id('1',lista) is None
    lista = delete('3', lista)
    assert len(lista) == 1
    assert get_by_id('2', lista) is not None


def testgetById():
    '''
    testeaza daca gaseste o anumita rezervare
    '''

    lista= add('1', 'Adriana', 'economy', 200, 'Da', [])
    assert get_by_id('1',lista) is not None


def testmodify():
    '''
    testeaza daca modifica corect o rezervare
    '''

    lista = add('1', 'Adriana', 'economy', 200, 'Da', [])
    lista= modify('1', 'Adriana', 'economy plus', 250, 'Nu', lista)
    assert get_id(get_by_id("1", lista)) == '1'
    assert get_nume(get_by_id("1", lista)) == "Adriana"
    assert get_clasa(get_by_id("1", lista)) == 'economy plus'
    assert get_pret(get_by_id("1", lista)) == 250
    assert get_checkin(get_by_id("1", lista)) == "Nu"


def testupgrade():
    '''
    testeaza daca upgradeaza corect o clasa
    '''
    lista = []
    lista = add("1", "Adriana", "economy", 1400, "da", lista)
    lista = add("2", "Ariana", "business", 360, "nu", lista)

    lista = Upgrade("Adriana", lista)
    rezervareUpdatata = get_by_name("Adriana", lista)
    assert get_id(rezervareUpdatata) == "1"
    assert get_nume(rezervareUpdatata) == "Ariana"
    assert get_clasa(rezervareUpdatata) == "economy plus"
    assert get_pret(rezervareUpdatata) == 1400
    assert get_checkin(rezervareUpdatata) == "da"


def testreduce():
    '''
    testeaza daca ieftineste corect cu un procent
    '''
    lista = []
    lista = add("1", "Adriana", "economy", 1400, "da", lista)
    lista = add("2", "Ariana", "business", 360, "nu", lista)

    lista = reduce(42, lista)
    rezervareUpdatata = get_by_checkin(lista)
    assert get_id(rezervareUpdatata) == "1"
    assert get_nume(rezervareUpdatata) == "Adriana"
    assert get_clasa(rezervareUpdatata) == "economy"
    assert get_pret(rezervareUpdatata) == 812
    assert get_checkin(rezervareUpdatata) == "da"


def testmax():
    '''
    testeaza daca gaseste corect preturile maxime al fiecarei clase
    '''
    lista = []
    lista = add("1", "Adriana", "economy", 140, "da", lista)
    lista = add("2", "Ariana", "business", 360, "nu", lista)
    lista = add("3", "Adriana", "economy", 1400, "da", lista)
    rezultat = suma(lista)
    assert len(rezultat) == 2
    assert rezultat["Adriana"] == 1540
    assert rezultat["Ariana"] == 360


def testOrdo():
    '''
    testeaza daca se ordoneaza corect descrescator rezervarile, in functie de pretul lor
    '''
    lista = []
    lista = add("1", "Adriana", "economy", 140, "da", lista)
    lista = add("2", "Ariana", "business", 360, "nu", lista)
    lista = add("3", "Adriana", "economy", 1400, "da", lista)
    lista = add("4", "Ariana", "business", 90, "nu", lista)
    rezultat = ordo(lista)
    assert get_id(rezultat[0]) == "3"
    assert get_id(rezultat[1]) == "2"
    assert get_id(rezultat[2]) == "1"
    assert get_id(rezultat[3]) == "4"


