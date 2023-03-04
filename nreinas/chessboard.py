import tkinter as tk

class Queen:
    
    def __init__(self, x: int = None, y: int = None) -> None:
        self.x = x
        self.y = y

    def draw(self):
        img = tk.PhotoImage('assets/reina.png')
        return img

class Chessboard:

    def __init__(self, n_reinas: int = 4, reinas: list[Queen] = []) -> None:
        self.n_reinas = n_reinas
        self.reinas = reinas
        self.queensize = 80
        self.construir_campo()

    def construir_campo(self):
        self.campo = tk.Canvas(width=(self.n_reinas*self.queensize), height=(self.n_reinas*self.queensize))
    
        for i in range(self.n_reinas):
            fill_color_pattern = ['black', 'white'] if i % 2 == 0 else ['white', 'black']

            for j in range(self.n_reinas):
                x1 = i * self.queensize
                y1 = j * self.queensize
                x2 = x1 + self.queensize
                y2 = y1 + self.queensize
                color = fill_color_pattern[j % 2 == 0]
                self.campo.create_rectangle(x1, y1, x2, y2, fill=color)

    def add_reina(self, reina: Queen):
        self.reinas.append(reina)

    def refresh(self):
        self.campo.update()

    def pack(self):
        self.campo.pack()
