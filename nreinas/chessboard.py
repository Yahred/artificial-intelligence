import tkinter as tk
import os

absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
absolute_image_path = os.path.join(absolute_folder_path, 'assets/reina.gif')

class Queen:
    
    def __init__(self, x: int = None, y: int = None) -> None:
        self.x = x
        self.y = y

    def draw(self):
        img = tk.PhotoImage(file=absolute_image_path)
        return img

class Chessboard:

    def __init__(self, window: tk.Tk, n_reinas: int = 4, reinas: list[Queen] = []) -> None:
        self.n_reinas = n_reinas
        self.reinas = reinas
        self.queensize = 80
        self.construir_campo(window)

    def construir_campo(self, window: tk.Tk):
        self.campo = tk.Canvas(window, width=(self.n_reinas*self.queensize), height=(self.n_reinas*self.queensize))

        for i in range(self.n_reinas):
            fill_color_pattern = ['#b58863', '#f0d9b5'] if i % 2 == 0 else ['#f0d9b5', '#b58863']

            for j in range(self.n_reinas):
                x1 = i * self.queensize
                y1 = j * self.queensize
                x2 = x1 + self.queensize
                y2 = y1 + self.queensize
                color = fill_color_pattern[j % 2 == 0]
                self.campo.create_rectangle(x1, y1, x2, y2, fill=color)
        img = tk.PhotoImage(file=absolute_image_path)
        self.campo.create_image(100, 100, {'image': img})    

    def add_reina(self):
        img = tk.PhotoImage('reina.png')
        self.campo.create_image(0, 50, {'image': img})

    def refresh(self):
        self.campo.update()

    def pack(self):
        self.campo.pack()
