from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin, creeazaRezervare
from Logic.Ieftinire import IeftinirePret
from Logic.cerinte import pretMaxim, ordo, do_undo, do_redo
from Logic.clasaSuperioara import UpgradeClasa
from Logic.crud import adaugaRezervare, getById, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    """
    testeaza daca aduga o rezervare
    """
    undolist = []
    redolist = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [], undolist, redolist)
    assert getId(getById("1", lista)) == '1'
    assert getNume(getById("1", lista)) == "Prigoana"
    assert getClasa(getById("1", lista)) == 'economy'
    assert getPret(getById("1", lista)) == 200
    assert getCheckin(getById("1", lista)) == "Da"


def testStergeRezervare():
    """
    testeaza daca sterge o rezervare
    """
    undolist = []
    redolist = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [], undolist, redolist)
    lista = adaugaRezervare('2', 'Claudiu', 'economy', 200, 'Nu', lista, undolist, redolist)
    lista = stergeRezervare('1', lista, undolist, redolist)
    assert len(lista) == 1
    assert getById('1', lista) is None
    lista = stergeRezervare('3', lista, undolist, redolist)
    assert len(lista) == 1
    assert getById('2', lista) is not None


def testgetById():
    """
    testeaza daca gaseste o anumita rezervare
    """
    undolist = []
    redolist = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [], undolist, redolist)
    assert getById('1', lista) is not None


def testModificare():
    """
    testeaza daca modifica corect o rezervare
    """
    undolist = []
    redoList = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [], undolist, redoList)
    lista = modificaRezervare('1', 'Prigoana', 'economy plus', 250, 'Nu', lista, undolist, redoList)
    assert getId(getById("1", lista)) == '1'
    assert getNume(getById("1", lista)) == "Prigoana"
    assert getClasa(getById("1", lista)) == 'economy plus'
    assert getPret(getById("1", lista)) == 250
    assert getCheckin(getById("1", lista)) == "Nu"


def testclasasuperioara():
    """
    testeaza daca upgradeaza corect o clasa
    """
    undoList = []
    redoList = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [], undoList, redoList)
    rezervare1 = creeazaRezervare('1', 'Prigoana', 'economy plus', 200, 'Da')
    lista = UpgradeClasa(lista, 'Prigoana', undoList, redoList)
    assert rezervare1 in lista


def testIeftinereProcent():
    """
    testeaza daca ieftineste corect cu un procent
    """
    undoList = []
    redoList = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [], undoList, redoList)
    rezervare1 = creeazaRezervare('1', 'Prigoana', 'economy', 180, 'Da')
    lista = IeftinirePret(lista, 10, undoList, redoList)
    assert rezervare1 in lista


def testPretMaxim():
    """
    testeaza daca gaseste corect preturile maxime al fiecarei clase
    """
    undoList = []
    redoList = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [], undoList, redoList)
    lista = adaugaRezervare('2', 'Claudiu', 'business', 250, 'Nu', lista, undoList, redoList)
    lista = adaugaRezervare('3', 'Claudiu', 'economy', 100, 'Da', lista, undoList, redoList)
    lista = adaugaRezervare('4', 'Alex', 'economy plus', 50, 'Da', lista, undoList, redoList)
    lista = adaugaRezervare('5', 'Pop', 'economy', 220, 'Da', lista, undoList, redoList)
    assert pretMaxim(lista) == {'economy': 220, 'business': 250, 'economy plus': 50}


