import sys
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
    x1 = casilla.x + 1
    y1 = casilla.y + 1
    x2 = objetivo.x + 1
    y2 = objetivo.y + 1

    distancia = abs(x2 - x1) + abs(y2 - y1)
    return distancia


def x(casilla: Casilla, visitante: Visitante):
    return visitante.distancia_caminada + 1


def evaluate(casilla: Casilla, visitante: Visitante):
    visitante.distancia_caminada = x(casilla, visitante)
    return h(casilla, laberinto.casilla_objetivo)


def iniciar_competicion():
    visitante_a = Visitante()
    visitante_b = Visitante()

    laberinto.agregar_visitante_definido(visitante_a, 0, 0)
    laberinto.agregar_visitante_definido(
        visitante_b, laberinto.numero_casillas - 1, laberinto.numero_casillas - 1)

    laberinto.definir_objetivo_definido(
        int(laberinto.numero_casillas / 2), int(laberinto.numero_casillas / 2))

    hilos: list[Thread] = []

    def competir(visitante: Visitante):
        busqueda_a_estrella([visitante.casilla_actual], lambda casilla: goal_test(
            casilla, visitante), lambda casilla: expand(casilla, visitante), lambda casilla: evaluate(casilla, visitante))
        visitante.animar_recorrido()

    hilos.append(Thread(target=competir, args=(
        visitante_a,), daemon=True).start())
    hilos.append(Thread(target=competir, args=(
        visitante_b,), daemon=True).start())


laberinto.pack()
root.after(1000, iniciar_competicion)
root.mainloop()
