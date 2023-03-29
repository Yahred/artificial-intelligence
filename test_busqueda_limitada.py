from utilities.crear_arbol import crear_arbol
from classes.nodo import Nodo
from busquedas.profundidad_limitada import profundidad_limitada


raiz = Nodo(1)

nivel_1_1 = Nodo(2)
nivel_1_2 = Nodo(3)
raiz.hijos = [nivel_1_1, nivel_1_2]

nivel_2_1 = Nodo(4)
nivel_2_2 = Nodo(5)
nivel_2_3 = Nodo(6)
nivel_2_4 = Nodo(7)

#Hijos del nivel 1
nivel_1_1.hijos = [nivel_2_1, nivel_2_2]
nivel_1_2.hijos = [nivel_2_3, nivel_2_4]

#nivel 3
nivel_3_1 = Nodo(8)
nivel_3_2 = Nodo(9)
nivel_3_3 = Nodo(10)
nivel_3_4 = Nodo(11)
nivel_3_5 = Nodo(12)
nivel_3_6 = Nodo(13)
nivel_3_7 = Nodo(14)
nivel_3_8 = Nodo(15)

#hijos del nivel 2
nivel_2_1.hijos = [nivel_3_1, nivel_3_2]
nivel_2_2.hijos = [nivel_3_3, nivel_3_4]
nivel_2_3.hijos = [nivel_3_5, nivel_3_6]
nivel_2_4.hijos = [nivel_3_7, nivel_3_8]

limite = 4

objetivo = Nodo(9)

def goal_test(estado_actual: Nodo):
    return estado_actual.valor == objetivo.valor

def expand(estado_actual: Nodo):
    return estado_actual.hijos

encontrado = profundidad_limitada([raiz], goaltest=goal_test, expand=expand, lim=limite)

print('Encontrado' if encontrado else 'No lo encontré')

