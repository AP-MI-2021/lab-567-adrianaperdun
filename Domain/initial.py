def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    creeaza o rezervare
    :param id: id-ul rezervarii
    :param nume: numele pasagerului
    :param clasa: clasa la care zboara pasagerul
    :param pret: pretul biletului
    :param checkin: si-a facut sau nu checkin-ul pasagerul
    :return: un dictionar cu datele despre rezervare
    '''
    return [('id', id,),('nume', nume,), ('clasa', clasa,), ('pret', pret,),('checkin',checkin,)]


def getId(rezervare):
    '''
    ia id-ul rezervarii
    :param rezervare: dictionar de tipuil rezervare
    :return: id-ul rezervarii
    '''
    return rezervare[0][1]


def getNume(rezervare):
    '''
    ia numele rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: numele rezervarii
    '''
    return rezervare[1][1]


def getClasa(rezervare):
    '''
    ia clasa rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: clasa rezervarii (economy, economy plus, business)
    '''
    return rezervare[2][1]


def getPret(rezervare):
    '''
    ia pretul rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: pretul rezervarii
    '''
    return rezervare[3][1]


def getCheckin(rezervare):
    '''
    ia checkin-ul rezervarii (da/nu)
    :param rezervare: dictionar de tipul rezervare
    :return: da/nu
    '''
    return rezervare[4][1]


def toString(rezervare):
    '''
    afiseaza toate datele despre rezervare
    :param rezervare: dictionar de tipul rezervare
    '''
    if getCheckin(rezervare) == 'Da':
        checkin = 'a fost facut'
    else:
        checkin = 'nu a fost facut'
    return f"Rezervarea cu ID-ul {getId(rezervare)} este facuta pe numele {getNume(rezervare)}, este incadrata in clasa " \
           f"{getClasa(rezervare)}, cu pretul de {getPret(rezervare)} lei si checkin-ul {checkin}."