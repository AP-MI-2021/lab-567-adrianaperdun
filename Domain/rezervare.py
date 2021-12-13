def create(id, nume, clasa, pret, checkin):
    '''
    Creaza o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: string
    :param checkin: string
    :return: un dictionar ce retine o prajitura
    '''
    if id < '1':
        raise ValueError("ID-ul nu poate fi nul sau negativ! Introduceti alt id!")
    if len(nume) == 0:
        raise ValueError("Numele nu poate fi nul! Introduceti un nume!")
    return {
        'id': id,
        'nume': nume,
        'clasa': clasa,
        'pret': pret,
        'checkin': checkin
    }

def get_id(rezervare):
    """
    :param rezervare: locul unde gasim rezervarea
    :return: id
    """
    return rezervare["id"]

def get_nume(rezervare):
    """
    :param rezervare: locul unde gasim rezervarea
    :return: nume
    """
    return rezervare["nume"]

def get_clasa(rezervare):
    """
    :param rezervare: locul unde gasim rezervarea
    :return: clasa
    """
    return rezervare["clasa"]

def get_pret(rezervare):
    """
    :param rezervare: locul unde gasim rezervarea
    :return: pret
    """
    return rezervare["pret"]

def get_checkin(rezervare):
    """
    :param rezervare: locul unde gasim rezervarea
    :return: checkin
    """
    return rezervare["checkin"]


def to_string(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )