from Tabuleiro import Tabuleiro
from BuscaGulosa import BuscaGulosa

class App:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.busca = BuscaGulosa(self.tabuleiro)

    def executar(self):
        
        print("O tabuleiro inicial é: ")
        self.tabuleiro.exibir_tabuleiro()
        resultado = self.busca.buscar(self.tabuleiro)        


app = App()
app.executar()