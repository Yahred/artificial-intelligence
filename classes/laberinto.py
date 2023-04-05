from tkinter import Canvas
from random import randint


class Visitante:

    def __init__(self, x: int, y: int, size: int) -> None:
        self.casilla_size = size
        self.r = size / 2
        self.canvas_id = None
        self.color = 'cyan'
        self.starting_x = x
        self.starting_y = y
        self.current_x = x
        self.current_y = y

    def dibujar(self, canvas: Canvas):
        self.canvas_id and canvas.delete(self.canvas_id)

        offset = self.casilla_size / 4

        x1 = (self.current_x * self.casilla_size) + offset
        y1 = (self.current_y * self.casilla_size) + offset

        canvas.create_oval(
            x1, y1, x1 + self.r, y1 + self.r, fill=self.color)


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

    def marcar_recorrido(self, canvas:Canvas, size: int):
        self.recorrida = True
        self.dibujar(canvas, size)


class Laberinto:

    def __init__(self, porcentaje_obstaculos) -> None:
        self.casilla_size = 40
        self.numero_casillas = 20
        self.porcentaje_obstaculos = porcentaje_obstaculos
        self.canvas = Canvas(width=self.casilla_size * self.numero_casillas,
                             height=self.casilla_size * self.numero_casillas)

        self.casillas: list[list[Casilla]] = []
        self.construir_laberinto()
        self.asignar_bloqueos()
        self.visitante = None
        self.definir_objetivo()
        self.definir_visitante()
        self.ruta = []

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

            break

    def definir_visitante(self):
        if self.bloqueos_existentes >= self.numero_casillas * self.numero_casillas:
            return

        while True:
            random_x = randint(0, self.numero_casillas - 1)
            random_y = randint(0, self.numero_casillas - 1)

            casilla = self.casillas[random_x][random_y]

            if casilla.bloqueada or casilla.es_objetivo:
                continue

            print(random_x, random_y)
            self.visitante = Visitante(random_x, random_y, self.casilla_size)
            self.visitante.dibujar(self.canvas)
            break


    def obtener_rangos_vecinos(self, punto: int):
        izq = punto - 1 if punto - 1 >= 0 else 0
        der = punto + 1 if punto + 1 < self.numero_casillas else self.numero_casillas - 1

        return izq, der

    def obtener_vecinos_casilla(self, x: int, y: int):
        rango_izq_x, rango_der_x = self.obtener_rangos_vecinos(x)
        rango_izq_y, rango_der_y = self.obtener_rangos_vecinos(y)

        vecinos: list[Casilla] = []
        for x in range(rango_izq_x, rango_der_x + 1):
            for y in range(rango_izq_y, rango_der_y + 1):
                casilla = self.casillas[x][y]

                if casilla.bloqueada:
                    continue

                vecinos.append(casilla)

        return vecinos
    
    def trazar_ruta(self, casilla: Casilla):
        self.ruta.append(casilla)
        for casilla in self.ruta:
            if casilla.recorrida:
                continue

            casilla.marcar_recorrido(self.canvas, self.casilla_size)