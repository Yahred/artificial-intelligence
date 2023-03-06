import os
import time
import tkinter as tk
import numpy as np
from PIL import ImageTk

absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
absolute_image_path = os.path.join(absolute_folder_path, '../assets/reina.gif')

class Chessboard:
    def __init__(self, window: tk.Tk, n_reinas: int = 4) -> None:
        self.n_reinas = n_reinas
        self.queensize = 80
        self.img_reina = tk.PhotoImage(file=absolute_image_path)
        self.window = window
        self.reinas = []
        self.ataques = []
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

    def add_reina(self, x: int, y: int):
        x1 = (x * self.queensize / 2) + self.queensize / 4
        y1 = (y * self.queensize / 2) + self.queensize / 4
        
        reina = self.campo.create_image(x1, y1, {'image': self.img_reina})
        self.reinas.append(reina)
        self.window.update()

    def add_reinas(self, reinas: list[int]) -> None:
        for i in range(len(reinas)):
            x = i
            y = reinas[i]
            
            x1 = (x * self.queensize) + self.queensize / 2

            y1 = (y * self.queensize) + self.queensize / 2

            reina = self.campo.create_image(x1, y1, {'image': self.img_reina})
            self.window.update()
            self.reinas.append(reina)
            time.sleep(.1)

    def draw_attack(self, pos_a: tuple[int, int], pos_b: tuple[int, int]) -> None:
        x1, y1 = pos_a
        x2, y2 = pos_b

        x1 = x1 * self.queensize + self.queensize / 2
        y1 = y1 * self.queensize + self.queensize / 2
        x2 = x2 * self.queensize + self.queensize / 2
        y2 = y2 * self.queensize + self.queensize / 2

        ataque = self.campo.create_line(x1, y1, x2, y2, fill='red', width=15)
        self.ataques.append(ataque)
        self.window.update() 
        time.sleep(.1)       

    def clear(self):
        for reina in self.reinas:
            self.campo.delete(reina)
        
        for ataque in self.ataques:
            self.campo.delete(ataque)
        
        self.reinas = []
        self.window.update()

    def refresh(self):
        self.campo.update()

    def pack(self):
        self.campo.pack()
