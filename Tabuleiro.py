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
    
    def mover(self, peca):

        # encontra a posição da peça a ser movido
        for i in range(3):
            for j in range(3):
                if self.tab[i][j] == peca:
                    linha_peca, coluna_peca = i, j
                    break
        
        # encontra a posição do espaço vazio
        for i in range(3):
            for j in range(3):
                if self.tab[i][j] == " ":
                    linha_vazio, coluna_vazio = i, j
                    break

        # troca as posições
        if abs(linha_peca - linha_vazio) + abs(coluna_peca - coluna_vazio) == 1:
            self.tab[linha_vazio][coluna_vazio], self.tab[linha_peca][coluna_peca] = \
                self.tab[linha_peca][coluna_peca], self.tab[linha_vazio][coluna_vazio]

            
tabuleiro = Tabuleiro()
print('tabuleiro original: ')
tabuleiro.exibir_tabuleiro()
print('tabuleiro com peça movida: ')
tabuleiro.mover(8)
tabuleiro.exibir_tabuleiro()