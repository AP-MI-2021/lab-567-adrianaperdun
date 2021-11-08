from Domain.obiect import to_string
from Logic.crud import delete_object, modify_object, add_object


def Show(lista):
    for obiect in lista:
        print(to_string(obiect))


def mmain(lista):
    while True:
        m = input()
        if m == "help":
            print("Add, id, nume, descriere, pret, locatie => adauga obiect")
            print("Delete, id => sterge obiect")
            print("Update, id => modifica obiect")
            print("Show_all => afiseaza toate obiectele")
            print("Exit => opreste programul")
        else:
            op = m.split(";")
            if op[0] == "Exit!":
                break
            else:
                for opt in op:
                    c = opt.split(",")
                    if c[0] == "Add":
                        try:
                            lista = add_object(c[1], c[2], c[3], c[4], c[5], lista)
                        except ValueError as ve:
                            print("Eroare : {}".format(ve))
                    elif c[0] == "Showall":
                        Show(lista)
                    elif [0] == "Update":
                        lista = modify_object(c[1], c[2], c[3], c[4], c[5], lista)
                    elif c[0] == "Delete":
                        try:
                            lista = delete_object(c[1], lista)
                        except ValueError as ve1:
                            print("Eroare : {}".format(ve1))
                    else:
                        print("Optiune gresita! Acceseaza comanda 'help'!")