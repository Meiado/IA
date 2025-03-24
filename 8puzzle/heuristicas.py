def pecas_fora_do_lugar(atual, final):
    return sum(atual[i][j] != final[i][j] and atual[i][j] != 0 for i in range(3) for j in range(3))


def distancia_manhattan(atual, final):
    distancia = 0
    for num in range(1,9):
        for i in range(3):
            for j in range(3):
                if atual[i][j] == num:
                    for x in range(3):
                        for y in range(3):
                            if final[x][y] == num:
                                distancia += abs(x - i) + abs(y - j)
    return distancia