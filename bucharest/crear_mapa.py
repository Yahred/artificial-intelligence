

class Ciudad:
    def __init__(self, nombre: str, hijos: list = []) -> None:
        self.nombre = nombre
        self.hijos = hijos

class Camino: 
    def __init__(self, ciudad: Ciudad, distancia: int) -> None:
        self.ciudad = ciudad
        self.distancia = distancia

arad = Ciudad('Arad')
zerind = Ciudad('Zerind')
oradea = Ciudad('Oradea')
timisoara = Ciudad('Timisoara')
lugoj = Ciudad('Lugoj')
mehadia = Ciudad('Mehadia')
dobreta = Ciudad('Dobreta')
craiova = Ciudad('Craiova')
sibiu = Ciudad('Sibiu')
rimnicu_vilcea = Ciudad('Rimnicu Vilcea')
fagaras = Ciudad('Fagaras')
pitesti = Ciudad('Pitestu')
bucharest = Ciudad('Bucharest')
giurgiu = Ciudad('Giurgiu')
urziceni = Ciudad('Urziceni')
vaslui = Ciudad('Vaslui')
iasi = Ciudad('Iasi')
neamt = Ciudad('Neamt')
hirsova = Ciudad('Hirsova')
eforie = Ciudad('Eforie')

arad.hijos = [Camino(zerind, 75), Camino(timisoara, 118), Camino(sibiu, 140)]
zerind.hijos = [Camino(arad, 75), Camino(oradea, 71)]
oradea.hijos = [Camino(zerind, 71), Camino(sibiu, 151)]
timisoara.hijos = [Camino(arad, 118), Camino(lugoj, 111)]
lugoj.hijos = [Camino(timisoara, 111), Camino(mehadia, 70)]
mehadia.hijos = [Camino(lugoj, 70), Camino(dobreta, 75)]
dobreta.hijos = [Camino(mehadia, 75), Camino(craiova, 120)]
craiova.hijos = [Camino(dobreta, 120), Camino(rimnicu_vilcea, 146), Camino(pitesti, 138)]
rimnicu_vilcea.hijos = [Camino(craiova, 146), Camino(pitesti, 97), Camino(sibiu, 80)]
pitesti.hijos = [Camino(rimnicu_vilcea, 97), Camino(craiova, 138), Camino(bucharest, 101)]
sibiu.hijos = [Camino(arad, 140), Camino(fagaras, 99)]
fagaras.hijos = [Camino(sibiu, 99), Camino(bucharest, 211)]
bucharest.hijos = [Camino(fagaras, 211), Camino(giurgiu, 90), Camino(pitesti, 101), Camino(urziceni, 85)]
giurgiu.hijos = [Camino(bucharest, 90)]
urziceni.hijos = [Camino(bucharest, 85), Camino(hirsova, 98), Camino(vaslui, 142)]
hirsova.hijos = [Camino(urziceni, 98), Camino(eforie, 86)]
eforie.hijos = [Camino(hirsova, 86)]
vaslui.hijos = [Camino(urziceni, 98), Camino(iasi, 92)]
iasi.hijos = [Camino(vaslui, 92), Camino(neamt, 87)]
neamt.hijos = [Camino(iasi, 87)]

def Mapa(): 
    return arad

if __name__ == '__main__':
    ciudad_actual = arad

    while ciudad_actual.hijos:
        print(ciudad_actual.hijos)
        ciudad_actual = ciudad_actual.hijos[0].ciudad
