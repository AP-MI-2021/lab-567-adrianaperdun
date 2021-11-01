def creare_obiect(id, nume, descriere, pret, locatie):
    """
    creeaza un dictionar ce reprezinta un obiect
    param. id: string
    param. nume: string
    param. descriere: string
    param. pret_achizitie: float (exact 4 caractere)
    param. locatie: string (exact 4 caractere)
    return: un dictionar
    """

    if id < '1':
        raise ValueError("ID-ul nu poate fi nul sau negativ! Introduceti alt id!")
    if len(nume) == 0:
        raise ValueError("Numele nu poate fi nul! Introduceti un nume!")
    if len(descriere) == 0:
        raise ValueError("Descrierea nu poate fi nula!")
    if pret.is_integer() is True and len(str(int(pret))) != 4:
        raise ValueError("Pretul trebuie sa aiba exact 4 cifre! Introduceti alt pret!")
    if pret.is_integer() is False and len(str(pret).replace(".", "")) != 4:
        raise ValueError("Pretul trebuie sa aiba exact 4 cifre! Introduceti alt pret!")
    if len(locatie) != 4:
        raise ValueError("Locatia trebuie sa aiba exact 4 caractere!")
    return {"id": id, "nume": nume, "descriere": descriere, "pret": pret, "locatie": locatie}


def get_id(obiect):
    """
    obiect: dictionar, unde gasim un obiect
    return: id-ul obiectului
    """
    return obiect["id"]


def get_name(obiect):
    """
    obiect: dictionar, unde gasim un obiect
    return: numele obiectului
    """
    return obiect["nume"]


def get_description(obiect):
    """
    obiect: dictionar, unde gasim un obiect
    return: descrierea obiectului
    """
    return obiect["descriere"]


def get_pret(obiect):
    """
    obiect: dictionar, unde gasim un obiect
    return: pretul de achizitie al obiectului
    """
    return obiect["pret"]


def get_location(obiect):
    """
    obiect: dictionar, unde gasim un obiect
    return: locatia obiectului
    """
    return obiect["locatie"]


def to_string(obiect):
    return f'Obiectul cu id-ul {get_id(obiect)}, aflat in {get_location(obiect)}, pretul{get_pret(obiect)} si numele {get_name(obiect)} are descrierea: {get_description(obiect)}.'
