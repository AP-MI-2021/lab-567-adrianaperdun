from Domain.rezervare import creeazaRezervare, getId


def adaugaRezervare(id,nume,clasa,pret,checkin, lista, undoList, redoList):
    '''
    adauga o noua rezervare
    :param id: id ul rezervarii
    :param nume: numele ei
    :param clasa: clasa ei
    :param pret: pretul ei
    :param checkin: daca are facut checkin-ul sau nu
    :param lista: lista cu toate rezervarile
    :return: lista cu noua rezervare adaugata
    '''
    for rez in lista:
        if getId(rez) == id:
            raise ValueError("Exista deja o rezervare cu acest id")
    rezervare= creeazaRezervare(id, nume, clasa, pret, checkin)
    undoList.append(lista)
    redoList.clear()
    return lista + [rezervare]


def stergeRezervare(id, lista, undoList, redoList):
    '''
    sterge rezervari cu un anumit id din lista
    :param id: id-ul rezervarii de sters
    :param lista: lista cu rezervari
    :return: o lista de rezervari cu id-ul diferit de id
    '''
    lista_noua = []
    for rezervare in lista:
        if getId(rezervare) != id:
            lista_noua.append(rezervare)
    return lista_noua


def modificaRezervare(id,nume,clasa,pret,checkin, lista, undoList, redoList):
    '''
    modifica o rezervare
    :param id: id ul ei
    :param nume: numele ei
    :param clasa: clasa ei
    :param pret: pretul ei
    :param checkin: daca are facut checkin ul
    :param lista: lista cu rezervarile
    :return: lista cu rezervarea noua modificata
    '''
    listaNoua= []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    undoList.append(lista)
    redoList.clear()
    return listaNoua


def getById(id, lista):
    '''
    gaseste o anumite rezervare
    :param id: idul rezervarii de gasit
    :param lista: lista cu rezervari
    :return: rezervarea gasita
    '''
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None