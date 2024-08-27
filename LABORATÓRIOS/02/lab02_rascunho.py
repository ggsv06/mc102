# Você está avaliando se deve manter seu cartão de crédito atual, que não possui anuidade, 
# ou fazer um upgrade para um novo cartão que oferece mais benefícios, porém cobra uma anuidade. 
# Para tomar essa decisão, você pode usar seu conhecimento em programação 
# para desenvolver um programa que ajude a calcular e comparar os gastos e benefícios dos dois cartões.
# Para o cartão atual, não há anuidade, mas para o novo cartão há uma anuidade fixa de R$ X, 
# mas você teria acesso a benefícios adicionais mensais de R$ Y e um cashback de Z% em todas as compras 
# (ou seja, Z% do valor de todas as compras será devolvido para você).
# Seu programa deve receber como entrada os valores de X, Y e Z, e o seu gasto mensal estimado K. 
# Com esses dados, o programa calculará o custo total da nova opção de cartão para os próximos 12 meses,
# levando em conta a anuidade, benefícios mensais e cashback, e determinará qual opção é mais vantajosa 
# (manter ou não o cartão atual).
# Como saída, seu programa deverá imprimir o valor booleano True se manter o cartão atual é mais 
# econômico ou False se fazer o upgrade para o novo cartão é a melhor escolha, 
# considerando o período considerado.


# ANUIDADE
x = float(input('Valor da anuidade: R$ '))
# BENEFÍCIOS MENSAIS
y = float(input('Valor dos benefícios mensais: R$ '))
# CASHBACK
z = float(input('Taxa de cashback, em porcentagem (0 a 100): '))
# GASTO MENSAL
k = float(input('Valor médio dos gastos mensais: R$ '))


# Gasto anual com o cartão antigo:
card1 = 12*k

# Gasto anual com o cartão com anuidade:
card2 = 12*((1 - (z/100))*k - y) + x

if card1 > card2:
    print(False)
else:
    print(True)