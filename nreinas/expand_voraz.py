
visitados = []


def expand_voraz(configuracion: list[int]) -> list[int]:
    os = []
    n_reinas = len(configuracion)
    visitados.append(configuracion)

    for x in range(1, n_reinas):
        for y in range(n_reinas):
            configuracion_clon = configuracion.copy()
            movimiento = configuracion_clon[y] + x

            if movimiento < n_reinas:
                configuracion_clon[y] = movimiento
                configuracion_clon[y] not in visitados and os.append(
                    configuracion_clon)
                continue

            configuracion_clon[y] = movimiento - n_reinas
            configuracion_clon[y] not in visitados and os.append(
                configuracion_clon)

    return os


if __name__ == '__main__':
    os = expand_voraz([0, 3, 0, 0])
    print(os)
