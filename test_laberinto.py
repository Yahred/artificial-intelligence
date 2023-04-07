import tkinter

from classes.laberinto import Casilla, Laberinto, Visitante
from busquedas.busqueda_profundo import busqueda_profundo
from busquedas.busqueda_voraz import busqueda_voraz

porcentaje_obstaculos = int(input('Introduzca el porcentaje de obstaculos: '))

root = tkinter.Tk()

root.title('Laberinto')

laberinto = Laberinto(porcentaje_obstaculos)

laberinto.pack()

recorridos = []


def expand(casilla: Casilla, visitante: Visitante):
    recorridos.append(casilla)
    visitante.agregar_ruta(casilla)

    return [casilla for casilla in laberinto.obtener_vecinos_casilla(casilla.x, casilla.y) if casilla not in visitante.ruta]


def goal_test(casilla: Casilla, visitante: Visitante):
    if casilla.es_objetivo:
        visitante.agregar_ruta(casilla)
        print('llegué')
        return True


def calcular_distancia_objetivo(casilla: Casilla, objetivo: Casilla):
    x1 = casilla.x
    y1 = casilla.y
    x2 = objetivo.x
    y2 = objetivo.y

    distancia = abs(x2 - x1) + abs(y2 - y1)
    return distancia


def evaluate(casilla: Casilla):
    return calcular_distancia_objetivo(casilla, laberinto.casilla_objetivo)

def ejecutar_recorrido():
    visitante1 = Visitante()
    visitante2 = Visitante()
    
    laberinto.agregar_visitante(visitante1)
    laberinto.agregar_visitante(visitante2)
    
    busqueda_voraz([visitante1.casilla_actual], lambda casilla: goal_test(casilla, visitante1), lambda casilla: expand(casilla, visitante1), evaluate)
    busqueda_voraz([visitante2.casilla_actual], lambda casilla: goal_test(casilla, visitante2), lambda casilla: expand(casilla, visitante2), evaluate)
    
    visitante1.animar_recorrido()
    visitante2.animar_recorrido()



root.after(100, ejecutar_recorrido)
root.mainloop()
