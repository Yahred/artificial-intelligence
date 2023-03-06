from typing import Any, Callable

def busqueda_ancho(frontera: list[Any], goaltest: Callable[[Any], bool], expand: Callable[[Any], list[Any]]): 
    if not frontera:
        return False

    estado_actual = frontera.pop(0)
    if goaltest(estado_actual):
        return True

    os = expand(estado_actual)
    frontera = frontera + os

    return busqueda_ancho(frontera, goaltest, expand)
