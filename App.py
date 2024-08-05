import time
from Tabuleiro import Tabuleiro
from BuscaGulosa import BuscaGulosa

class App:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.busca = BuscaGulosa()

    def executar(self):
        
        while True:

            self.tabuleiro.exibir_tabuleiro()
            resultado = self.busca.buscar(self.tabuleiro)
            
            if resultado:
                break
            else:
                print("Gerando novo tabuleiro aleatório...")
                self.tabuleiro = Tabuleiro()
                self.busca = BuscaGulosa()
                time.sleep(2)  # delay de 2 segundos antes de tentar novamente        


app = App()
app.executar()