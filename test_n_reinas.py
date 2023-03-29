import time
import tkinter as tk
import numpy as np
import sys

from classes.chessboard import Chessboard
from nreinas.checar_ataques import checar_ataques
from busquedas.busqueda_ancho import busqueda_ancho
from busquedas.busqueda_profundo import busqueda_profundo
from nreinas.expand import Expand

n_reinas = int(input('Introduzca el número de reinas: '))

window = tk.Tk()
window.title('N-Reinas ')
ex_time = 0


def execute(busqueda: callable):
    chessboard.clear()
    Expand.restart()

    inicio = time.time()
    frontera = np.zeros(n_reinas).tolist()

    busqueda([frontera], lambda estado_actual: not checar_ataques(
        estado_actual, chessboard), Expand.expand)

    ex_time = time.time() - inicio
    txt_tiempo['text'] = 'Tiempo de ejecución: %.2f' % ex_time


txt_tiempo = tk.Label(text='Tiempo de ejecución: %.2f' % ex_time)
txt_tiempo.pack()

boton = tk.Button(text='Búsqueda a lo profundo',
                  command=lambda: execute(busqueda_profundo))
boton.pack()

boton = tk.Button(text='Búsqueda a lo ancho',
                  command=lambda: execute(busqueda_ancho))
boton.pack()

chessboard = Chessboard(window, n_reinas)
chessboard.pack()
sys.setrecursionlimit(2000000)

window.mainloop()
