from Domain.obiect import get_location, creare_obiect, get_description, get_id
from Logic.crud import add_object
from Logic.functions import move_object, concat_str, max_price, ascending_order


def test_move_object():
    lista = []
    lista = add_object(1, "obiect 1", "descriere 1", 4000.0, "parter", lista)
    lista = add_object(2, "obiect 2", "descriere 2", 10.0, "arhiva", lista)
    lista = add_object(3, "obiect 3", "descriere 3", 35.2, "sala mese", lista)
    lista = add_object(4, "obiect 4", "descriere 4", 2000.0, "birou", lista)
    lista = move_object("parter", "arhiva", lista)
    assert get_location(lista[0]) == "arhiva"
    assert get_location(lista[3]) == "arhiva"


def test_concat_str():
    obiect = creare_obiect(2, "Monitor Dell", "23.5'', HD, 148Hz", 1099.0, "sala conferinte")
    str = " string de test"
    obiect = concat_str(obiect, str)
    assert get_description(obiect) == "23.5'', HD, 148Hz string de test"


def test_max_price():
    lista = []
    lista = add_object(1, "obiect 1", "descriere 1", 4000.0, "parter", lista)
    lista = add_object(2, "obiect 2", "descriere 2", 10.0, "arhiva", lista)
    lista = add_object(3, "obiect 3", "descriere 3", 35.2, "sala mese", lista)
    lista = add_object(4, "obiect 4", "descriere 4", 2000.0, "birou", lista)
    rezultat = max_price(lista)
    assert rezultat["LOC1"] == 4000.0
    assert rezultat["LOC2"] == 3000.0


def test_ascending_order():
    lista = []
    lista = add_object(1, "obiect 1", "descriere 1", 4000.0, "parter", lista)
    lista = add_object(2, "obiect 2", "descriere 2", 10.0, "arhiva", lista)
    lista = add_object(3, "obiect 3", "descriere 3", 35.2, "sala mese", lista)
    lista = add_object(4, "obiect 4", "descriere 4", 2000.0, "birou", lista)
    lista = ascending_order(lista)
    assert get_id(lista[0]) == 3
    assert get_id(lista[1]) == 4
    assert get_id(lista[2]) == 1
    assert get_id(lista[3]) == 2


def test_sum():
    lista = []
    lista = add_object(1, "obiect 1", "descriere 1", 4000.0, "parter", lista)
    lista = add_object(2, "obiect 2", "descriere 2", 10.0, "arhiva", lista)
    lista = add_object(3, "obiect 3", "descriere 3", 35.2, "sala mese", lista)
    lista = add_object(4, "obiect 4", "descriere 4", 2000.0, "birou", lista)
    rezultat = sum(lista)
    assert rezultat["parter"] == 60.0
    assert rezultat["arhiva"] == 4000.0