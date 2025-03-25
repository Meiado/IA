import tkinter as tk
from tkinter import messagebox, ttk
from puzzle import Puzzle
from buscas import busca_em_largura, a_star, best_first
from heuristicas import pecas_fora_do_lugar, distancia_manhattan

import time
import datetime
import os

os.makedirs("logs", exist_ok=True)

class PuzzleGUI:
    def __init__(self, master):
        self.master = master
        master.title('Resolução Puzzle 8 - Busca')

        self.puzzle = Puzzle()

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.botao_embaralhar = tk.Button(self.frame, text="Embaralhar", command=self.embaralhar)
        self.botao_embaralhar.grid(row=0, column=0)

        self.opcao_busca = ttk.Combobox(
            self.frame,
            values=[
                "BFS (Cega)",
                "A* (Peças fora)",
                "A* (Manhattan)",
                "Best-First (Peças fora)",
                "Best-First (Manhattan)"
            ]
        )
        self.opcao_busca.current(0)
        self.opcao_busca.grid(row=0, column=2)

        self.opcao_nivel = ttk.Combobox(self.frame, values=["1", "2"])
        self.opcao_nivel.current(0)
        self.opcao_nivel.grid(row=0, column=3)

        self.botao_resolver = tk.Button(self.frame, text="Resolver", command=self.resolver)
        self.botao_resolver.grid(row=0, column=4)

        self.estado_label = tk.Label(self.frame, text='Estado Inicial:', font=('Arial', 14))
        self.estado_label.grid(row=1, column=0, columnspan=5)

        self.texto_estado = tk.Text(self.frame, height=5, width=20, font=('Arial', 14))
        self.texto_estado.grid(row=2, column=0, columnspan=5)

        self.opcao_busca.bind("<<ComboboxSelected>>", self.atualizar_interface)
        self.atualizar_interface()

        self.embaralhar()

    def mostrar_estado(self, estado):
        self.texto_estado.delete('1.0', tk.END)
        for linha in estado:
            self.texto_estado.insert(tk.END, ' '.join(str(n) if n != 0 else ' ' for n in linha) + '\n')

    def mostrar_solucao(self, caminho):
        for estado in caminho:
            self.mostrar_estado(estado)
            self.master.update()
            time.sleep(0.5)

    def embaralhar(self):
        self.puzzle.estado_inicial = self.puzzle.gerar_embaralhado()
        self.mostrar_estado(self.puzzle.estado_inicial)

    def resolver(self):
        if not self.estado_soluvel(self.puzzle.estado_inicial):
            messagebox.showerror("Insolúvel", "Este puzzle não tem solução!")
            return

        busca = self.opcao_busca.get()
        nivel = None
        if busca not in ["BFS (Cega)"]:
            nivel = int(self.opcao_nivel.get())

        inicio = time.time()

        if busca == "BFS (Cega)":
            caminho = busca_em_largura(self.puzzle.estado_inicial, self.puzzle.estado_final)
        elif busca == "A* (Peças fora)":
            caminho = a_star(self.puzzle.estado_inicial, self.puzzle.estado_final, pecas_fora_do_lugar, nivel)
        elif busca == "A* (Manhattan)":
            caminho = a_star(self.puzzle.estado_inicial, self.puzzle.estado_final, distancia_manhattan, nivel)
        elif busca == "Best-First (Peças fora)":
            caminho = best_first(self.puzzle.estado_inicial, self.puzzle.estado_final, pecas_fora_do_lugar, nivel)
        elif busca == "Best-First (Manhattan)":
            caminho = best_first(self.puzzle.estado_inicial, self.puzzle.estado_final, distancia_manhattan, nivel)

        fim = time.time()

        if caminho:
            self.mostrar_solucao(caminho)
            tempo_execucao = (fim - inicio) * 1000
            movimentos = len(caminho) - 1

            # log
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            with open(f"logs/log_busca_{timestamp}.log", "w") as f:
                f.write(f"Busca: {busca}\n")
                if nivel != None:
                    f.write(f"Heurística nível: {nivel}\n")
                f.write(f"Tempo de execução: {tempo_execucao:.4f} ms\n")
                f.write(f"Movimentos até a solução: {movimentos}\n")
                f.write("\nPassos da solução:\n")
                for estado in caminho:
                    for linha in estado:
                        f.write(" ".join(str(n) if n != 0 else " " for n in linha) + "\n")
                    f.write("\n")

            messagebox.showinfo("Sucesso", f"Solução encontrada em {movimentos} movimentos.\nTempo: {tempo_execucao:.2f} ms.")
        else:
            messagebox.showerror("Falha", "Nenhuma solução encontrada!")

    def estado_soluvel(self, estado):
        plano = [num for linha in estado for num in linha if num != 0]
        inversoes = 0
        for i in range(len(plano)):
            for j in range(i + 1, len(plano)):
                if plano[i] > plano[j]:
                    inversoes += 1
        return inversoes % 2 == 0
    
    def atualizar_interface(self, event=None):
        if self.opcao_busca.get() == "BFS (Cega)":
            self.opcao_nivel.config(state='disabled')
        else:
            self.opcao_nivel.config(state='readonly')


if __name__ == '__main__':
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()
