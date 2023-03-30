import tkinter as tk
import random

n_cuadros = int(input('Introduzca el tamaño del laberinto: '))
obsta_percent = int(input('Introduzca el porcentaje de obstaculos: '))

class Grid(tk.Frame):
    
    def __init__(self, parent, rows, columns, size):
        tk.Frame.__init__(self, parent)

        self.grid_cells = []
        self.obstacles = set()

        for row in range(rows):
            grid_row = []
            for col in range(columns):
                grid_cell = tk.Canvas(self, width=size, height=size, highlightthickness=0, bg="black")
                grid_cell.grid(row=row, column=col, padx=1, pady=1)
                grid_row.append(grid_cell)
            self.grid_cells.append(grid_row)

        self.grid_cells[0][0].create_oval(size/4, size/4, size/4*3, size/4*3, fill="yellow")
        self.add_random_obstacles()
        self.draw_obstacles()

        self.pack()

    def add_random_obstacles(self):
        self.num_obstaculos = int((n_cuadros*n_cuadros)*(obsta_percent/100))
        for i in range(self.num_obstaculos):
            x = random.randint(0, len(self.grid_cells) - 1)
            y = random.randint(0, len(self.grid_cells[0]) - 1)
            if (x, y) not in self.obstacles and (x, y) != (0, 0):
                self.obstacles.add((x, y))

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            x, y = obstacle
            self.grid_cells[x][y].create_rectangle(0, 0, n_cuadros, n_cuadros, fill="red")

root = tk.Tk()
root.title("Laberinto")


grid = Grid(root, rows=n_cuadros, columns=n_cuadros, size=(600/n_cuadros))

root.mainloop()