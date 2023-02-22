from nodo import *
from expand import *

def busqueda_ancho(frontera: list[Nodo], objetivo: Nodo): 
    if not len(frontera):
        return 'No Encontrado'

    estadoActual = frontera.pop(0)

    if estadoActual.valor == objetivo:
        return 'Encontrado'

    offspring = expand(estadoActual)
    frontera = frontera + offspring

    busqueda_ancho(frontera, objetivo)