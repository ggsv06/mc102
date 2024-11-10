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
def caminho(mapa, i, j, E, G, M):

# . . .


# Leitura da entrada
N, E, G, M = [int(i) for i in input().split()]
i, j = [int(i) for i in input().split()]

mapa = []
for _ in range(N):
  mapa.append(input().split())

# Simulação do jogo


# Impressão da saída
