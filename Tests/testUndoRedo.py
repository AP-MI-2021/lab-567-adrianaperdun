from Domain.rezervare import getId, getClasa, getPret
from Logic.crud import adaugaRezervare, getById
from Logic.cerinte import trecereaClasaSuperioaraDupaNume, ieftinirePretRezervariDupaCheckin


def testUndoRedo():
    lista = []
    undoList = []
    redoList = []
    rezultat = adaugaRezervare("1", "Marius", "economy", 350, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("2", "Ionut", "business", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("3", "Ionut", "business", 550, "da", lista)
    undoList.append(lista)
    lista = rezultat

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == []

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList
    assert len(lista) == 0
    assert undoList == []

    rezultat = adaugaRezervare("1", "Marius", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    rezultat = adaugaRezervare("2", "Ionut", "business", 120, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("3", "Crina", "economy plus", 125, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert len(lista) == 2

    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    rezultat = adaugaRezervare("4", "Bianca", "economy plus", 250, "da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 1

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert len(undoList) == 0
    assert len(redoList) == 2

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0
    assert len(undoList) == 2


def testUndoRedoTrecereClasaSuperioara():
    lista = []
    undoList = []
    redoList = []

    rezultat = adaugaRezervare("1", "Marius", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("2", "Ionut", "business", 320, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("3", "Crina", "economy plus", 225, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = trecereaClasaSuperioaraDupaNume("Martinescu", lista)
    undoList.append(lista)
    lista = rezultat
    assert getClasa(getById("1", lista)) == "economy plus"

    redoList.append(lista)
    lista = undoList.pop()
    assert getClasa(getById("1", lista)) == "economy"

    undoList.append(lista)
    lista = redoList.pop()
    assert getClasa(getById("1", lista)) == "economy plus"


def testUndoRedoIeftinire():
    lista = []
    undoList = []
    redoList = []

    rezultat = adaugaRezervare("1", "Marius", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("2", "Ionut", "business", 120, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = ieftinirePretRezervariDupaCheckin(10, lista)
    undoList.append(lista)
    lista = rezultat
    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 120

    redoList.append(lista)
    lista = undoList.pop()
    assert getPret(getById("1", lista)) == 100
    assert getPret(getById("2", lista)) == 120

    undoList.append(lista)
    lista = redoList.pop()
    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 120