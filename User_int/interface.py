from Domain.obiect import to_string, get_pret
from Logic.crud import modify_object, add_object, delete_object
from Logic.functions import move_object, concat_str, max_price, ascending_order


def print_menu():
    print("1. Adaugare obiect.")
    print("2. Stergere obiect.")
    print("3. Modificare obiect.")
    print("4. Afisare obiecte.")
    print("5. Mutarea obiectelor dintr-o locație în alta")
    print("6. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    print("7. Cel mai mare preț pentru fiecare locație")
    print("8. Obiectele ordonate crescător după prețul de achiziție")
    print("9. Afișarea sumelor prețurilor pentru fiecare locație")
    print("x. Iesire")


def user_int_add_object(lista):
    try:
        id = int(input("Introduceti ID-ul: "))
        nume = input("Introduceti numele: ")
        descriere = input("Introduceti descrierea: ")
        pret_achizitie = float(input("Introduceti pretul: "))
        locatie = input("Introduceti locatia: ")
        return add_object(id, nume, descriere, pret_achizitie, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def user_int_delete_object(lista):
    try:
        id = int(input("Introduceti ID-ul obiectului de sters: "))
        return delete_object(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def user_int_modify_object(lista):
    try:
        id = int(input("Introduceti ID-ul obiectului de modificat: "))
        nume = input("Introduceti noul nume: ")
        descriere = input("Introduceti noua descriere: ")
        pret = float(input("Introduceti noul pret: "))
        locatie = input("Introduceti noua locatie: ")
        return modify_object(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def user_int_move_object(lista):
    try:
        old_location = input("Introduceti locatia obiectelor pe care vreti sa le mutati: ")
        new_location = input("Introduceti noua locatie: ")
        return move_object(old_location, new_location, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    except RuntimeError as re:
        print("Atentie! {}".format(re))
        return lista


def user_int_concat_str(lista):
    try:
        str = input("Introduceti stringul: ")
        us_pret = float(input("Introduceti un pret: "))
        for obiect in lista:
            if get_pret(obiect) > us_pret:
                obiect = concat_str(obiect, str)
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def user_int_max_price(lista):
    rezultat = max_price(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim de {}".format(locatie, rezultat[locatie]))


def user_int_ascending_order(lista):
    show(ascending_order(lista))


def user_int_sum(lista):
    rezultat = sum(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor de {}".format(locatie, rezultat[locatie]))



def show(lista):
    for object in lista:
        print(to_string(object))



def run_user_int(lista):
    while True:
        print_menu()
        op = input("Dati optiunea: ")
        if op == "1":
            lista = user_int_add_object(lista)
        elif op == "2":
            lista = user_int_delete_object(lista)
        elif op == "3":
            lista = user_int_modify_object(lista)
        elif op == "4":
            show(lista)
        elif op == "5":
            user_int_move_object(lista)
        elif op == "6":
            user_int_concat_str(lista)
        elif op == "7":
            user_int_max_price(lista)
        elif op == "8":
            user_int_ascending_order(lista)
        elif op == "9":
            user_int_sum(lista)
        elif op == "x":
            break
        else:
            print("Eroare. Inceracti alta optiune ")