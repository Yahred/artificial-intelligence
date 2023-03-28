from typing import Any, Callable
from random import randint

from classes.nodo import Nodo


def busqueda_voraz(frontera: list[Nodo], goaltest: Callable[[Any], bool], expand: Callable[[Any], list[Any]], evaluate: Callable[[Any], list[Any]]):
    if not frontera:
        return False

    estado_actual = frontera.pop(0)
    if goaltest(estado_actual):
        return estado_actual

    os = expand(estado_actual)
    
    ganador = None
    if os:
        valor_ganador = min([evaluate(child) for child in os])

        empatados = [child for child in os if evaluate(child) == valor_ganador]

        ganador = empatados[randint(0, len(empatados) - 1)]
        print(ganador)

    frontera = [ganador] if ganador else []

    return busqueda_voraz(frontera, goaltest, expand, evaluate)
