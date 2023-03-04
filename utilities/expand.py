from classes.nodo import Nodo

def expand(nodo: Nodo):
    return [hijo for hijo in nodo.hijos]

