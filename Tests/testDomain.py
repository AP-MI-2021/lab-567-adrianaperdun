from Domain.rezervare import creeazaRezervare, getId, getNume, getPret, getCheckin, getClasa


def testDomain():
    '''testeaza daca aduga corect o rezervare'''
    rezervare=creeazaRezervare('1', 'Prigoana', 'economy', 200, 'Da')
    assert getId(rezervare) == '1'
    assert getNume(rezervare) == "Prigoana"
    assert getClasa(rezervare) == 'economy'
    assert getPret(rezervare) == 200
    assert getCheckin(rezervare) == "Da"