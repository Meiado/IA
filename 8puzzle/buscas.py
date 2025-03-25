from collections import deque
import heapq
import copy

from collections import deque

def busca_em_largura(estado_inicial, estado_final):
    fila = deque([(estado_inicial, [])])
    visitados = set()

    while fila:
        estado_atual, caminho = fila.popleft()
        if tuple(map(tuple, estado_atual)) in visitados:
            continue

        visitados.add(tuple(map(tuple, estado_atual)))

        if estado_atual == estado_final:
            return caminho + [estado_atual]

        for proximo_estado in gerar_sucessores(estado_atual):
            fila.append((proximo_estado, caminho + [estado_atual]))

    return None


def a_star(estado_inicial, estado_final, heuristica, nivel=1):
    visitados = set()
    fila = [(heuristica(estado_inicial, estado_final), estado_inicial, [])]

    while fila:
        _, estado_atual, caminho = heapq.heappop(fila)

        if tuple(map(tuple, estado_atual)) in visitados:
            continue

        visitados.add(tuple(map(tuple, estado_atual)))

        if estado_atual == estado_final:
            return caminho + [estado_atual]

        for proximo_estado in gerar_sucessores(estado_atual):
            if nivel == 2:
                sucessores_proximo = gerar_sucessores(proximo_estado)
                custo = len(caminho) + 1 + min([heuristica(s, estado_final) for s in sucessores_proximo])
            else:
                custo = len(caminho) + 1 + heuristica(proximo_estado, estado_final)

            heapq.heappush(fila, (custo, proximo_estado, caminho + [estado_atual]))

    return None

def best_first(estado_inicial, estado_final, heuristica, nivel=1):
    visitados = set()
    fila = [(heuristica(estado_inicial, estado_final), estado_inicial, [])]

    while fila:
        _, estado_atual, caminho = heapq.heappop(fila)

        if tuple(map(tuple, estado_atual)) in visitados:
            continue

        visitados.add(tuple(map(tuple, estado_atual)))

        if estado_atual == estado_final:
            return caminho + [estado_atual]

        for proximo_estado in gerar_sucessores(estado_atual):
            if nivel == 2:
                sucessores_proximo = gerar_sucessores(proximo_estado)
                custo = min([heuristica(s, estado_final) for s in sucessores_proximo])
            else:
                custo = heuristica(proximo_estado, estado_final)

            heapq.heappush(fila, (custo, proximo_estado, caminho + [estado_atual]))

    return None


def gerar_sucessores(estado):
    vazio = None
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                vazio = (i, j)
                break
        if vazio:
            break
    direcoes = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    sucessores = []
    for dx, dy in direcoes:
        nova_pos = (vazio[0] + dx, vazio[1] + dy)
        if 0 <= nova_pos[0] < 3 and 0 <= nova_pos[1] < 3:
            novo_estado = [linha.copy() for linha in estado]
            novo_estado[vazio[0]][vazio[1]], novo_estado[nova_pos[0]][nova_pos[1]] = novo_estado[nova_pos[0]][nova_pos[1]], novo_estado[vazio[0]][vazio[1]]
            sucessores.append(novo_estado)
    
    return sucessores
