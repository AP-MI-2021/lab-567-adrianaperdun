from Domain.rezervare import get_id, create


def add(id, nume, clasa, pret, checkin, lista):
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
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    rezervare = create(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def delete(id, lista):
    '''
    sterge rezervarea dupa id-ul din lista
    :param id: id-ul rezervarii de sters, str
    :param lista:lista de rezervari
    :return: o lista continand rezervarile cu id-ul direrit de id
    '''

    return [rezervare for rezervare in lista if get_id(rezervare) != id]


def modify(id,nume,clasa,pret,checkin, lista):
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
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o prajitura cu Id-ul dat!")
    listaNoua = []
    for rezervare in lista:
        if get_id(rezervare) == id:
            rezervareNoua = create(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def get_by_id(id, lista):
    '''
    gaseste rezervare
    :param id: idul rezervarii de gasit
    :param lista: lista cu rezervari
    :return: rezervarea gasita
    '''
    for rezervare in lista:
        if get_id(rezervare) == id:
            return rezervare
    return None