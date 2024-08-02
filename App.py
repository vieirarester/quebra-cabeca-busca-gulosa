import Tabuleiro
import Heuristica

class App:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.heuristica = Heuristica()

    def executar(self):
        self.tabuleiro.exibir_tabuleiro()
        distancia = self.heuristica.distancia_manhattan(self.tabuleiro.tab)
        print(f"Distância de Manhattan: {distancia}")


app = App()
app.executar()