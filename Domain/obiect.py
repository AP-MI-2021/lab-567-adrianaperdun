def creare_obiect(id, nume, descriere, pret, locatie):
    """
    Creeaza o lista, ce reprezinta informatii despre un obiect.
    param. id: string
    param. nume: string
    param. descriere: string
    param. pret: float
    param. locatie: string
    :return: caracteristicile obiectului
    """
    if id < '1':
        raise ValueError("ID-ul introdus nu e bun, deoarece nu poate fi nul sau negativ!")
    if len(nume) == 0:
        raise ValueError("Numele introdus nu e bun, reincercati!")
    if len(descriere) == 0:
        raise ValueError("Descrierea nu poate lipsi. Va rugam sa adaugati descriere!")
    if float(pret).is_integer() is True and len(str(float(pret))) != 4:
        raise ValueError("Pretul de achizitie nu poate depasi 4 caractere. Introduceti alt pret!")
    if float(pret).is_integer() is False and len(str(pret).replace(".", "")) != 4:
        raise ValueError("Pretul de achizitie are doar 4 carctere. Introduceti alt pret!")
    if len(locatie) != 4:
        raise ValueError("Locatia trebuie sa aiba 4 caractere!")
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
