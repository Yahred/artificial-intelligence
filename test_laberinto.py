import tkinter as tk
import random

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

        ##self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        


        self.pack()

    def add_random_obstacles(self):
        for i in range(50):
            x = random.randint(0, len(self.grid_cells) - 1)
            y = random.randint(0, len(self.grid_cells[0]) - 1)
            if (x, y) not in self.obstacles and (x, y) != (0, 0):
                self.obstacles.add((x, y))

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            x, y = obstacle
            self.grid_cells[x][y].create_rectangle(0, 0, 40, 20, fill="red")

root = tk.Tk()
root.title("Laberinto")

w = 800 # width for the Tk root
h = 800 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


grid = Grid(root, rows=30, columns=30, size=20)

root.mainloop()
