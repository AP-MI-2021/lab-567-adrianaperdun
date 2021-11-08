from Logic.crud import add_object


def undo_test():
    lista = []
    undo_lista = []
    redo_lista = []

    rez = add_object("1", "imprimanta", "laser", 2300, "sala", lista)
    undo_lista.append(rez)
    lista = rez

    assert len(undo_lista) == 1
    assert len(redo_lista) == 0