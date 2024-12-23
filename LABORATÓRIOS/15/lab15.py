###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Labirinto de Creta
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

'''
Função para simular o caminho percorrido pelo Teseu, essa função deve ser implementada de forma recursiva. A função recebe a matriz representando o mapa, a posição (i,j) do Teseu, a energia E de Teseu, a energia G de um gigante e a energia M do Minotauro. A função deve retornar se Teseu conseguiu derrotar o Minotauro.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida implementada será considerada TENTATIVA DE FRAUDE.

'''
temp = []
# Leitura da entrada
N, E, G, M = [int(i) for i in input().split()]
i, j = [int(i) for i in input().split()]

mapa = []
for _ in range(N):
  mapa.append(input().split())

def caminho(mapa, i, j, E, G, M, lista):
    dire = []
    lista.append([i,j]) 
    if i < len(mapa)-1:
        d =[i+1,j]
        if d not in lista and mapa[d[0]][d[1]] != '#':
            dire.append(d)
    if i > 0:
        u = [i-1,j]
        if u not in lista and mapa[u[0]][u[1]] != '#':
            dire.append(u)

    if j < len(mapa[0])-1:
        r = [i,j+1]
        if r not in lista and mapa[r[0]][r[1]] != '#':
            dire.append(r)
    if j > 0:
        l = [i,j-1]
        if l not in lista and mapa[l[0]][l[1]] != '#':
            dire.append(l)
    for v in dire:
        if v != dire[0]:
            nlista = lista.copy()
            temp.append([ v,E,nlista ])

    if mapa[i][j] == 'M' and E > 0:
        return 'Teseu derrotou o Minotauro'

    if E <= 0 or len(dire) == 0:
        for s in temp:
            temp.remove(s)
            ni = s[0][0]
            nj = s[0][1]
            ne = s[1]
            nl = s[2]
            if mapa[ni][nj] == '.':
                return caminho(mapa, ni, nj, ne-1, G, M, nl)
            if mapa[ni][nj] == 'G':
                return caminho(mapa, ni, nj, ne-G, G, M, nl)
            if mapa[ni][nj] == 'M':
                return caminho(mapa, ni, nj, ne-M, G, M, nl)
        return 'Teseu não derrotou o Minotauro'

    for v in dire:
        ni = v[0]
        nj = v[1]
        if mapa[ni][nj] == '.':
            return caminho(mapa, ni, nj, E-1, G, M, lista)
        if mapa[ni][nj] == 'G':
            return caminho(mapa, ni, nj, E-G, G, M, lista)
        if mapa[ni][nj] == 'M':
            return caminho(mapa, ni, nj, E-M, G, M, lista)

# . . .
# Simulação do jogo
# Impressão da saída
lista = []
print(caminho(mapa, i, j, E, G, M, lista))
