from Tabuleiro import Tabuleiro
from Heuristica import Heuristica
from BuscaGulosa import BuscaGulosa

class App:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.heuristica = Heuristica()
        self.busca = BuscaGulosa(self.tabuleiro, self.heuristica)

    def executar(self):
        
        print("O tabuleiro inicial é: ")
        self.tabuleiro.exibir_tabuleiro()
        resultado = self.busca.buscar()

        if resultado:
            print("Solução encontrada!")
            for estado, movimento in resultado:
                estado.exibir_tabuleiro()
        


app = App()
app.executar()