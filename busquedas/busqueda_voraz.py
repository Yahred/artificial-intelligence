from typing import Any, Callable

from classes.nodo import Nodo


def busqueda_voraz(frontera: list[Nodo], goaltest: Callable[[Any], bool], expand: Callable[[Any], list[Any]], evaluate: Callable[[Any], list[Any]]):
    if not frontera:
        return False

    estado_actual = frontera.pop(0)
    if goaltest(estado_actual):
        return True

    os = expand(estado_actual)
    os.sort(key=evaluate)

    frontera = [os[0]]

    return busqueda_voraz(frontera, goaltest, expand, evaluate)
