# Função para simular a caminhada em uma direção a partir da cabana
def simular_direcao(mapa, inicio_x, inicio_y, direcao):
    visitados = set()
    x, y = inicio_x, inicio_y
    
    while True:
        if (x, y) in visitados:
            return "andou em circulos."
        visitados.add((x, y))
        
        # Movendo na direção indicada
        if direcao == 'N' and y > 0:  # Norte
            y -= 1
        elif direcao == 'S' and y < len(mapa) - 1:  # Sul
            y += 1
        elif direcao == 'L' and x < len(mapa[0]) - 1:  # Leste
            x += 1
        elif direcao == 'O' and x > 0:  # Oeste
            x -= 1
        else:
            return "caminho sem saida."
        
        if mapa[y][x] == 'F':
            return "encontrou o fim da floresta."
        elif mapa[y][x] == 'C':
            return "de volta a cabana."
        
        # Pegando a próxima direção do mapa
        direcao = mapa[y][x]

# # Leitura do mapa
# x, y = map(int, input().split())
# mapa = [input().split() for _ in range(x)]

# # Encontrar a posição inicial da cabana (C)
# for i in range(x):
#     for j in range(y):
#         if mapa[i][j] == 'C':
#             cabana_x, cabana_y = j, i
#             break

# Verificar as 4 direções a partir da cabana
resultados = {
    'N': simular_direcao(mapa, cabana_x, cabana_y, 'N'),
    'S': simular_direcao(mapa, cabana_x, cabana_y, 'S'),
    'L': simular_direcao(mapa, cabana_x, cabana_y, 'L'),
    'O': simular_direcao(mapa, cabana_x, cabana_y, 'O')
}

# Exibir os resultados
for direcao, resultado in resultados.items():
    print(f"{direcao}: {resultado}")
