import copy
import random

class Puzzle:
    def __init__(self, estado_final=None):
        self.estado_final = estado_final or [[1,2,3],[4,5,6],[7,8,0]]
        self.estado_inicial = self.gerar_embaralhado()

    def gerar_embaralhado(self, movimentos=50):
        estado = copy.deepcopy(self.estado_final)
        vazio = [(ix, iy) for ix, row in enumerate(estado) for iy, i in enumerate(row) if i == 0][0]

        direcoes = [(0,1), (1,0), (-1,0), (0,-1)]

        for _ in range(movimentos):
            possibilidades = [
                (vazio[0]+dx, vazio[1]+dy)
                for dx, dy in direcoes
                if 0 <= vazio[0]+dx <= 2 and 0 <= vazio[1]+dy <= 2
            ]
            nova_pos = random.choice(possibilidades)
            estado[vazio[0]][vazio[1]], estado[nova_pos[0]][nova_pos[1]] = estado[nova_pos[0]][nova_pos[1]], estado[vazio[0]][vazio[1]]
            vazio = nova_pos

        return estado

    def exibir(self, estado):
        for linha in estado:
            print(' '.join(str(n) if n != 0 else ' ' for n in linha))
        print()

    def resolvido(self, estado):
        return estado == self.estado_final



if __name__ == '__main__':
    jogo = Puzzle()
    print('Estado Inicial (Embaralhado):')
    jogo.exibir(jogo.estado_inicial)

    print('Estado Final (Desejado):')
    jogo.exibir(jogo.estado_final)

    print('Resolvido?', jogo.resolvido(jogo.estado_inicial))
