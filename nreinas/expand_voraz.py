
def checar_ataques(configuration: list[int], chessboard=None) -> int:
    numero_ataques = 0
    n_reinas = len(configuration)

    for i in range(n_reinas):
        pos_a = configuration[i]

        for j in range(i+1, n_reinas):
            pos_b = configuration[j]

            if pos_a == pos_b:
                chessboard and chessboard.draw_attack([i, pos_a], [j, pos_b])
                numero_ataques += 2
                continue

            if abs(j - i) == abs(pos_a - pos_b):
                chessboard and chessboard.draw_attack([i, pos_a], [j, pos_b])
                numero_ataques += 2

    return numero_ataques


def expand_voraz(configuracion: list[int]) -> list[int]:
    os = []

    n_reinas = len(configuracion)
    for x in range(n_reinas):
        for y in range(n_reinas):
            configuracion_clon = configuracion.copy()

            if configuracion_clon[x] + (y + 1) < n_reinas:
                configuracion_clon[x] += y + 1
                os.append(configuracion_clon)

    return os


if __name__ == '__main__':
    os = expand_voraz([0, 0, 0, 0])

    print(len(os))
    print(os)
    
    print([checar_ataques(conf) for conf in os])

    os.sort(key=lambda conf: checar_ataques(conf))

    print(os)
