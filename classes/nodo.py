class Nodo: 
    def __init__(self, valor: any, nivel = 0, hijos: list = [],):
        self.valor = valor
        self.hijos = hijos
        self.nivel = nivel

    def __str__(self):
        return 'Valor %s' %(self.valor)
    