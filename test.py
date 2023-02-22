from busqueda_ancho import *
from nodo import * 

raiz = Nodo(1)
nivel_1_1 = Nodo(2)
nivel_1_2 = Nodo(3)
nivel_1_3 = Nodo(4)
raiz.hijos = [nivel_1_1, nivel_1_2, nivel_1_3]

print(busqueda_ancho([raiz], 3))