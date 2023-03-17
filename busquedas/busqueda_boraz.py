from typing import Callable

from pyparsing import Any
from classes.nodo import Nodo 

def busqueda_boraz(frontera: list[Nodo], goaltest: Callable[[Any], bool], expand: Callable[[Any], list[Any]], evaluate: Callable[[Any], list[Any]], sort_func: Callable):
    if not frontera:
        return False

    estado_actual = frontera.pop(0)
    if goaltest(estado_actual):
        return True

    os = expand(estado_actual)
    os.sort(key=sort_func)
    
    frontera = [ os[0] ]

    return busqueda_boraz(frontera, goaltest, expand, evaluate, sort_func)