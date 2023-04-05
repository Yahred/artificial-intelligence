import tkinter

from classes.laberinto import Casilla, Laberinto
from busquedas.busqueda_profundo import busqueda_profundo

porcentaje_obstaculos = int(input('Introduzca el porcentaje de obstaculos: '))

root = tkinter.Tk()

root.title('Laberinto')

laberinto = Laberinto(porcentaje_obstaculos)

laberinto.pack()

recorridos = []


def expand(casilla: Casilla):
    recorridos.append(casilla)
    laberinto.trazar_ruta(casilla)
    
    return [casilla for casilla in laberinto.obtener_vecinos_casilla(casilla.x, casilla.y) if casilla not in recorridos]


def goal_test(casilla: Casilla):
    if casilla.es_objetivo:
        print('Terminé')
        return True


def ejecutar_recorrido():
    estado_inicial = laberinto.casillas[laberinto.visitante.current_x][laberinto.visitante.current_y]

    busqueda_profundo([estado_inicial], goal_test, expand)


root.after(100, ejecutar_recorrido)
root.mainloop()
