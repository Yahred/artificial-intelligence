class Nodo: 
    def __init__(self, valor: int, hijos: list = []):
        self.valor = valor
        self.hijos = hijos

    def __str__(self):
        return 'Valor %s, Hijos: %s' %(self.valor, [hijo.valor for hijo in self.hijos])
    