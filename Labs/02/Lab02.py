###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Escolhendo seu Cartão de Crédito
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

# Leitura da entrada
x = float(input())
y = float(input())
z = float(input())
k = float(input())

# Cálculos e impressão da saída
card1 = 12*k
card2 = 12*((1 - (z/100))*k - y) + x
if card1 > card2:
    print(False)
else:
    print(True)