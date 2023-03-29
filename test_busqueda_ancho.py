
from busquedas.busqueda_ancho import busqueda_ancho
from classes.nodo import Nodo
from utilities.crear_arbol import crear_arbol

raiz = crear_arbol()

objetivo = Nodo(12)
encontrado = busqueda_ancho([raiz], lambda estado_actual: estado_actual.valor ==
                            objetivo.valor, lambda estado_actual: estado_actual.hijos)

print('Encontrado' if encontrado else 'No encontrado')
