
class Ciudad:
    def __init__(self, nombre: str, x: int = None, y: int = None) -> None:
        self.nombre = nombre
        self.hijos = []
        self.x = x
        self.y = y
        self.desde = None
        self.distancia_acumulada = 0

class Camino: 
    def __init__(self, ciudad: Ciudad, distancia: int) -> None:
        self.ciudad = ciudad
        self.distancia = distancia

    
    
