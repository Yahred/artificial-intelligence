import tkinter as tk

from classes.chessboard import Chessboard
from nreinas.checar_ataques import checar_ataques
from busquedas.busqueda_ancho import busqueda_ancho
from busquedas.busqueda_profundo import busqueda_profundo
from nreinas.expand import expand

n_reinas = int(input('Introduzca el número de reinas: '))

window = tk.Tk()
chessboard = Chessboard(window, n_reinas)
chessboard.pack()

def execute():
    busqueda_profundo([[0,0,0,0]], lambda configuracion: checar_ataques(configuracion, chessboard) == 0, expand)

window.after(1000, execute)
window.mainloop()




