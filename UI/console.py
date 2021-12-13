from Domain.rezervare import to_string
from Logic.crud import add, delete, modify
from Logic.functions import Upgrade, reduce, max_price, ordo, suma, undo, redo
from UI.commandline import commandLine


def startmenu(lista):
    """
    meniul initial
    :return:
    """
    while True:
        print("1. Consola.")
        print("2. Command line.")
        op = input("Alegeti meniul: ")
        if op == "1":
            lista = printMenu()
        elif op == "2":
            lista = commandLine(lista)
        else:
            print("Optiune gresita. Reincercati.")


def uiupgrade(lista, undo_lista, redo_list):
    nume = input("Dati numele clasei: ")
    rez = Upgrade(nume, lista)
    undo_lista.append(lista)
    redo_list.clear()
    return rez


def uireduce(lista, undo_list, redo_list):
    try:
        p = int(input("Cu cat doriti sa se faca ieftinirea? "))
        rez = reduce(p, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rez
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def uimax(lista):
    rez = max_price(lista)
    return rez


def uiordo(lista):
    rez = ordo(lista)
    showAll(rez)


def uisuma(lista):
    rez = suma(lista)
    for n in rez:
        print("Pentru {} suma este: {}".format(n, rez[n]))


def printMenu():
    '''
    meniul afisat
    '''
    rezervari = []
    lista = []
    undo_list = []
    redo_list = []
    while True:
        print("1. Crud rezervare.")
        print("2. Trecerea la o clasa superioara, dupa nume.")
        print("3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
        print("4. Determinarea prețului maxim pentru fiecare clasă.")
        print("5. Ordonarea rezervărilor descrescător după preț.")
        print("6. Afișarea sumelor prețurilor pentru fiecare nume")
        print("7. Undo.")
        print("8. Redo.")
        print("x. Iesire.")
        op = input("Dati optiunea: ")
        if op == "1":
            lista = meniul2(lista)
        elif op == "2":
            lista = uiupgrade(lista, undo_list, redo_list)
        elif op == "3":
            lista = uireduce(lista, undo_list, redo_list)
        elif op == "4":
            uimax(lista)
        elif op == "5":
            uiordo(lista)
        elif op == "6":
            uisuma(lista)
        elif op == "7":
            rezervari = undo(rezervari, undo_list, redo_list)
        elif op == "8":
            rezervari = redo(rezervari, undo_list, redo_list)
        elif op == "x":
            break
        else:
            print("Optiunea este gresita. Reincercati.")



def uiAdaugaRezervare(lista, undoList, redoList):
    '''
    adauga o rezervare
    :param lista: lista de rezervari
    '''
    try:
        id=input('Dati id-ul: ')
        nume=input("Dati numele: ")
        clasa=input("Dati clasa: ")
        pret=float(input("Dati pretul: "))
        checkin=input("S-a facut checkin-ul? Da/Nu: ")

        rezultat = add(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare", ve)
        return lista


def uiStergeRezervare(lista, undoList, redoList):
    '''
    sterge o rezervare
    :param lista: lista de rezervari
    '''
    try:
        id=input("Dati id-ul rezervarii ce trebuie sterse: ")
        rezultat = delete(id,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare:", ve)



def uiModificaRezervare(lista, undoList, redoList):
    '''
    modifica o rezervare
    :param lista: lista de rezervari
    '''
    try:
        id = input('Dati id-ul rezervarii de modificat: ')
        nume = input("Dati numele nou: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("S-a facut checkin-ul? Da/Nu: ")

        rezultat = modify(id,nume,clasa,pret,checkin,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare",ve)


def showAll(lista):
    '''
    afiseaza toate rezervarile facute
    :param lista: rezervarile facute
    '''
    for rezervare in lista:
        print(to_string(rezervare))


def meniul2(lista):
    '''
    submeniul pentru optiunea 1
    '''

    undoList= []
    redoList= []
    while True:
        print('1.Adauga o rezervare.')
        print('2.Modifica o rezervare.')
        print('3.Sterge o rezervare.')
        print('4.Revenire la cealalta pagina de functionalitati.')
        print("5. Undo.")
        print("6. Redo.")
        print('7.Afiseaza lista de rezervari.')
        op = input('Alege optiunea: ')
        if op == '1':
            lista=uiAdaugaRezervare(lista,undoList,redoList)
        elif op == '2':
            lista = uiModificaRezervare(lista,undoList, redoList)
        elif op == '3':
            lista = uiStergeRezervare(lista,undoList, redoList)
        elif op == '7':
            showAll(lista)
        elif op == '4':
            return lista
        elif op == '5':
            if len(undoList) > 0:
                redoList.append(lista)
                lista= undoList.pop()
            else:
                print("Nu se poate face Undo!")
        elif op == '6':
            if len(redoList) > 0:
                undoList.append(lista)
                lista= redoList.pop()
            else:
                print("Nu se poate face Redo.")

def runMenu(lista):
    undoList= []
    redoList= []

    while True:
        printMenu()
        op=input("Dati optiunea: ")
        if op == "1":
            lista= meniul2(lista)
        elif op == 'a':
            showAll(lista)
        elif op == '2':
            try:
                numele=input("Dati numele clientului: ")
                lista=Upgrade(lista,numele,undoList, redoList)
                print("Upgrade-ul s-a realizat.")
            except ValueError as ve:
                print("Eroare", ve)
        elif op == '3':
            try:
                procent=float(input("Dati procentul cu care vreti sa se ieftineasca rezervarea:"))
                lista=reduce(lista,procent,undoList,redoList)
                print("Preturile au fost reduse.")
            except ValueError as vee:
                print("Eroare",vee)
        elif op == '4':
            print(max_price(lista,undoList,redoList))
        elif op == '5':
            lista=ordo(lista,undoList,redoList)
        elif op == '6':
            suma(lista)

        elif op == '7':
            if len(undoList) > 0:
                redoList.append(lista)
                lista= undoList.pop()
            else:
                print("Nu se poate face Undo!")
        elif op == '8':
            if len(redoList) > 0:
                undoList.append(lista)
                lista= redoList.pop()
            else:
                print("Nu se poate face Redo.")

        elif op == 'x':
            break
        else:
            print("Optiune invalida. Reincercati.")

