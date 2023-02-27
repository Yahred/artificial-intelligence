from classes.nodo import Nodo
from utilities.expand import expand

def busqueda_ancho(frontera: list[Nodo], objetivo: Nodo): 
    if not frontera:
        return False

    estado_actual = frontera.pop(0)

    if estado_actual.valor == objetivo.valor:
        return True

    os = expand(estado_actual)
    frontera = frontera + os

    return busqueda_ancho(frontera, objetivo)