def testOrdo():
    """
    testeaza daca se ordoneaza corect descrescator rezervarile, in functie de pretul lor
    """
    undoList = []
    redoList = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [], undoList, redoList)
    lista = adaugaRezervare('2', 'Claudiu', 'business', 250, 'Nu', lista, undoList, redoList)
    lista = adaugaRezervare('3', 'Claudiu', 'economy', 100, 'Da', lista, undoList, redoList)
    lista = adaugaRezervare('4', 'Alex', 'economy plus', 50, 'Da', lista, undoList, redoList)
    lista = adaugaRezervare('5', 'Pop', 'economy', 220, 'Da', lista, undoList, redoList)
    assert ordo(lista, undoList, redoList) == [
        [('id', '2'), ('nume', 'Claudiu'), ('clasa', 'business'), ('pret', 250), ('checkin', 'Nu')],
        [('id', '5'), ('nume', 'Pop'), ('clasa', 'economy'), ('pret', 220), ('checkin', 'Da')],
        [('id', '1'), ('nume', 'Prigoana'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'Da')],
        [('id', '3'), ('nume', 'Claudiu'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')],
        [('id', '4'), ('nume', 'Alex'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'Da')]]


def testUndoRedo():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', lista, undoList, redoList)
    assert lista == [[('id', '1'), ('nume', 'Prigoana'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'Da')]]

    lista = adaugaRezervare('2', 'Claudiu', 'business', 250, 'Nu', lista, undoList, redoList)
    assert lista == [[('id', '1'), ('nume', 'Prigoana'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'Da')],
                     [('id', '2'), ('nume', 'Claudiu'), ('clasa', 'business'), ('pret', 250), ('checkin', 'Nu')]]

    lista = adaugaRezervare('3', 'Claudiu', 'economy', 100, 'Da', lista, undoList, redoList)
    assert lista == [[('id', '1'), ('nume', 'Prigoana'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'Da')],
                     [('id', '2'), ('nume', 'Claudiu'), ('clasa', 'business'), ('pret', 250), ('checkin', 'Nu')],
                     [('id', '3'), ('nume', 'Claudiu'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    lista = ordo(lista, undoList, redoList)
    assert lista == [[('id', '2'), ('nume', 'Claudiu'), ('clasa', 'business'), ('pret', 250), ('checkin', 'Nu')],
                     [('id', '1'), ('nume', 'Prigoana'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'Da')],
                     [('id', '3'), ('nume', 'Claudiu'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    lista = do_undo(lista, undoList, redoList)
    assert lista == [[('id', '1'), ('nume', 'Prigoana'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'Da')],
                     [('id', '2'), ('nume', 'Claudiu'), ('clasa', 'business'), ('pret', 250), ('checkin', 'Nu')],
                     [('id', '3'), ('nume', 'Claudiu'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    lista = do_undo(lista, undoList, redoList)
    assert lista == [[('id', '1'), ('nume', 'Prigoana'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'Da')],
                     [('id', '2'), ('nume', 'Claudiu'), ('clasa', 'business'), ('pret', 250), ('checkin', 'Nu')]]

    lista = do_undo(lista, undoList, redoList)
    assert lista == [[('id', '1'), ('nume', 'Prigoana'), ('clasa', 'economy'), ('pret', 200), ('checkin', 'Da')]]

    lista = do_undo(lista, undoList, redoList)
    assert lista == []

    lista = adaugaRezervare('4', 'Alex', 'economy plus', 50, 'Da', lista, undoList, redoList)
    assert lista == [[('id', '4'), ('nume', 'Alex'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'Da')]]

    lista = adaugaRezervare('2', 'Claudiu', 'business', 250, 'Nu', lista, undoList, redoList)
    assert lista == [[('id', '4'), ('nume', 'Alex'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'Da')],
                     [('id', '2'), ('nume', 'Claudiu'), ('clasa', 'business'), ('pret', 250), ('checkin', 'Nu')]]

    lista = do_redo(lista, undoList, redoList)
    assert lista == [[('id', '4'), ('nume', 'Alex'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'Da')],
                     [('id', '2'), ('nume', 'Claudiu'), ('clasa', 'business'), ('pret', 250), ('checkin', 'Nu')]]

    lista = do_undo(lista, undoList, redoList)
    assert lista == [[('id', '4'), ('nume', 'Alex'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'Da')]]

    lista = do_undo(lista, undoList, redoList)
    assert lista == []

    lista = do_redo(lista, undoList, redoList)
    assert lista == []

    lista = do_redo(lista, undoList, redoList)
    assert lista == [[('id', '4'), ('nume', 'Alex'), ('clasa', 'economy plus'), ('pret', 50), ('checkin', 'Da')]]
