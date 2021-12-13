from Domain.rezervare import getId, creeazaRezervare


def adaugaRezervare (id, nume, clasa, pret, checkin, lista):
    '''
    adauga o rezervare noua
    :param id: str
    :param nume: str
    :param clasa: str
    :param pret: float
    :param checkin: str
    :param lista: lista initiala
    :return:lista initiala cu adaugarea inclusa
    '''
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def stergereRezervare(id, lista):
    '''
    sterge rezervarea dupa id-ul din lista
    :param id: id-ul rezervarii de sters, str
    :param lista:lista de rezervari
    :return: o lista continand rezervarile cu id-ul direrit de id
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o prajitura cu Id-ul dat!")
    return [rezervare for rezervare in lista if getId(rezervare) != id]


def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    '''
    modifica o rezervare
    :param id: id actual
    :param nume: nume nou
    :param clasa:clasa noua
    :param pret: pret nou
    :param checkin:checkin nou
    :param lista: lista initiala de rezervari
    :return:lista initiala cu modificarea inclusa
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o prajitura cu Id-ul dat!")
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def getById(id, lista):
    '''
    gaseste o rezervare cu id-ul dat intr-o lista
    :param id: str
    :param lista: lista de rezervari
    :return:rezervarea cu id-ul dat din lista sau None, daca aceasta nu exista
    '''

    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None