from typing import Any, Callable

from busquedas.profundidad_limitada import profundidad_limitada

def profundidad_iterada(frontera: list[Any], goaltest: Callable[[Any], bool], expand: Callable[[Any], list[Any]], lim: int):
    lim = 2

    while True:
        if profundidad_limitada(frontera, goaltest, expand, lim):
            return True
        
        lim += 2
    
