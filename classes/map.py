import tkinter
import time

from classes.bucharest import Ciudad, Camino


class Map:

    def __init__(self, mapa: Ciudad) -> tkinter.Canvas:
        self.width = 700
        self.height = 600
        self.canvas = tkinter.Canvas(width=self.width, height=self.height)
        self.r = 10
        self.animation_speed = 1
        self.dibujados = []
        self.path_revelado = []
        self.raiz = mapa
        self.map_drawed = []
        self.distancia_dibujada = []
        self.draw_map(mapa)

    def draw_map(self, mapa: Ciudad):
        if not mapa:
            return

        for camino in mapa.hijos:
            city = camino.ciudad

            if city in self.dibujados:
                continue

            x = city.x
            y = city.y

            if x is not None and y is not None:
                city_circle = self.canvas.create_oval(
                    x - self.r, y-self.r, x + self.r, y+self.r, fill='red')
                city_name = self.canvas.create_text(
                    x, y + 20, text=city.nombre, fill="black", font='Helvetica 12 bold')
                self.map_drawed.append(city_circle)
                self.map_drawed.append(city_name)

            self.dibujados.append(city)
            self.draw_map(city)

    def clear_map(self):
        for item in self.map_drawed:
            self.canvas.delete(item)
        self.dibujados = []

    def reveal_all(self):
        self.clear_map()
        self.reveal_all_path(self.raiz)
        self.draw_map(self.raiz)
        self.canvas.update()

    def reveal_all_path(self, ciudad_actual: Ciudad):
        if not ciudad_actual or ciudad_actual in self.path_revelado:
            return

        for camino in ciudad_actual.hijos:
            city = camino.ciudad

            if city in self.path_revelado:
                continue

            x1 = city.x
            y1 = city.y

            distancia = camino.distancia

            if x1 is not None and y1 is not None:
                offset = 15
                x = ciudad_actual.x
                y = ciudad_actual.y
                self.canvas.create_line(
                    x, y, x1, y1, fill='blue', width=2)
                self.canvas.create_text(
                    (x + (x1 - x)/2) - offset, (y + (y1 - y)/2) - offset, text=distancia)

            self.path_revelado.append(ciudad_actual)

        for hijo in ciudad_actual.hijos:
            self.reveal_all_path(hijo.ciudad)

    def draw_path(self, path: list[Ciudad]):
        x_ant = 0
        y_ant = 0

        for i in range(len(path)):
            city = path[i]
            x = city.x
            y = city.y

            if i > 0 and i < len(path):
                x_act = x_ant
                y_act = y_ant
                line_reference = None
                direction_x = 1
                direction_y = 1

                if x_act > x:
                    direction_x = -1

                if y_act > y:
                    direction_y = -1

                while abs(x_act - x) or abs(y_act - y):
                    if line_reference:
                        self.canvas.delete(line_reference)

                    line_reference = self.canvas.create_line(
                        x_ant, y_ant, x_act, y_act, fill='black', width=5)
                    if abs(x_act - x):
                        x_act += (self.animation_speed * direction_x)
                    if abs(y_act - y):
                        y_act += (self.animation_speed * direction_y)
                    self.canvas.update()
                    time.sleep(0.002)

            x_ant = x
            y_ant = y
