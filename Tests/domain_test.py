from Domain.obiect import creare_obiect, get_id, get_name, get_description, get_pret, get_location


def test_object():
    obiect = creare_obiect("1", "Smartphone", "Iphone 12 Pro Max", 3530, "sala")
    assert get_id(obiect) == "1"
    assert get_name(obiect) == "Smartphone"
    assert get_description(obiect) == "Iphone 12 Pro Max"
    assert get_pret(obiect) == 3530
    assert get_location(obiect) == "sala"
