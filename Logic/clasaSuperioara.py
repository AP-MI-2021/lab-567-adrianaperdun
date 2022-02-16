from Domain.rezervare import getNume, getClasa, creeazaRezervare, getId, getPret, getCheckin


def UpgradeClasa(lista, nume, undoList, redoList):
    '''
    Trece clasa la una superioara
    :param lista: lista de rezervari
    :param nume: numele persoanei
    :return: lista dupa upgrade
    '''
    k=None
    for rezervare in lista:
        if getNume(rezervare) == nume:
            k=1
    if k is None:
        raise ValueError(f'Nu exista o rezervare pe numele {nume} pe care sa o trecem la o clasa superioara')
    listaNoua=[]
    for rezervare in lista:
        if getNume(rezervare) != nume:
            listaNoua.append(rezervare)
        else:
            if getClasa(rezervare) == 'economy':
                clasaNoua='economy plus'
            else:
                clasaNoua='business'
            rezervareNoua=creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                clasaNoua,
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
    undoList.append(lista)
    redoList.clear()
    return listaNoua