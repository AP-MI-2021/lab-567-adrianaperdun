def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    Creaza o rezervare
    :param ID: str
    :param nume: str
    :param clasa: str
    :param preț: float
    :param checkin: str
    :return: un dictionar ce retine o prajitura
    '''

    return {
        'id' : id,
        'nume' : nume,
        'clasa' : clasa,
        'pret': pret,
        'checkin': checkin
    }

def getId(rezervare):
    return rezervare['id']

def getNume(rezervare):
    return rezervare['nume']

def getClasa(rezervare):
    return rezervare['clasa']

def getPret(rezervare):
    return rezervare['pret']

def getCheckin(rezervare):
    return rezervare['checkin']


def toString(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )