import os
import tkinter as tk
import numpy as np

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
        self.window = window
        self.reinas = []
        self.construir_campo()

    def construir_campo(self):
        size_campo = self.n_reinas * self.queensize
        self.campo = tk.Canvas(self.window, width=size_campo, height=size_campo )

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

    def add_reina(self, x: int, y: int):
        x1 = (x * self.queensize / 2) + self.queensize / 4
        x2 = x1 + self.queensize / 2

        y1 = (y * self.queensize / 2) + self.queensize / 4
        y2 = y1 + self.queensize / 2
        
        reina = self.campo.create_rectangle(x1, y1, x2, y2, fill='red')
        self.reinas.append(reina)
        self.window.update()

    def add_reinas(self, reinas: np.array) -> None:
        for i in range(reinas.size):
            x = i
            y = reinas[i]
            
            x1 = (x * self.queensize) + self.queensize / 4
            x2 = x1 + self.queensize / 2

            y1 = (y * self.queensize) + self.queensize / 4
            y2 = y1 + self.queensize / 2

            reina = self.campo.create_rectangle(x1, y1, x2, y2, fill='red')
            self.reinas.append(reina)
        self.window.update()

    def clear(self):
        for reina in self.reinas:
            self.campo.delete(reina)
        self.reinas = []
        self.window.update()

    def refresh(self):
        self.campo.update()

    def pack(self):
        self.campo.pack()
