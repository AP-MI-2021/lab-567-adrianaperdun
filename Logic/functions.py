from Domain.obiect import get_location, get_pret, get_description


def move_object(old_location, new_location, lista):
	"""
	muta obiectele dintr-o locatie in alta
	:param old_location: locatia de unde se muta obiectele
	:param new_location: locatia unde se muta obiectele
	:return: lista dupa mutare
	"""
	exist_old_location = False
	for obiect in lista:
		if get_location(obiect) == old_location:
			exist_old_location = True
			obiect["locatie"] = new_location
	if exist_old_location is False:
		raise ValueError("Locatia aleasa nu exista! Incercati alta locatie!")
	if len(new_location) != 4:
		raise ValueError("Locatia noua trebuie sa aiba exact 4 caractere!")
	if old_location == new_location:
		raise RuntimeError("Cele doua locatii trebuie sa fie diferite!")
	return lista


def concat_str(obiect, str):
	"""
    concateneaza un string la descrierea unui obiect
	:param obiect: obiectul
	:param str: stringul
	:return: obiectul dupa concatenare
	"""
	obiect["descriere"] = get_description(obiect) + str
	return obiect


def max_price(lista):
	"""
	pentru fiecare locatie determina cel mai mare pret
	:param lista: lista de obiecte
	:return: un dictionar
	"""
	rezultat = {}
	for obiect in lista:
		pret = get_pret(obiect)
		locatie = get_location(obiect)
		if locatie in rezultat:
			if pret > rezultat[locatie]:
				rezultat[locatie] = pret
		else:
			rezultat[locatie] = pret
	return rezultat


def ascending_order(lista):
	"""
	ordoneaza crescator obiectele din lista dupa pretul de achizitie
	:param lista: lista de obiecte
	:return: lista ordonata crescator
	"""
	return sorted(lista, key=get_pret)


def sum(lista):
	"""
	pentru fiecare locatie determina suma preturilor
	:param lista: lista de obiecte
	:return: un dictionar
	"""
	rezultat = {}
	for obiect in lista:
		pret = get_pret(obiect)
		locatie = get_location(obiect)
		if locatie in rezultat:
			rezultat[locatie] += pret
		else:
			rezultat[locatie] = pret
	return rezultat