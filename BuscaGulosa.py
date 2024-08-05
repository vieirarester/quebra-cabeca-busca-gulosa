import time
from Tabuleiro import Tabuleiro

class BuscaGulosa:

    def __init__(self):
        self.visitados = set()

    def escolher_melhor_movimento(self, tabuleiro):
        if not tabuleiro.movimentos_possiveis:
            return 
        
        melhor_tabuleiro = tabuleiro.movimentos_possiveis[0]
        menor_custo = float('inf')

        for tabuleiro_possivel in tabuleiro.movimentos_possiveis:
            if tabuleiro_possivel.estado_unico() not in self.visitados:
                custo = tabuleiro_possivel.get_custo()
                if custo < menor_custo:
                    menor_custo = custo
                    melhor_tabuleiro = tabuleiro_possivel
      
        if melhor_tabuleiro:
            melhor_tabuleiro.movimento_realizado = True
            print("-----------------------------------")
            print("A melhor opção é:")
            melhor_tabuleiro.exibir_tabuleiro()

        return melhor_tabuleiro
    
    def exibir_jogadas(self):
        print(f"TOTAL DE JOGADAS = {len(self.visitados) - 1}")
        print("\nJOGADAS REALIZADAS:")
    
        for tabuleiro_visitado in self.visitados:
            tab = [list(tabuleiro_visitado[i:i + 3]) for i in range(0, 9, 3)]

            for linha in tab:
                print(" ".join(str(n) for n in linha))            
    
    def buscar(self, tabuleiro):
        
        estado_atual = tabuleiro.estado_unico()
        if estado_atual in self.visitados:
            print("\nNÃO HÁ MAIS MOVIMENTOS ÚNICOS!")
            print("Encerrando execução...")
            time.sleep(3)
            return
        self.visitados.add(estado_atual)

        tabuleiro.movimento_realizado = True
        print("* ESTADO ATUAL DO TABULEIRO *\n")
        tabuleiro.exibir_tabuleiro()

        if tabuleiro.verificar_objetivo():
            print("Tabuleiro objetivo encontrado!")
            self.exibir_jogadas()
            return
        
        print("\nOs tabuleiros possíveis são: \n")
        tabuleiro.imprimir_movimentos_possiveis()
        melhor_tabuleiro = self.escolher_melhor_movimento(tabuleiro)
        print('-----------------------------------')
        
        if melhor_tabuleiro:
            self.buscar(melhor_tabuleiro)
        else:
            print("Não foi possível resolver o tabuleiro.")


tabuleiro = Tabuleiro()
busca = BuscaGulosa()

busca.buscar(tabuleiro)