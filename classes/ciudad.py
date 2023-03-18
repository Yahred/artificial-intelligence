
class Ciudad:

    def __init__(self, nombre: str, distancia: int = None, hijos: list = []) -> None:
        self.nombre = nombre
        self.hijos = hijos
        self.distancia = distancia

    
    
