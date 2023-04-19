import tkinter as tk
from threading import Thread
from busquedas.busqueda_a_estrella import busqueda_a_estrella

from classes.laberinto import Casilla, Laberinto, Visitante


porcentaje_obstaculos = int(input('Introduzca el porcentaje de obstaculos:'))

root = tk.Tk()
laberinto = Laberinto(porcentaje_obstaculos, 40, True)

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

def x(casilla: Casilla, visitante: Visitante):
    return visitante.distancia_caminada + 1

def evaluate(casilla: Casilla, visitante: Visitante):
    visitante.distancia_caminada = x(casilla, visitante)
    return h(casilla, laberinto.casilla_objetivo) + x(casilla, visitante)


def iniciar_competicion():
    visitante_a = Visitante()
    visitante_b = Visitante()

    laberinto.agregar_visitante(visitante_a)
    laberinto.agregar_visitante(visitante_b)

    hilos: list[Thread] = []
    def competir(visitante: Visitante):
        busqueda_a_estrella([visitante.casilla_actual], lambda casilla: goal_test(
            casilla, visitante), lambda casilla: expand(casilla, visitante), evaluate=lambda casilla: evaluate(casilla, visitante))
        visitante.animar_recorrido()

    hilos.append(Thread(target=competir, args=(visitante_a,)).start())
    hilos.append(Thread(target=competir, args=(visitante_b,)).start())
    
laberinto.pack()
root.after(1000, iniciar_competicion)
root.mainloop()