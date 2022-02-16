from Domain.rezervare import getCheckin, creeazaRezervare, getPret, getNume, getId, getClasa


def IeftinirePret(lista,procent,undoList,redoList):
    if not (0 < procent < 100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100.')
    listaNoua=[]
    for rezervare in lista:
        if getCheckin(rezervare) == 'Nu':
            listaNoua.append(rezervare)
        else:
            rezervareNoua= creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare) - (getPret(rezervare)*(procent/100)),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
    undoList.append(lista)
    redoList.clear()
    return listaNoua