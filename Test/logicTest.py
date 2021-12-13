from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.crud import adaugaRezervare, getById, stergereRezervare, modificaRezervare
from Logic.functions import trecereaClasaSuperioaraDupaNume, getByName, ieftinirePretRezervariDupaCheckin, getByCheckin, \
    ordoneazaRezervarileDescrescDupaPret, sumaPreturiPerNume


def testAdaugareRezervare():
    lista = []
    lista = adaugaRezervare("2", "Ana", "business", 300, "Nu", lista)
    assert len(lista) == 1
    assert getId(getById("2", lista)) == "2"
    assert getNume(getById("2", lista)) == "Ana"
    assert getClasa(getById("2", lista)) == "business"
    assert getPret(getById("2", lista)) == 300
    assert getCheckin(getById("2", lista)) == "Nu"



def testStergereRezervare():
    lista = []
    lista = adaugaRezervare("1", "Ana", "business", 300, "Nu", [])
    lista = adaugaRezervare("2", "Teo", "business", 360, "Nu", lista)

    lista= stergereRezervare("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None

    try:
        lista = stergereRezervare("3", lista)
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False



def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Ana", "business", 1400, "Da", lista)
    lista = adaugaRezervare("2", "Teo", "business", 800, "Nu", lista)
    lista = modificaRezervare("1", "Ana", "business", 1400, "Da", lista)

    rezervareUpdatata = getById("1", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ana"
    assert getClasa(rezervareUpdatata) == "business"
    assert getPret(rezervareUpdatata) == 1400
    assert getCheckin(rezervareUpdatata) == "Da"

    rezervareNeupdatata = getById("2", lista)
    assert getId(rezervareNeupdatata) == "2"
    assert getNume(rezervareNeupdatata) == "Teo"
    assert getClasa(rezervareNeupdatata) == "business"
    assert getPret(rezervareNeupdatata) == 800
    assert getCheckin(rezervareNeupdatata) == "Nu"


def testTrecereaClasaSuperioaraDupaNume():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 1400, "da", [])
    lista = adaugaRezervare("2", "Teo", "business", 360, "nu", lista)

    lista = trecereaClasaSuperioaraDupaNume("Ana", lista)
    rezervareUpdatata = getByName("Ana", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ana"
    assert getClasa(rezervareUpdatata) == "economy plus"
    assert getPret(rezervareUpdatata) == 1400
    assert getCheckin(rezervareUpdatata) == "da"


def testIeftinirePretRezervariDupaCheckin():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 1400, "da", [])
    lista = adaugaRezervare("2", "Teo", "business", 360, "nu", lista)

    lista = ieftinirePretRezervariDupaCheckin(42, lista)
    rezervareUpdatata = getByCheckin(lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ana"
    assert getClasa(rezervareUpdatata) == "economy"
    assert getPret(rezervareUpdatata) == 812
    assert getCheckin(rezervareUpdatata) == "da"


def testOrdoneazaRezervarileDescrescDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 140, "da", lista)
    lista = adaugaRezervare("2", "Teo", "business", 360, "nu", lista)
    lista = adaugaRezervare("3", "Ana", "economy", 1400, "da", lista)
    lista = adaugaRezervare("4", "Teo", "business", 90, "nu", lista)
    rezultat = ordoneazaRezervarileDescrescDupaPret(lista)
    assert getId(rezultat[0]) == "3"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "1"
    assert getId(rezultat[3]) == "4"


def testSumaPreturiPerNume():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 140, "da", lista)
    lista = adaugaRezervare("2", "Teo", "business", 360, "nu", lista)
    lista = adaugaRezervare("3", "Ana", "economy", 1400, "da", lista)
    rezultat = sumaPreturiPerNume(lista)
    assert len(rezultat) == 2
    assert rezultat["Ana"] == 1540
    assert rezultat["Mara"] == 360