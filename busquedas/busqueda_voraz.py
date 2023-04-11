from typing import Any, Callable
from random import randint

from classes.nodo import Nodo


def busqueda_voraz(frontera: list[Nodo], goaltest: Callable[[Any], bool], expand: Callable[[Any], list[Any]], evaluate: Callable[[Any], list[Any]]):

    if not frontera:
        return False

    estado_actual = frontera.pop(0)
    if goaltest(estado_actual):
        return estado_actual

    os = [{'child': child, 'eval': evaluate(child)}
          for child in expand(estado_actual)]

    if not os:
        return busqueda_voraz([], goaltest, expand, evaluate)

    os.sort(key=lambda child: child['eval'])

    ganador = os[0]['eval']

    empatados = 0
    for child in os:
        if child['eval'] != ganador:
            break
        empatados += 1

    frontera = [os[randint(0, empatados - 1)]['child']]

    return busqueda_voraz(frontera, goaltest, expand, evaluate)
 