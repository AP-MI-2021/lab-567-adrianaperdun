from Domain.rezervare import toString
from Logic.Ieftinire import IeftinirePret
from Logic.cerinte import pretMaxim, ordo, sumaFiecareNume
from Logic.clasaSuperioara import UpgradeClasa
from Logic.crud import adaugaRezervare, modificaRezervare, stergeRezervare
from UI.commandline import commandLine


def printMenu():
    '''
    meniul afisat
    '''
    print("1. Adauga, sterge sau modifica o rezervare.")
    print("2. Trecerea la o clasa superioara a unui client, dupa nume.")
    print("3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("4. Determinarea prețului maxim pentru fiecare clasă.")
    print("5. Ordonarea rezervărilor descrescător după preț.")
    print("6. Afișarea sumelor prețurilor pentru fiecare nume")
    print("7. Command_line.")

    print("8. Undo.")
    print("9. Redo.")
    print("10. Afiseaza toate rezervarile.")
    print("x. Iesire.")


def uiAdaugaRezervare(lista, undoList, redoList):
    '''
    adauga o rezervare
    :param lista: lista de rezervari
    '''
    try:
        id = input('Dati id-ul: ')
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("S-a facut checkin-ul? Da/Nu: ")

        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista, undoList, redoList)
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
        id = input("Dati id-ul rezervarii ce trebuie sterse: ")
        rezultat = stergeRezervare(id, lista, undoList, redoList)
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

        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista, undoList, redoList)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare", ve)


def showAll(lista):
    '''
    afiseaza toate rezervarile facute
    :param lista: rezervarile facute
    '''
    for rezervare in lista:
        print(toString(rezervare))


def meniulDoi(lista):
    '''submeniul pentru optiunea 1'''

    undoList = []
    redoList = []
    while True:
        print('1.Adauga o rezervare.')
        print('2.Modifica o rezervare.')
        print('3.Sterge o rezervare.')
        print('4.Revenire la cealalta pagina de functionalitati.')
        print("5. Undo.")
        print("6. Redo.")
        print("7.Afiseaza lista de rezervari.")
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            lista = uiAdaugaRezervare(lista, undoList, redoList)
        elif optiune == '2':
            lista = uiModificaRezervare(lista, undoList, redoList)
        elif optiune == '3':
            lista = uiStergeRezervare(lista, undoList, redoList)
        elif optiune == 'a':
            showAll(lista)
        elif optiune == '4':
            return lista
        elif optiune == '5':
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face Undo!")
        elif optiune == '6':
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face Redo.")


def runMenu(lista):
    undoList = []
    redoList = []

    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = meniulDoi(lista)
        elif optiune == '3':
            showAll(lista)
        elif optiune == '2':
            try:
                numele = input("Dati numele clientului: ")
                lista = UpgradeClasa(lista, numele, undoList, redoList)
                print("Upgrade-ul s-a realizat.")
            except ValueError as ve:
                print("Eroare", ve)
        elif optiune == '3':
            try:
                procent = float(input("Cu cat la suta doriti sa se ieftineasca rezervarea?:"))
                lista = IeftinirePret(lista, procent, undoList, redoList)
                print("Preturile au fost reduse.")
            except ValueError as vee:
                print("Eroare", vee)
        elif optiune == '4':
            print(pretMaxim(lista))
        elif optiune == '5':
            lista = ordo(lista, undoList, redoList)
        elif optiune == '6':
            sumaFiecareNume(lista)

        elif optiune == 'u':
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face Undo!")
        elif optiune == 'r':
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face Redo.")


        elif optiune == '7':
            lista = commandLine(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida. Reincercati.")
