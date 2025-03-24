from collections import deque
import heapq
import copy

def busca_em_largura(estado_inicial, estado_final):
    visitados = set()
    fila = deque([(estado_inicial, [])])

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
    heap = [(heuristica(estado_inicial, estado_final), estado_inicial, [])]

    while heap:
        _, estado_atual, caminho = heapq.heappop(heap)

        if tuple(map(tuple, estado_atual)) in visitados:
            continue

        visitados.add(tuple(map(tuple, estado_atual)))

        if estado_atual == estado_final:
            return caminho + [estado_atual]

        for proximo_estado in gerar_sucessores(estado_atual):
            custo = len(caminho) + 1

            if nivel == 2:
                sucessores_proximo = gerar_sucessores(proximo_estado)
                custo += min([heuristica(s, estado_final) for s in sucessores_proximo])
            else:
                custo += heuristica(proximo_estado, estado_final)

            heapq.heappush(heap, (custo, proximo_estado, caminho + [estado_atual]))

    return None


def best_first(estado_inicial, estado_final, heuristica, nivel=1):
    visitados = set()
    heap = [(heuristica(estado_inicial, estado_final), estado_inicial, [])]

    while heap:
        _, estado_atual, caminho = heapq.heappop(heap)

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

            heapq.heappush(heap, (custo, proximo_estado, caminho + [estado_atual]))

    return None


def gerar_sucessores(estado):
    direcoes = [(0,1), (1,0), (-1,0), (0,-1)]
    sucessores = []

    vazio = [(ix, iy) for ix, row in enumerate(estado) for iy, i in enumerate(row) if i == 0][0]

    for dx, dy in direcoes:
        nx, ny = vazio[0] + dx, vazio[1] + dy
        if 0 <= nx <= 2 and 0 <= ny <= 2:
            novo_estado = copy.deepcopy(estado)
            novo_estado[vazio[0]][vazio[1]], novo_estado[nx][ny] = novo_estado[nx][ny], novo_estado[vazio[0]][vazio[1]]
            sucessores.append(novo_estado)

    return sucessores