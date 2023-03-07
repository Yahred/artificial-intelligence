import tkinter as tk
import numpy as np
import sys


from classes.chessboard import Chessboard
from nreinas.checar_ataques import checar_ataques
from busquedas.busqueda_ancho import busqueda_ancho
from busquedas.busqueda_profundo import busqueda_profundo
from nreinas.expand import expand

n_reinas = int(input('Introduzca el número de reinas: '))

window = tk.Tk()
window.title('N-Reinas')
chessboard = Chessboard(window, n_reinas)
chessboard.pack()
sys.setrecursionlimit(2000000) 


def execute():
    frontera = np.zeros(n_reinas).tolist()

    busqueda_profundo([frontera], lambda configuracion: checar_ataques(configuracion, chessboard) == 0, expand)

window.after(1000, execute)
window.mainloop()




