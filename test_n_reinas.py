import time
import tkinter as tk
import numpy as np

from nreinas.chessboard import Chessboard

n_reinas = int(input('Introduzca el número de reinas: '))

window = tk.Tk()
chessboard = Chessboard(window, n_reinas)
chessboard.pack()

def execute():
    reinas_config = np.zeros(n_reinas, dtype=int)
    chessboard.add_reinas(reinas_config)
    chessboard.draw_attack([0, 0], [3,3])

    time.sleep(2)

window.after(1000, execute)
window.mainloop()




