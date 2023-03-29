from classes.nodo import Nodo

def asignar_niveles(nodos: list[Nodo], nivel: int):
    for nodo in nodos:
        nodo.nivel = nivel