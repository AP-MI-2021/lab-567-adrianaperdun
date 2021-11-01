def creare_obiect(id, nume, descriere, pret, locatie):
    """
    creeaza un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie:string
    :return: un obiect
    """
    return [
        id,
        nume,
        descriere,
        pret,
        locatie
    ]


def get_id(obiect):
    """
    id obiect
    :param obiect: obiectul
    :return: id-ul obiectului dat ca parametru
    """
    return obiect[0]


def get_nume(obiect):
    """
    nume obiect
    :param obiect: obiectul
    :return: numele obiectului dat ca parametru
    """
    return obiect[1]


def get_descriere(obiect):
    """
    descriere obiect
    :param obiect: obiectul
    :return: descrierea obiectului dat ca parametru
    """
    return obiect[2]


def get_pret(obiect):
    """
    pret obiect
    :param obiect: obiectul
    :return: pretul obiectului dat ca parametru
    """
    return obiect[3]


def get_locatie(obiect):
    """
    locatie obiect
    :param obiect: obiectul
    :return: locatia obiectului dat ca parametru
    """
    return obiect[4]


def get_str(obiect):
    """
    :param obiect:
    :return: reprezentarea obiectului ca string
    """
    return f'Obiectul care are  id-ul {get_id(obiect)} este :{get_nume(obiect)}, avand descrierea: {get_descriere(obiect)} , ' \
           f'a costat {get_pret(obiect)} ' \
           f'si se afla in {get_locatie(obiect)}'