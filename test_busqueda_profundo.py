
from busquedas.busqueda_profundo import busqueda_profundo
from classes.nodo import Nodo
from utilities.crear_arbol import crear_arbol

raiz = crear_arbol()

objetivo = Nodo(12)

encontrado = busqueda_profundo([raiz], goaltest=lambda e_a: e_a.valor == objetivo.valor,
                               expand=lambda e_a: e_a.hijos)

print('Encontrado' if encontrado else 'No encontrado')
