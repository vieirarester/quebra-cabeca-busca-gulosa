import random

class Tabuleiro:

    def __init__(self):
        self.tab = self.gerar_tabuleiro_aleatorio()

    def gerar_tabuleiro_aleatorio(self):
        tab = list(range(1,9)) + [" "]
        random.shuffle(tab)

        return [tab[i:i + 3] for i in range(0, 9, 3)]
        

    def exibir_tabuleiro(self):
        for linha in self.tab:
            print(" ".join(str(n) for n in linha))
        print()

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

            self.tab[linha_vazio][coluna_vazio], self.tab[linha_peca][coluna_peca] = \
                self.tab[linha_peca][coluna_peca], self.tab[linha_vazio][coluna_vazio]
            
            return self  # Retorna um novo estado do tabuleiro

        return None
