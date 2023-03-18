class Expand: 
    visitados = []

    def restart():
        Expand.visitados = []

    def expand(configuracion: list[int]) -> list[int]:
        os = []

        n_reinas = len(configuracion)
        for x in range(len(configuracion)):
            configuracion_clon = configuracion.copy()
            if configuracion_clon[x] + 1 < n_reinas:
                configuracion_clon[x] += 1
                os.append(configuracion_clon)

        return os


if __name__ == '__main__':
    test = Expand.expand([0, 0, 0, 0])
    print(test)