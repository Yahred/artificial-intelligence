import time
import tkinter
import numpy as np

from busquedas.busqueda_voraz import busqueda_voraz
from nreinas.expand_voraz import expand_voraz
from nreinas.checar_ataques import checar_ataques
from classes.chessboard import Chessboard

n_reinas = int(input('Introduzca el número de Reinas: '))


def execute():
    inicio = time.time()
    frontera = np.zeros(n_reinas).tolist()

    def evaluate(conf):
        return checar_ataques(conf)

    ganador = busqueda_voraz([frontera], lambda estado_actual: not checar_ataques(
        estado_actual), expand_voraz, evaluate)

    if ganador:
        chessboard.add_reinas(ganador)

    ex_time = time.time() - inicio
    print('Tiempo de ejecución: %.2f' % ex_time)


root = tkinter.Tk()

chessboard = Chessboard(root, n_reinas)
chessboard.pack()

root.after(1, execute)
root.mainloop()
