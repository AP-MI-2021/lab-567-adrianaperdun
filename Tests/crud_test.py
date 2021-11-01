from Domain.obiect import get_id, get_name, get_description, get_pret, get_location
from Logic.crud import add_object, get_by_id, delete_object, modify_object


def test_add_object():
    lista = []
    lista = add_object("1", "masca", "protectie", 1.0, "amf1", lista)
    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_name(get_by_id("1", lista)) == "masca"
    assert get_description(get_by_id("1", lista)) == "protectie"
    assert get_pret(get_by_id("1", lista)) == 1.0
    assert get_location(get_by_id("1", lista)) == "amf1"


def test_delete_object():
    lista = []
    lista = add_object("1", "mustar", "dulce", 10, "sal3", lista)
    lista = add_object("2", "sunca", "porc", 12, "dep2", lista)
    lista = delete_object("1", lista)
    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None
    lista = delete_object("3", lista)
    assert len(lista) == 1
    assert get_by_id("2", lista) is not None




def test_modify_object():
    lista = []
    lista = add_object("1", "Monitor", "HP", 9312, "bir3", lista)
    lista = add_object("2", "Tableta", "Samsung", 1000, "sala", lista)
    lista = modify_object("1", "Casti", "Hama", 1019, "amf2", lista)
    updated_object = get_by_id("1", lista)
    assert get_id(updated_object) == "1"
    assert get_name(updated_object) == "Casti"
    assert get_description(updated_object) == "Hama"
    assert get_pret(updated_object) == 1019
    assert get_location(updated_object) == "amf2"
    out_dated_object = get_by_id("2", lista)
    assert get_id(out_dated_object) == "2"
    assert get_name(out_dated_object) == "Tableta"
    assert get_description(out_dated_object) == "Samsung"
    assert get_pret(out_dated_object) == 1000
    assert get_location(out_dated_object) == "sala"
    lista = []
    lista = add_object("1", "Monitor", "HP", 9312, "bir2", lista)
    lista = modify_object("3", "Casti", "Hama", 1019, "sala", lista)
    out_dated_object = get_by_id("1", lista)
    assert get_id(out_dated_object) == "1"
    assert get_name(out_dated_object) == "Monitor"
    assert get_description(out_dated_object) == "HP"
    assert get_pret(out_dated_object) == 9312
    assert get_location(out_dated_object) == "bir2"


def test_get_by_id():
    lista = []
    lista = add_object(1, "Calculator", "Horizon", 900.00, "birou", lista)
    lista = add_object(2, "Monitor Dell", "23.5'', HD, 148Hz", 1099.0, "sala conferinte", lista)
    assert get_id(get_by_id(2, lista)) == 2
    assert get_name(get_by_id(2, lista)) == "Monitor Dell"
    assert get_description(get_by_id(2, lista)) == "23.5'', HD, 148Hz"
    assert get_pret(get_by_id(2, lista)) == 1099.0
    assert get_location(get_by_id(2, lista)) == "sala conferinte"