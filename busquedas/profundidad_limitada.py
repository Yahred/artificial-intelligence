from typing import Any, Callable

from utilities.asignar_niveles import asignar_niveles

def profundidad_limitada(frontera: list[Any], goaltest: Callable[[Any], bool], expand: Callable[[Any], list[Any]], lim: int):     
    if not frontera:
        return False

    estado_actual = frontera.pop(0)

    if goaltest(estado_actual):
        return True

    os = []
    if estado_actual.nivel <= lim:
        os = expand(estado_actual)
        asignar_niveles(os, estado_actual.nivel + 1)

    frontera = os + frontera

    return profundidad_limitada(frontera, goaltest, expand, lim)