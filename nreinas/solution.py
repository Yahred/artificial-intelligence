def solve(configuration: list[int]) -> int:
    numero_ataques = 0
    n_reinas = len(configuration)

    for i in range(n_reinas):
        pos_a = configuration[i]

        for j in range(i+1, n_reinas):
            pos_b = configuration[j]

            if pos_a == pos_b:
                numero_ataques += 2
                continue

            if abs(j - i) == abs(pos_a - pos_b):
                numero_ataques += 2
    
    return numero_ataques

if __name__ == '__main__':
    result = solve([0, 0, 0, 0])
    print(result)
