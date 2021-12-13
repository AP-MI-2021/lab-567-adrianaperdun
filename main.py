from Logic.crud import add
from Test.tests import alltest
from UI.console import startmenu


def main():
    alltest()
    lista = []
    lista= add('1', 'Adriana', 'economy', 200, 'Da', lista)
    lista= add('2', 'Andreea', 'business', 202, 'Nu', lista)
    lista = add('3', 'Andreea', 'economy', 100, 'Da', lista)
    lista = add('4', 'Magda', 'economy plus', 50, 'Da', lista)
    lista = add('5', 'Teo', 'economy', 170, 'Da', lista)
    startmenu(lista)

main()
