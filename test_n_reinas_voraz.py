import time
import tkinter
import numpy as np

from busquedas.busqueda_voraz import busqueda_voraz
from nreinas.expand_voraz import expand_voraz
from nreinas.checar_ataques import checar_ataques
from classes.chessboard import Chessboard

n_reinas = int(input('Introduzca el número de Reinas: '))

inicio = time.time()
frontera = np.zeros(n_reinas).tolist()


def evaluate(conf):
    return checar_ataques(conf)

def goal_test(estado_actual):
    numero_ataques = checar_ataques(estado_actual)
    print(numero_ataques)
    return not numero_ataques

ganador = busqueda_voraz([frontera], goal_test, expand_voraz, evaluate)

ex_time = time.time() - inicio
print('Tiempo de ejecución: %.2f' % ex_time)

root = tkinter.Tk()

chessboard = Chessboard(root, n_reinas)
chessboard.pack()

if ganador:
    chessboard.add_reinas(ganador)

root.mainloop()
