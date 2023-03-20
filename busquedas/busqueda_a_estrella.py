from typing import Callable


def busqueda_a_estrella(frontera: list[any], goaltest: Callable[[any], bool], expand: Callable[[any], list[any]], evaluate: Callable[[any], list[any]]):
    if not frontera:
        return False

    estado_actual = frontera.pop(0)
    if goaltest(estado_actual):
        return True

    os = expand(estado_actual)
    os.sort(key=evaluate)

    frontera = os + frontera

    return busqueda_a_estrella(frontera, goaltest, expand, evaluate)
