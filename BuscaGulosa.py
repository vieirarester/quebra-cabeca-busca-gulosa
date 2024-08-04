import heapq

class BuscaGulosa:
    def __init__(self, tabuleiro, heuristica):
        self.tabuleiro_inicial = tabuleiro
        self.heuristica = heuristica

    def buscar(self):
        tabuleiro_atual = self.tabuleiro_inicial
        custo_atual = self.heuristica.distancia_manhattan(tabuleiro_atual)
        print(f"CUSTO: {custo_atual}")

        fila_prioridade = []
        caminho = []
        visitados = set()

        heapq.heappush(fila_prioridade, (custo_atual, tabuleiro_atual, caminho))

        while fila_prioridade:
            # Imprime a fila de prioridade
            # print("Fila de prioridade:")
            # for item in fila_prioridade:
                #print(item)

            print(f"O tamanho da fila_prioridade é: {len(fila_prioridade)}")

            custo_atual, tabuleiro_atual, caminho = heapq.heappop(fila_prioridade)

            if tabuleiro_atual.verificar_objetivo():
                print("Tabuleiro resolvido!")

                for tabuleiro, movimento in caminho:
                    tabuleiro.exibir_tabuleiro()
                return caminho

            if str(tabuleiro_atual.tab) in visitados: continue

            visitados.add(str(tabuleiro_atual.tab))

            movimentos_possiveis = tabuleiro_atual.verificar_movimentos_possiveis()

            for movimento in movimentos_possiveis:             
                tabuleiro_possivel = tabuleiro_atual.mover(movimento)
                
                if tabuleiro_possivel:
                    custo = self.heuristica.distancia_manhattan(tabuleiro_possivel)
                    caminho_atualizado = caminho + [(tabuleiro_possivel, movimento)]
                    
                    # Adiciona o novo estado à fila de prioridade
                    heapq.heappush(fila_prioridade, (custo, tabuleiro_possivel, caminho_atualizado))
            
            # Imprime o movimento e o novo estado do tabuleiro apenas para o estado escolhido
            print(f"\nMovimento realizado: {caminho[-1][1] if caminho else 'Início'}")
            print("Estado atual do tabuleiro:")
            tabuleiro_atual.exibir_tabuleiro()
            print(f"Custo do estado: {custo}")

        print("Não foi possível resolver o tabuleiro.")
        return None