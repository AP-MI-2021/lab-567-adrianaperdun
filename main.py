
from Logic.crud import adaugaRezervare
from UI.console import printMenu1, runMenu


def main():
    lista = []
    lista = adaugaRezervare("1", "Ana", "business", 200, "nu", lista)
    lista = adaugaRezervare("2", "Teo", "economy", 1400, "da", lista)
    lista = adaugaRezervare("3", "Magda", "business", 100, "nu", lista)
    lista = adaugaRezervare("4", "Madalina", "economy", 1400, "da", lista)
    lista = adaugaRezervare("5", "Bogdan", "business", 2300, "nu", lista)
    lista = adaugaRezervare("6", "Octavian", "economy", 140, "da", lista)
    runMenu(lista)

main()
