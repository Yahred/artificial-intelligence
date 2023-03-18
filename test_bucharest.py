from bucharest.crear_mapa import Mapa, Ciudad, Camino
from busquedas.busqueda_voraz import busqueda_voraz

distancias_bucharest = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitestu': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374, 
}

estado_inicial = Mapa()

objetivo = 'Bucharest'

def goal_test(estado_actual: Ciudad):
    return True if estado_actual.nombre == 'Bucharest' else False

def expand(estado_actual: Ciudad):
    return [camino.ciudad for camino in estado_actual.hijos]

def evaluate(child: Ciudad):
    return distancias_bucharest[child.nombre]

encontrado = busqueda_voraz([estado_inicial], goal_test, expand, evaluate)

print('Encontrado' if encontrado else 'No encontrado')