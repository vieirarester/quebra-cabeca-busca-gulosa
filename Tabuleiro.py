import random

from Heuristica import Heuristica

class Tabuleiro:

    def __init__(self, tab=None):
        self.tab = tab if tab else self.gerar_tabuleiro_aleatorio()
        self.movimento_realizado = False
        self.custo = 0
        self.movimentos_possiveis = []
        self.heuristica = Heuristica()

    def estado_unico(self):
        return tuple(tuple(linha) for linha in self.tab)

    def gerar_tabuleiro_aleatorio(self):
        tab = list(range(1,9)) + [" "]
        random.shuffle(tab)

        return [tab[i:i + 3] for i in range(0, 9, 3)]
    
    def get_custo(self):
        self.custo = self.heuristica.distancia_manhattan(self)

        return self.custo

    def exibir_tabuleiro(self):
        for linha in self.tab:
            print(" ".join(str(n) for n in linha))
        
        print(f"CUSTO = {self.get_custo()}\n")

    def verificar_objetivo(self):
        tabuleiro_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, " "]]

        return self.tab == tabuleiro_objetivo
    
    def verificar_movimentos_possiveis(self):
        movimentos = []
        # encontra a posição do espaço vazio
        for i in range(3):
            for j in range(3):
                if self.tab[i][j] == " ":
                    linha_vazio, coluna_vazio = i, j
    
        # verifica movimentos possíveis
        if linha_vazio > 0: movimentos.append((linha_vazio - 1, coluna_vazio))  # movimento para cima
        if linha_vazio < 2: movimentos.append((linha_vazio + 1, coluna_vazio))  # movimento para baixo
        if coluna_vazio > 0: movimentos.append((linha_vazio, coluna_vazio - 1))  # movimento para a esquerda
        if coluna_vazio < 2: movimentos.append((linha_vazio, coluna_vazio + 1))  # movimento para a direita
    
        return movimentos

    def mover(self, movimento):
        
        linha_peca, coluna_peca = movimento
        linha_vazio, coluna_vazio = next(
            (i, j) for i in range(3) for j in range(3) if self.tab[i][j] == " ")

        if movimento in self.verificar_movimentos_possiveis():
        
            novo_tab = [linha[:] for linha in self.tab]  # faz uma cópia do tabuleiro
            novo_tab[linha_vazio][coluna_vazio], novo_tab[linha_peca][coluna_peca] = \
                novo_tab[linha_peca][coluna_peca], novo_tab[linha_vazio][coluna_vazio]
        
        return Tabuleiro(novo_tab)  # retorna um novo estado do tabuleiro

        return None
    
    def add_movimentos_possiveis(self):

        self.movimentos_possiveis = []

        for movimento in self.verificar_movimentos_possiveis():
            tabuleiro_possivel = self.mover(movimento)
            if tabuleiro_possivel:
                self.movimentos_possiveis.append(tabuleiro_possivel)
                

    def imprimir_movimentos_possiveis(self):

        self.add_movimentos_possiveis()
        for tabuleiro in self.movimentos_possiveis:
            tabuleiro.exibir_tabuleiro()

