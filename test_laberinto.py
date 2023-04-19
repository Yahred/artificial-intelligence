from tkinter import ttk
import tkinter

from classes.nodo import Nodo
from classes.laberinto import Casilla, Laberinto, Visitante
from busquedas.busqueda_profundo import busqueda_profundo
from busquedas.busqueda_ancho import busqueda_ancho
from busquedas.busqueda_voraz import busqueda_voraz
from busquedas.busqueda_a_estrella import busqueda_a_estrella
from busquedas.profundidad_iterada import profundidad_iterada
from busquedas.profundidad_limitada import profundidad_limitada


def expand(casilla: Casilla, visitante: Visitante):
    visitante.agregar_ruta(casilla)

    return [casilla for casilla in laberinto.obtener_vecinos_casilla(casilla.x, casilla.y) if casilla not in visitante.ruta]


def goal_test(casilla: Casilla, visitante: Visitante):
    if casilla.es_objetivo:
        visitante.agregar_ruta(casilla)
        return True


def h(casilla: Casilla, objetivo: Casilla):
    x1 = casilla.x
    y1 = casilla.y
    x2 = objetivo.x
    y2 = objetivo.y

    distancia = abs(x2 - x1) + abs(y2 - y1)
    return distancia


def evaluate(casilla: Casilla):
    return h(casilla, laberinto.casilla_objetivo)

def evaluate_a_estrella(casilla: Casilla, visitante: Visitante):
    return h(casilla, laberinto.casilla_objetivo)


def expand_profundidad_limitada(hijo: Nodo, visitante: Visitante):
    casilla = hijo.valor
    visitante.agregar_ruta(casilla)
    return [Nodo(valor=casilla) for casilla in laberinto.obtener_vecinos_casilla(casilla.x, casilla.y) if casilla not in visitante.ruta]


def goaltest_profundidad_limitada(hijo: Nodo, visitante: Visitante):
    casilla = hijo.valor

    if casilla.es_objetivo:
        visitante.agregar_ruta(casilla)
        return True

def ejecutar_busqueda(metodo_busqueda: callable):
    visitante = Visitante()
    laberinto.agregar_visitante(visitante)

    metodo_busqueda([visitante.casilla_actual], lambda casilla: goal_test(
        casilla, visitante), lambda casilla: expand(casilla, visitante))
    visitante.animar_recorrido()


def ejecutar_profundidad_limitada():
    visitante = Visitante()
    laberinto.agregar_visitante(visitante)

    estado_inicial = Nodo(valor=visitante.casilla_actual)
    lim = 10
    profundidad_limitada(
        [estado_inicial], lambda hijo: goaltest_profundidad_limitada(hijo, visitante), lambda hijo: expand_profundidad_limitada(hijo, visitante), lim)
    visitante.animar_recorrido()


def ejecutar_profundidad_iterada():
    visitante = Visitante()
    laberinto.agregar_visitante(visitante)

    estado_inicial = Nodo(valor=visitante.casilla_actual)
    profundidad_iterada([estado_inicial], lambda hijo: goaltest_profundidad_limitada(
        hijo, visitante), lambda hijo: expand_profundidad_limitada(hijo, visitante), lambda: visitante.limpiar_recorrido())
    visitante.animar_recorrido()
    
def ejecutar_voraz():
    visitante = Visitante()

    laberinto.agregar_visitante(visitante)

    busqueda_voraz([visitante.casilla_actual], lambda casilla: goal_test(
        casilla, visitante), lambda casilla: expand(casilla, visitante), evaluate)

    visitante.animar_recorrido()    

def ejecutar_a_estrella():
    visitante = Visitante()
    laberinto.agregar_visitante(visitante)
    
    busqueda_a_estrella([visitante.casilla_actual], lambda casilla: goal_test(
        casilla, visitante), lambda casilla: expand(casilla, visitante), evaluate)
    visitante.animar_recorrido()


def iniciar():
    busqueda_seleccionada = seleccion_busqueda.current()

    if busqueda_seleccionada is None:
        return

    ejecucion_busquedas[busqueda_seleccionada]()


porcentaje_obstaculos = int(input('Introduzca el porcentaje de obstaculos: '))

root = tkinter.Tk()

root.title('Laberinto')

ejecucion_busquedas = [
    lambda: ejecutar_busqueda(busqueda_ancho),
    lambda: ejecutar_busqueda(busqueda_profundo),
    ejecutar_profundidad_limitada,
    ejecutar_profundidad_iterada,
    ejecutar_voraz,
    ejecutar_a_estrella
]

busquedas = [
    'Búsqueda a lo ancho',
    'Búsqueda a lo profundo',
    'Profundidad limitada',
    'Profundidad iterada',
    'Búsqueda voraz',
    'Búsqueda a*',
]
seleccion_busqueda = ttk.Combobox(values=busquedas)
seleccion_busqueda.pack()

boton_iniciar = ttk.Button(text='Iniciar recorrido', command=iniciar)
boton_iniciar.pack()

laberinto = Laberinto(porcentaje_obstaculos)
laberinto.pack()
root.mainloop()
