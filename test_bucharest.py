import tkinter
import time

from busquedas.busqueda_voraz import busqueda_voraz
from busquedas.busqueda_a_estrella import busqueda_a_estrella
from classes.map import Map

from classes.bucharest import Ciudad, Camino

arad = Ciudad('Arad', 30, 100)
zerind = Ciudad('Zerind', 60, 50)
oradea = Ciudad('Oradea', 120, 20)
timisoara = Ciudad('Timisoara', 80, 250)
lugoj = Ciudad('Lugoj', 150, 300)
mehadia = Ciudad('Mehadia', 140, 400)
dobreta = Ciudad('Dobreta', 130, 500)
craiova = Ciudad('Craiova', 200, 520)
sibiu = Ciudad('Sibiu', 210, 200)
rimnicu_vilcea = Ciudad('Rimnicu Vilcea', 240, 250)
fagaras = Ciudad('Fagaras', 350, 210)
pitestu = Ciudad('Pitestu', 300, 420)
bucharest = Ciudad('Bucharest', 400, 500)
giurgiu = Ciudad('Giurgiu', 350, 550)
urziceni = Ciudad('Urziceni', 470, 450)
vaslui = Ciudad('Vaslui', 500, 250)
iasi = Ciudad('Iasi', 400, 150)
neamt = Ciudad('Neamt', 300, 60)
hirsova = Ciudad('Hirsova', 600, 440)
eforie = Ciudad('Eforie', 550, 550)

arad.hijos = [Camino(zerind, 75), Camino(timisoara, 118), Camino(sibiu, 140)]
zerind.hijos = [Camino(arad, 75), Camino(oradea, 71)]
oradea.hijos = [Camino(zerind, 71), Camino(sibiu, 151)]
timisoara.hijos = [Camino(arad, 118), Camino(lugoj, 111)]
lugoj.hijos = [Camino(timisoara, 111), Camino(mehadia, 70)]
mehadia.hijos = [Camino(lugoj, 70), Camino(dobreta, 75)]
dobreta.hijos = [Camino(mehadia, 75), Camino(craiova, 120)]
craiova.hijos = [Camino(dobreta, 120), Camino(
    rimnicu_vilcea, 146), Camino(pitestu, 138)]
rimnicu_vilcea.hijos = [Camino(craiova, 146), Camino(
    pitestu, 97), Camino(sibiu, 80)]
pitestu.hijos = [Camino(rimnicu_vilcea, 97), Camino(
    craiova, 138), Camino(bucharest, 101)]
sibiu.hijos = [Camino(arad, 140), Camino(fagaras, 99), Camino(rimnicu_vilcea, 80), Camino(oradea, 151)]
fagaras.hijos = [Camino(sibiu, 99), Camino(bucharest, 211)]
bucharest.hijos = [Camino(fagaras, 211), Camino(
    giurgiu, 90), Camino(pitestu, 101), Camino(urziceni, 85)]
giurgiu.hijos = [Camino(bucharest, 90)]
urziceni.hijos = [Camino(bucharest, 85), Camino(
    hirsova, 98), Camino(vaslui, 142)]
hirsova.hijos = [Camino(urziceni, 98), Camino(eforie, 86)]
eforie.hijos = [Camino(hirsova, 86)]
vaslui.hijos = [Camino(urziceni, 98), Camino(iasi, 92)]
iasi.hijos = [Camino(vaslui, 92), Camino(neamt, 87)]
neamt.hijos = [Camino(iasi, 87)]

distancias_bucharest = {}

with open('data/distancia_bucharest.txt') as f:
    lines = f.readlines()
    for line in lines:
        ciudad, distancia, *rest = line.split(',')
        distancias_bucharest[ciudad] = int(distancia)
 
estado_inicial = mehadia
path = []
objetivo = 'Bucharest'

def goal_test(estado_actual: Ciudad):
    path.append(estado_actual)
    return True if estado_actual.nombre == objetivo else False

lista_negra = []
def expand(estado_actual: Ciudad):      
    
    def sumar_distancia_acumulada(camino: Camino):
        camino.ciudad.distancia_acumulada += camino.distancia
        camino.ciudad.desde = estado_actual
        return camino.ciudad
    
    return [sumar_distancia_acumulada(camino) for camino in estado_actual.hijos if not camino.ciudad in lista_negra]

def evaluate(child: Ciudad):
    return distancias_bucharest[child.nombre] + child.distancia_acumulada

def after_evaluate(estado_actual: Ciudad, os: list[Ciudad]):
    if os:
        best_choice = os[0]
        if best_choice == estado_actual.desde:
            path.remove(estado_actual)
            lista_negra.append(estado_actual)

encontrado = busqueda_a_estrella([estado_inicial], goal_test, expand, evaluate, after_evaluate)

root = tkinter.Tk()
root.title('Viaje')
mapa_ventana = Map(estado_inicial)
mapa_ventana.canvas.pack()

def show_result():
    mapa_ventana.reveal_all()
    time.sleep(1)
    mapa_ventana.draw_path(path)

root.after(100, show_result) 
root.mainloop()
