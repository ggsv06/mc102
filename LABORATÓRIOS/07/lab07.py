###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Dependências de Tarefas I
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

# Leitura de dados
l_tarefas = [int(item) for item in input().split()]

# Verificação das dependências entre as tarefas
l_no = []

def rec(tarefas, i, temp):
    temp.append(i+1)
    j = tarefas[i]
    if j == i + 1:
        return True
    elif j not in temp:
        n = j
        return rec(tarefas, n-1, temp)
    elif j in temp:
        return False
    else:
        return 'ERRO'

for i in range(len(l_tarefas)):
    temp = []
    resultado = rec(l_tarefas, i, temp)
    if resultado == True:
        continue
    elif resultado == False:
        tarefas_possiveis = False
        break
else:
    tarefas_possiveis = True

# Impressão da saída
if tarefas_possiveis:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma das tarefas não pode ser realizada")