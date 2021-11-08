from Domain.obiect import creare_obiect, get_location, get_id


def add_object(id, nume, descriere, pret, locatie, lista):
    """
    Adaugare obiect nou in lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: list
    :return: Lista obtinuta dupa adugarea tuturor obiectelor.
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista!")
    if len(locatie) > 4:
        raise ValueError("Locatia trebuie sa continta cel mult 4 caractere!")
    if len(locatie) == 0:
        raise ValueError("Locatia nu poate fi nula!")
    obiect=creare_obiect(id, nume, descriere, pret, locatie)
    return lista+[obiect]


def get_by_id(id, lista):
    """
    Cauta in lista obiectul, caruia ii corespunde id-ul dat de utilizator.
    :param id: string
    :param lista: list
    :return: obiectul caruia ii apartine id-ul.
    """
    for object in lista:
        if get_id(object) == id:
            return object


def get_by_location(location, lista):
    """
    Cauta in lista obiectul, caruia ii corespunde locatia data de utilizator.
    :param location: string
    :param lista: list
    :return: obiectul caruia ii corespunde locatia.
    """
    for object in lista:
        if get_location(object) == location:
            return object


def delete_object(id, lista):
    """
    Sterge obiectul caruia ii corespunde id-ul dat.
    :param id: string
    :param lista: list
    :return: lista dupa eliminarea obiectului.
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Obiectul cu ID-ul introdus nu exista! Introduce-ti alt numar.")
    return [object for object in lista if get_id(object) != id ]


def modify_object(id, nume, descriere, pret, locatie, lista):
    """
    Obiectul care are id-ul dat de utilizator se va modifica.
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: list
    :return: lista dupa modificari.
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Obiectul cu ID-ul introdus nu exista! Introduce-ti alt numar")
    newlist = []
    for object in lista:
        if get_id(object) == id:
            newobject = creare_obiect(id, nume, descriere, pret, locatie)
            newlist.append(newobject)
        else:
            newlist.append(object)
    return newlist


