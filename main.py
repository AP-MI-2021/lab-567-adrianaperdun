from Logic.crud import adaugaRezervare
from Tests.testALL import alltests
from UI.console import runMenu


def main():
    alltests()
    undoList= []
    redoList= []
    lista= adaugaRezervare('1', 'Adriana', 'economy', 200, 'Da', [], undoList, redoList)
    lista= adaugaRezervare('2', 'Ioana', 'business', 202, 'Nu', lista, undoList, redoList)
    lista = adaugaRezervare('3', 'Naomi', 'economy', 100, 'Da', lista, undoList, redoList)
    lista = adaugaRezervare('4', 'Magda', 'economy plus', 50, 'Da', lista, undoList, redoList)
    lista = adaugaRezervare('5', 'Teo', 'economy', 170, 'Da', lista, undoList, redoList)
    runMenu(lista)

main()