###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Kungsleden
# Nome: Gian Gabriel Silva Vianna
# RA: 23062009
###################################################

# Leitura de dados
l_input = [int(x) for x in input().split()]

y = l_input[0]
x = l_input[1]

mapa = []
for linha in range(0, y):
    mapa.append([x for x in input().split()])

# Processamento de dados
for i, linha in enumerate(mapa):
    for j, a in enumerate(linha):
        if a == 'C':
            xo = j
            yo = i
        elif a == 'F':
            xf = j
            yf = i

def avaliar(x, y, xf, yf, mapa, dir):
    caminho = []
    borda_x = len(mapa[0]) - 1
    borda_y = len(mapa) - 1
    while True:

        if dir == 'N' and y > 0:
            y = y-1
        elif dir == 'L' and x < borda_x:
            x = x+1
        elif dir == 'S' and y < borda_y:
            y = y+1
        elif dir == 'O' and x > 0:
            x = x - 1
        else:
            return 0
        
        if (x,y) in caminho:
            return 1
        else:
            caminho.append((x,y))

        if x == xf and y == yf:
            return 2
        
        linha = mapa[y]
        a = linha[x]
        if a == 'C':
            return 3
        dir = a

# Saída de dados
for dir in ['N', 'S', 'L', 'O']:
    resposta = avaliar(xo, yo, xf, yf, mapa, dir)
    if resposta == 0:
        msg = 'caminho sem saida.'
    elif resposta == 1:
        msg = 'andou em circulos.'
    elif resposta == 2:
        msg = 'encontrou o fim da floresta.'
    elif resposta == 3:
        msg = 'de volta a cabana.'
    print(f'{dir}: {msg}')