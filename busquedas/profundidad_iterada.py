from tkinter.messagebox import NO
from typing import Any, Callable

from busquedas.profundidad_limitada import profundidad_limitada


def profundidad_iterada(frontera: list[Any], goaltest: Callable[[Any], bool], expand: Callable[[Any], list[Any]], cambio_nivel: Callable = None):
    lim = 2
    encontrado = False

    while not encontrado:
        encontrado = profundidad_limitada(
            frontera.copy(), goaltest, expand, lim)
        cambio_nivel and cambio_nivel()
        lim += 2

    return encontrado
