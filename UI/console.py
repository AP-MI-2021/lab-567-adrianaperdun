from Domain.rezervare import toString
from Logic.crud import adaugaRezervare, stergereRezervare, modificaRezervare
from Logic.functions import trecereaClasaSuperioaraDupaNume, ieftinirePretRezervariDupaCheckin, \
    pretMaximRezervare, ordoneazaRezervarileDescrescDupaPret, sumaPreturiPerNume
from UI.commandline import commandLine


"""def startMenu(lista):
    lista = []
    print("1.Command line")
    print("2.Consola")
    while True:
        op = input("Dati optiune: ")

        if op == "1":
            commandLine(lista)
        elif op == "2":
            printMenu1()
        else:
            print("Optiune gresita!")"""


def printMenu1():
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervarea")
    print("4. Trece toate rezervările făcute pe un nume citit la o clasă superioară.")
    print("5. Ieftineste toate rezervările la care s-a făcut checkin cu un procentaj citit.")
    print("6. Determina prețul maxim pentru fiecare clasă.")
    print("7. Ordoneaza rezervările descrescător după preț.")
    print("8. Afișaza sumele prețurilor pentru fiecare nume")
    print("9. Undo")
    print("10. Redo")
    print("11. Afiseaza toate rezervariile")
    print("x. Iesire")


def uiAdaugaRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa (`economy`, `economy plus`, `business`): ")
        pret = float(input("Dati pret-ul: "))
        checkin = input("Dati checkin-ul făcut (`da` / `nu`): ")
        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroarea: ", ve)
        return lista


def uiStergereRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        rezultat = stergereRezervare(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroarea: ", ve)
        return lista


def uiModificaRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul numele: ")
        clasa = input("Dati noua clasa (`economy`, `economy plus`, `business`): ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Dati noul checkin făcut (`da` / `nu`): ")
        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroarea: ", ve)
        return lista


def uiTrecereaClasaSuperioaraDupaNume(lista, undoList, redoList):
    nume = input("Dati numele: ")
    rezultat = trecereaClasaSuperioaraDupaNume(nume, lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat


def uiIeftinirePretRezervariDupaCheckin(lista, undoList, redoList):
    try:
        procentaj = int(input("Dati procentajul cu care sa se faca ieftirirea:"))
        rezultat = ieftinirePretRezervariDupaCheckin(procentaj, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroarea: ", ve)
        return lista


def uiPretMaximRezervare(lista):
    rezultat = pretMaximRezervare(lista)
    return rezultat


def uiOrdoneazaRezervarileDescrescDupaPret(lista):
    rezultat = ordoneazaRezervarileDescrescDupaPret(lista)
    showAll(rezultat)


def uiSumaPreturiPerNume(lista):
    rezultat = sumaPreturiPerNume(lista)
    for nume in rezultat:
        print("Pentru numele {} suma preturilor este: {}".format(nume, rezultat[nume]))


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def runMenu(lista):
     undoList = []
     redoList = []
     while True:
         try:
            printMenu1()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                lista = uiAdaugaRezervare(lista, undoList, redoList)
            elif optiune == "2":
                lista = uiStergereRezervare(lista, undoList, redoList)
            elif optiune == "3":
                lista = uiModificaRezervare(lista, undoList, redoList)
            elif optiune == "4":
                lista = uiTrecereaClasaSuperioaraDupaNume(lista, undoList, redoList)
            elif optiune == "5":
                lista = uiIeftinirePretRezervariDupaCheckin(lista, undoList, redoList)
            elif optiune == "6":
                uiPretMaximRezervare(lista)
            elif optiune == "7":
                uiOrdoneazaRezervarileDescrescDupaPret(lista)
            elif optiune == "8":
                uiSumaPreturiPerNume(lista)
            elif optiune == "9":
                if len(undoList) > 0:
                    redoList.append(lista)
                    lista = undoList.pop()
                else:
                    print("Nu se poate face undo!")
            elif optiune == "10":
                if len(redoList) > 0:
                    undoList.append(lista)
                    lista = redoList.pop()
                else:
                    print("Nu se poate face redo!")
            elif optiune == "11":
                showAll(lista)
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati")
         except Exception as ex:
             print("Eroare: ", ex)