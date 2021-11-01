from Domain.obiect import creare_obiect, get_id, get_name, get_description, get_pret, get_location


def test_object():
    obiect = creare_obiect("1", "cana", "ceramica", 35, "bucatarie")
    assert get_id(obiect) == "1"
    assert get_name(obiect) == "cana"
    assert get_description(obiect) == "ceramica"
    assert get_pret(obiect) == 35
    assert get_location(obiect) == "bucatarie"
