from classes.nodo import Nodo

def asignar_niveles(nodos: list[Nodo], nivel: int):
    return [Nodo(nodo.valor, nivel) for nodo in nodos]