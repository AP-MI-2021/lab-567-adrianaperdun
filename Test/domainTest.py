from Domain.rezervare import create, get_id, get_nume, get_clasa, get_pret, get_checkin


def testDomain():
    '''
    testeaza daca aduga corect o rezervare
    '''
    rezervare=create('1', 'Adriana', 'economy', 200, 'Da')
    assert get_id(rezervare) == '1'
    assert get_nume(rezervare) == "Adriana"
    assert get_clasa(rezervare) == 'economy'
    assert get_pret(rezervare) == 200
    assert get_checkin(rezervare) == "Da"