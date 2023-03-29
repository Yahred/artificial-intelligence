from busquedas.profundidad_iterada import profundidad_iterada
from utilities.crear_arbol import crear_arbol
from classes.nodo import Nodo
from busquedas.profundidad_limitada import profundidad_limitada


raiz = crear_arbol()

limite = 4

objetivo = Nodo(9)

def goal_test(estado_actual: Nodo):
    return estado_actual.valor == objetivo.valor

def expand(estado_actual: Nodo):
    return estado_actual.hijos

encontrado = profundidad_limitada([raiz], goaltest=goal_test, expand=expand, lim=limite)

print('Encontrado' if encontrado else 'No lo encontré')

encontrado_iterado = profundidad_iterada([raiz], goaltest=goal_test, expand=expand)

print('Encontrado Iterado' if encontrado else 'No lo encontré Iterado')
