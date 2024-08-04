class Heuristica:
    
    def distancia_manhattan(self, tabuleiro):
        # Define a posição final de cada peça no tabuleiro
        posicoes_finais = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), " ": (2, 2)
        }
        distancia_total = 0
        valor = -1

        for i in range(3):
            for j in range(3):
                valor = tabuleiro.tab[i][j]
                if valor != " ":
                    pos_final = posicoes_finais[valor]
                    # Calcula a distância de Manhattan usando abs (módulo)
                    distancia = abs(i - pos_final[0]) + abs(j - pos_final[1])
                    distancia_total += distancia
        return distancia_total