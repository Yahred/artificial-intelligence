from classes.nodo import Nodo

def expand(nodo: Nodo):
    return [Nodo(hijo.valor) for hijo in nodo.hijos]

