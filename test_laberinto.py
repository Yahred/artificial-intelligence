from tkinter import ttk
import tkinter

from classes.laberinto import Casilla, Laberinto, Visitante
from busquedas.busqueda_profundo import busqueda_profundo
from busquedas.busqueda_ancho import busqueda_ancho
from busquedas.busqueda_voraz import busqueda_voraz
from busquedas.busqueda_a_estrella import busqueda_a_estrella

def expand(casilla: Casilla, visitante: Visitante):
    visitante.agregar_ruta(casilla)

    return [casilla for casilla in laberinto.obtener_vecinos_casilla(casilla.x, casilla.y) if casilla not in visitante.ruta]


def goal_test(casilla: Casilla, visitante: Visitante):
    if casilla.es_objetivo:
        visitante.agregar_ruta(casilla)
        return True

def g(casilla: Casilla, objetivo: Casilla):
    x1 = casilla.x
    y1 = casilla.y
    x2 = objetivo.x
    y2 = objetivo.y

    distancia = abs(x2 - x1) + abs(y2 - y1)
    return distancia

def evaluate(casilla: Casilla):
    return g(casilla, laberinto.casilla_objetivo)

def ejecutar_recorrido():
    visitante1 = Visitante()
    visitante2 = Visitante()
    
    laberinto.agregar_visitante(visitante1)
    laberinto.agregar_visitante(visitante2)
    
    busqueda_voraz([visitante1.casilla_actual], lambda casilla: goal_test(casilla, visitante1), lambda casilla: expand(casilla, visitante1), evaluate)
    busqueda_voraz([visitante2.casilla_actual], lambda casilla: goal_test(casilla, visitante2), lambda casilla: expand(casilla, visitante2), evaluate)
    
    visitante1.animar_recorrido()
    visitante2.animar_recorrido()

def ejecutar_busqueda(metodo_busqueda: callable):
    visitante = Visitante()
    laberinto.agregar_visitante(visitante)

    metodo_busqueda([visitante.casilla_actual], lambda casilla: goal_test(casilla, visitante), lambda casilla: expand(casilla, visitante))
    visitante.animar_recorrido()

def iniciar():
    busqueda_seleccionada = seleccion_busqueda.current()
    print(busquedas[busqueda_seleccionada])
    
    if busqueda_seleccionada is None:
        return

    ejecucion_busquedas[busqueda_seleccionada]()


porcentaje_obstaculos = int(input('Introduzca el porcentaje de obstaculos: '))

root = tkinter.Tk()

root.title('Laberinto')

ejecucion_busquedas = [
    lambda: ejecutar_busqueda(busqueda_ancho),
    lambda: ejecutar_busqueda(busqueda_profundo)
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
