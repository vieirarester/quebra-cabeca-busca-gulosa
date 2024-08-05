import time
from Tabuleiro import Tabuleiro

class BuscaGulosa:

    def __init__(self):
        # construtor que inicializa um conjunto para armazenar tabuleiros já jogados
        self.visitados = set()

    # escolhe o melhor movimento baseado no menor custo se é um novo movimento
    def escolher_melhor_movimento(self, tabuleiro):
        if not tabuleiro.movimentos_possiveis:
            return 
        
        melhor_tabuleiro = tabuleiro.movimentos_possiveis[0]
        menor_custo = float('inf') # mais infinito

        for tabuleiro_possivel in tabuleiro.movimentos_possiveis:
            if tabuleiro_possivel.estado_unico() not in self.visitados:

                # calcula o custo se o tabuleiro não foi jogado
                custo = tabuleiro_possivel.get_custo()

                # considera o menor custo
                if custo < menor_custo:
                    menor_custo = custo
                    melhor_tabuleiro = tabuleiro_possivel
      
        if melhor_tabuleiro:
            melhor_tabuleiro.movimento_realizado = True
            print("-----------------------------------")
            print("A melhor opção é:")
            melhor_tabuleiro.exibir_tabuleiro()

        return melhor_tabuleiro
                
    
    def buscar(self, tabuleiro):
        
        estado_atual = tabuleiro.estado_unico() # obtém o estado único do tabuleiro atual
        if estado_atual in self.visitados: # se o tabuleiro já foi jogado, encerra a execução
            print("\nNÃO HÁ MAIS MOVIMENTOS ÚNICOS!")
            print(f"TOTAL JOGADAS = {len(self.visitados)-1}")
            print("Encerrando execução...")
            time.sleep(1)
            return False
        
        self.visitados.add(estado_atual)

        tabuleiro.movimento_realizado = True
        print("* ESTADO ATUAL DO TABULEIRO *\n")
        tabuleiro.exibir_tabuleiro()

        # verifica se o tabuleiro atual é o tabuleiro objetivo
        if tabuleiro.verificar_objetivo():
            print("* VOCÊ ENCONTROU SEU OBJETIVO *")
            print(f"TOTAL JOGADAS = {len(self.visitados)-1}\n")
            return True
        
        print("\nOs tabuleiros possíveis são: \n")
        tabuleiro.imprimir_movimentos_possiveis()
        melhor_tabuleiro = self.escolher_melhor_movimento(tabuleiro)
        print('-----------------------------------')
        
        if melhor_tabuleiro:
            return self.buscar(melhor_tabuleiro)
        else:
            print("Não foi possível resolver o tabuleiro.")
            return False
