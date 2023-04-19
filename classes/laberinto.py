import os
from tkinter import Canvas
from random import randint
from time import sleep
from PIL import ImageTk, Image

absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
absolute_image_path = os.path.join(absolute_folder_path, '../assets/raton.png')


class Casilla:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.bloqueada = False
        self.es_objetivo = False
        self.recorrida = False
        self.canvas_id = None

    def dibujar(self, canvas: Canvas, size: int):
        self.canvas_id and canvas.delete(self.canvas_id)

        x1 = self.x * size
        y1 = self.y * size

        fill_color = 'white'
        if self.bloqueada:
            fill_color = 'red'
        if self.es_objetivo:
            fill_color = 'gold'
        if self.recorrida:
            fill_color = 'green'

        self.canvas_id = canvas.create_rectangle(
            x1, y1, x1 + size, y1 + size, fill=fill_color, outline='black')

    def bloquear_casilla(self, canvas: Canvas, size: int):
        self.bloqueada = True
        self.dibujar(canvas, size)

    def hacer_objetivo(self, canvas: Canvas, size: int):
        self.es_objetivo = True
        self.dibujar(canvas, size)

    def marcar_recorrido(self, canvas: Canvas, size: int):
        self.recorrida = True
        self.dibujar(canvas, size)


class Visitante:

    def __init__(self, img=None) -> None:
        self.color = 'cyan'
        self.velocidad = 1
        self.canvas_id = None
        self.ruta: list[Casilla] = []
        self.casilla_inicial = None
        self.distancia_caminada = 0

    def definir_posicion_inicial(self, casilla: Casilla, canvas: Canvas, size: int, img=None):
        self.canvas = canvas
        self.casilla_inicial = casilla
        self.casilla_actual = casilla
        self.casilla_size = size
        self.offset = self.casilla_size / 4
        self.r = size / 2
        self.x = casilla.x
        self.y = casilla.y
        self.current_x = (self.x * self.casilla_size) + \
            (self.offset * bool(not img))
        self.current_y = (self.y * self.casilla_size) + \
            (self.offset * bool(not img))
        self.img = img

    def dibujar(self):
        self.canvas_id and self.canvas.delete(self.canvas_id)

        if self.img:
            self.canvas_id = self.canvas.create_image(
                self.current_x, self.current_y, image=self.img)
            return

        self.canvas_id = self.canvas.create_oval(
            self.current_x, self.current_y, self.current_x + self.r, self.current_y + self.r, fill=self.color)

    def caminar(self, x_objetivo: int, y_objetivo: int):
        x_objetivo_coord = (x_objetivo * self.casilla_size) + \
            self.offset 
        y_objetivo_coord = (y_objetivo * self.casilla_size) + \
            self.offset

        direccion_x = 1 if self.current_x < x_objetivo_coord else -1
        direccion_y = 1 if self.current_y < y_objetivo_coord else -1

        while self.current_x != x_objetivo_coord or self.current_y != y_objetivo_coord:
            if self.current_x != x_objetivo_coord:
                self.current_x = self.current_x + \
                    (self.velocidad * direccion_x)

            if self.current_y != y_objetivo_coord:
                self.current_y = self.current_y + \
                    (self.velocidad * direccion_y)

            self.dibujar()
            self.canvas.update()
            sleep(0.01)

    def agregar_ruta(self, casilla: Casilla):
        self.ruta.append(casilla)

    def animar_recorrido(self):
        for casilla in self.ruta:
            self.caminar(casilla.x, casilla.y)

    def limpiar_recorrido(self):
        self.casilla_actual = self.casilla_inicial
        self.ruta = []


class Laberinto:

    def __init__(self, porcentaje_obstaculos, casilla_size: int = 20, raton=False) -> None:
        self.casilla_size = casilla_size
        self.numero_casillas = 20
        self.porcentaje_obstaculos = porcentaje_obstaculos
        self.canvas = Canvas(width=self.casilla_size * self.numero_casillas,
                             height=self.casilla_size * self.numero_casillas)

        self.casillas: list[list[Casilla]] = []
        self.construir_laberinto()
        self.asignar_bloqueos()
        self.visitantes = []
        self.casilla_objetivo = None
        self.definir_objetivo()
        self.ruta: list[Casilla] = []
        self.raton = raton
        img = Image.open(absolute_image_path).resize(
            (self.casilla_size, self.casilla_size))
        self.img_raton = ImageTk.PhotoImage(img)

    def pack(self):
        self.canvas.pack()

    def construir_laberinto(self):
        fila_casillas = []

        for i in range(self.numero_casillas):
            if i > 0:
                self.casillas.append(fila_casillas)
                fila_casillas = []

            for j in range(self.numero_casillas):
                casilla = Casilla(i, j)
                casilla.dibujar(self.canvas, self.casilla_size)
                fila_casillas.append(casilla)

        self.casillas.append(fila_casillas)

    def asignar_bloqueos(self):
        bloqueos_totales = self.numero_casillas * \
            self.numero_casillas * self.porcentaje_obstaculos / 100
        self.bloqueos_existentes = 0

        while self.bloqueos_existentes < bloqueos_totales:
            random_x = randint(0, self.numero_casillas - 1)
            random_y = randint(0, self.numero_casillas - 1)

            if self.casillas[random_x][random_y].bloqueada:
                continue

            self.casillas[random_x][random_y].bloquear_casilla(
                self.canvas, self.casilla_size)
            self.bloqueos_existentes += 1

    def definir_objetivo(self):
        if self.bloqueos_existentes >= self.numero_casillas * self.numero_casillas:
            return

        while True:
            random_x = randint(0, self.numero_casillas - 1)
            random_y = randint(0, self.numero_casillas - 1)

            if self.casillas[random_x][random_y].bloqueada:
                continue

            self.casillas[random_x][random_y].hacer_objetivo(
                self.canvas, self.casilla_size)

            self.casilla_objetivo = self.casillas[random_x][random_y]

            break

    def agregar_visitante(self, visitante: Visitante):
        if self.bloqueos_existentes >= self.numero_casillas * self.numero_casillas:
            return

        while True:
            random_x = randint(0, self.numero_casillas - 1)
            random_y = randint(0, self.numero_casillas - 1)

            casilla = self.casillas[random_x][random_y]

            if casilla.bloqueada or casilla.es_objetivo:
                continue

            visitante.definir_posicion_inicial(
                casilla, self.canvas, self.casilla_size, self.img_raton if self.raton else None)
            visitante.dibujar()
            self.visitantes.append(visitante)
            return

    def obtener_vecinos_casilla(self, x: int, y: int):
        vecinos = []

        x - 1 >= 0 and not self.casillas[x -
                                         1][y].bloqueada and vecinos.append(self.casillas[x-1][y])
        y - 1 >= 0 and not self.casillas[x][y -
                                            1].bloqueada and vecinos.append(self.casillas[x][y-1])
        x + 1 < self.numero_casillas and not self.casillas[x +
                                                           1][y].bloqueada and vecinos.append(self.casillas[x+1][y])
        y + 1 < self.numero_casillas and not self.casillas[x][y +
                                                              1].bloqueada and vecinos.append(self.casillas[x][y+1])

        return vecinos
