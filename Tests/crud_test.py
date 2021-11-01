from Domain.obiect import get_id, get_name, get_description, get_pret, get_location
from Logic.crud import add_object, get_by_id, delete_object, modify_object


def test_add_object():
    lista = []
    lista = add_object("1", "masca", "protectie", 1, "Cora", lista)
    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_name(get_by_id("1", lista)) == "masca"
    assert get_description(get_by_id("1", lista)) == "protectie"
    assert get_pret(get_by_id("1", lista)) == 1.0
    assert get_location(get_by_id("1", lista)) == "Cora"


def test_delete_object():
    lista = []
    lista = add_object("1", "mustar", "dulce", 10, "Penny", lista)
    lista = add_object("2", "sunca", "porc", 12, "Profi", lista)
    lista = delete_object("1", lista)
    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None
    lista = delete_object("3", lista)
    assert len(lista) == 1
    assert get_by_id("2", lista) is not None




def test_modify_object():
    lista = []
    lista = add_object("1", "farfurie", "plata", 9, "Auchan", lista)
    lista = add_object("2", "pahar", "sticla", 10, "Kaufland", lista)
    lista = modify_object("1", "solnita", "metal", 8, "MegaImage", lista)
    updated_object = get_by_id("1", lista)
    assert get_id(updated_object) == "1"
    assert get_name(updated_object) == "solnita"
    assert get_description(updated_object) == "metal"
    assert get_pret(updated_object) == 8
    assert get_location(updated_object) == "MegaImage"
    out_dated_object = get_by_id("2", lista)
    assert get_id(out_dated_object) == "2"
    assert get_name(out_dated_object) == "pahar"
    assert get_description(out_dated_object) == "sticla"
    assert get_pret(out_dated_object) == 10
    assert get_location(out_dated_object) == "Kaufland"
    lista = []
    lista = add_object("1", "farfurie", "plata", 9, "Auchan", lista)
    lista = modify_object("3", "solnita", "metal", 8, "MegaImage", lista)
    out_dated_object = get_by_id("1", lista)
    assert get_id(out_dated_object) == "1"
    assert get_name(out_dated_object) == "farfurie"
    assert get_description(out_dated_object) == "plata"
    assert get_pret(out_dated_object) == 9
    assert get_location(out_dated_object) == "Auchan"


def test_get_by_id():
    lista = []
    lista = add_object(1, "Calculator", "Horizon", 900.00, "birou", lista)
    lista = add_object(2, "Monitor Dell", "23.5'', HD, 148Hz", 1099.0, "sala conferinte", lista)
    assert get_id(get_by_id(2, lista)) == 2
    assert get_name(get_by_id(2, lista)) == "Monitor Dell"
    assert get_description(get_by_id(2, lista)) == "23.5'', HD, 148Hz"
    assert get_pret(get_by_id(2, lista)) == 1099.0
    assert get_location(get_by_id(2, lista)) == "sala conferinte"