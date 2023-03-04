import tkinter as tk
from nreinas.chessboard import Chessboard

window = tk.Tk()
chessboard = Chessboard(window)
chessboard.pack()

def add_queen():
    chessboard.add_reina()
    print('im not updating')
    window.update_idletasks()

window.after(2000, add_queen)
window.mainloop()




