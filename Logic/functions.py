from Domain.rezervare import get_nume, get_pret, get_clasa, create, get_checkin, get_id


def max_price(lista):
    '''
    Determinarea prețului maxim pentru fiecare clasă.
    :param lista: lista de rezervari
    :return: preturile maxime de la clase
    '''
    maxEconomy = -1
    maxEconomyPlus = -1
    maxBusiness = -1
    for rezervare in lista:
        if get_clasa(rezervare) == "economy" and get_pret(rezervare) >= maxEconomy:
            maxEconomy = get_pret(rezervare)
        elif get_clasa(rezervare) == "economy plus" and get_pret(rezervare) >= maxEconomyPlus:
            maxEconomyPlus = get_pret(rezervare)
        elif get_clasa(rezervare) == "business" and get_pret(rezervare) >= maxBusiness:
            maxBusiness = get_pret(rezervare)
    if maxEconomy > -1:
        print("Pretul maxim la clasa economy este: " + str(maxEconomy))
    else:
        print("Nu sunt rezervari la clasa economy")
    if maxEconomyPlus > -1:
        print("Pretul maxim la clasa economy plus este: " + str(maxEconomyPlus))
    else:
        print("Nu sunt rezervari la clasa economy plus!")
    if maxBusiness > -1:
        print("Pretul maxim la clasa business este: " + str(maxBusiness))
    else:
        print("Nu sunt rezervari la clasa economy plus")


def ordo(lista):
    '''
    ordoneaza descrescator rezervarile dupa pret
    '''
    return sorted(lista, key=lambda rezervare: get_pret(rezervare), reverse=True)


def suma(lista):
    '''
    afiseaza suma preturilor pt fiecare nume
    :param lista: lista de rezervari
    :return:
    '''
    rezultat = {}
    for rezervare in lista:
        nume = get_nume(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + get_pret(rezervare)
        else:
            rezultat[nume] = get_pret(rezervare)
    return rezultat


def undo(lista,undoList,redoList):
    if undoList:
        Undo1=undoList.pop()
        redoList.append(Undo1)
        return Undo1
    return lista


def redo(lista,undoList,redoList):
    if redoList:
        redo1=redoList.pop()
        undoList.append(redo1)
        return redo1
    return lista

def reduce(lista,procent):
    if not (0 < procent < 100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100.')
    listaNoua=[]
    for rezervare in lista:
        if get_checkin(rezervare) == 'Nu':
            listaNoua.append(rezervare)
        else:
            rezervareNoua= create(
                get_id(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                get_pret(rezervare) - (get_pret(rezervare)*(procent/100)),
                get_checkin(rezervare)
            )
            listaNoua.append(rezervareNoua)
    return listaNoua

def Upgrade(lista, nume):
    """Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
    :param nume: numele citit
    :param lista: lista finala dupa schimbarea clasei
    :return:
    """
    listaNoua = []
    for rezervare in lista:
        if nume == get_nume(rezervare) and get_clasa(rezervare) == "economy":
            modificaRezervare = create(
                get_id(rezervare),
                get_nume(rezervare),
                "economy plus",
                get_pret(rezervare),
                get_checkin(rezervare)
            )
            listaNoua.append(modificaRezervare)
        elif nume == get_nume(rezervare) and get_clasa(rezervare) == "economy plus":
            modificaRezervare = create(
                get_id(rezervare),
                get_nume(rezervare),
                "business",
                get_pret(rezervare),
                get_checkin(rezervare)
            )
            listaNoua.append(modificaRezervare)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def procentaj(procentaj, pret):
    '''
    calculeaza ieftinirea  pretulul cu un procentaj dat
    :param procentaj: procentajul dat, int
    :param pret: pretul rezervarii
    :return: returneaza calculul ieftinirii pretului cu un procentaj dat
    '''
    return pret - (pret * (procentaj / 100))

def get_by_name(nume, lista):
    '''
    gaseste o rezervare cu numele dat intr-o lista
    :param nume: numele dat
    :param lista: lista de rezervari
    :return: rezervarea cu numele dat din lista sau None, daca aceasta nu exista
    '''
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            return rezervare
    return None

def get_by_checkin(lista):
    '''
     gaseste o rezervare dupa checkin in lista
    :param lista:lista de rezervari
    :return: rezervarea cu checkin-ul "Da" dintr-o lista
    '''

    for rezervare in lista:
        if get_checkin(rezervare) == "da":
            return rezervare
    return None