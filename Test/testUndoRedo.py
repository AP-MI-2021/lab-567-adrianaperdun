from Domain.rezervare import get_id, get_clasa, get_pret
from Logic.crud import add, get_by_id
from Logic.functions import Upgrade, reduce


def testUndoRedo():
    lista = []
    undoList = []
    redoList = []
    rezultat = add("1", "Marius", "economy", 350, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = add("2", "Ionut", "business", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = add("3", "Ionut", "business", 550, "da", lista)
    undoList.append(lista)
    lista = rezultat

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert get_id(lista[1]) == "2"
    assert get_id(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
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

    rezultat = add("1", "Marius", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    rezultat = add("2", "Ionut", "business", 120, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = add("3", "Crina", "economy plus", 125, "nu", lista)
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
    assert get_id(lista[1]) == "2"
    assert get_id(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
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
    assert get_id(lista[1]) == "2"
    assert get_id(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert undoList == [[]]

    rezultat = add("4", "Bianca", "economy plus", 250, "da", lista)
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

    rezultat = add("1", "Marius", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = add("2", "Ionut", "business", 320, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = add("3", "Crina", "economy plus", 225, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = Upgrade("Martinescu", lista)
    undoList.append(lista)
    lista = rezultat
    assert get_clasa(get_by_id("1", lista)) == "economy plus"

    redoList.append(lista)
    lista = undoList.pop()
    assert get_clasa(get_by_id("1", lista)) == "economy"

    undoList.append(lista)
    lista = redoList.pop()
    assert get_clasa(get_by_id("1", lista)) == "economy plus"


def testUndoRedoIeftinire():
    lista = []
    undoList = []
    redoList = []

    rezultat = add("1", "Marius", "economy", 100, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = add("2", "Ionut", "business", 120, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = reduce(10, lista)
    undoList.append(lista)
    lista = rezultat
    assert get_pret(get_by_id("1", lista)) == 90
    assert get_pret(get_by_id("2", lista)) == 120

    redoList.append(lista)
    lista = undoList.pop()
    assert get_pret(get_by_id("1", lista)) == 100
    assert get_pret(get_by_id("2", lista)) == 120

    undoList.append(lista)
    lista = redoList.pop()
    assert get_pret(get_by_id("1", lista)) == 90
    assert get_pret(get_by_id("2", lista)) == 120