import time

from classes.chessboard import Chessboard

def checar_ataques(configuration: list[int], chessboard: Chessboard = None) -> int:
    chessboard.add_reinas(configuration)
    numero_ataques = 0
    n_reinas = len(configuration)

    for i in range(n_reinas):
        pos_a = configuration[i]

        for j in range(i+1, n_reinas):
            pos_b = configuration[j]

            if pos_a == pos_b:
                if chessboard:
                    chessboard.draw_attack([i, pos_a], [j, pos_b])
                numero_ataques += 2
                continue

            if abs(j - i) == abs(pos_a - pos_b):
                if chessboard:
                    chessboard.draw_attack([i, pos_a], [j, pos_b])
                numero_ataques += 2
    
    if(numero_ataques):
        chessboard.clear()
    
    return numero_ataques

if __name__ == '__main__':
    result = checar_ataques([0, 0, 0, 0])
    print(result)
