import time
import tkinter as tk
import numpy as np

from classes.chessboard import Chessboard
from nreinas.solution import solve

n_reinas = int(input('Introduzca el número de reinas: '))

window = tk.Tk()
chessboard = Chessboard(window, n_reinas)
chessboard.pack()

def execute():
    reinas_config = np.zeros(n_reinas, dtype=int)
    reinas_config[3] = 3    
    solve(reinas_config, chessboard)

window.after(1000, execute)
window.mainloop()




