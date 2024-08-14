###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Escolhendo seu Cartão de Crédito
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

# Leitura da entrada

# ANUIDADE
x = float(input('Valor da anuidade: R$ '))
# BENEFÍCIOS MENSAIS
y = float(input('Valor dos benefícios mensais: R$ '))
# CASHBACK
z = float(input('Taxa de cashback, em porcentagem (0 a 100): '))
# GASTO MENSAL
k = float(input('Valor médio dos gastos mensais: R$ '))

# Cálculos e impressão da saída

# Gasto anual com o cartão antigo:
card1 = 12*k

# Gasto anual com o cartão com anuidade:
card2 = 12*((1 - (z/100))*k - y) + x

if card1 > card2:
    print(False)
else:
    print(True)