###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Dependências de Tarefas II
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

"""
Função para detectar ciclos nas dependências das tarefas,
que deve ser implementada de forma recursiva.

Argumentos:
    - dependências: matriz com as dependências de cada tarefa
    - tarefa: tarefa sendo analisada
    - visitadas: lista de tarefas que já foram analisadas
Retorno:
    Essa função deve retornar True se não houver ciclos nas
    dependências da tarefa e False caso contrário.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
"""
def verifica_tarefas(dependencias, tarefa, visitadas):
    dtemp = {}
    for key in dependencias:
        ltemp = []
        for i in dependencias[key]:
            for ii in dependencias[i]:
                ltemp.append(ii)
        ltemp = list(dict.fromkeys(ltemp))
        ltemp.sort()
        dtemp[key] = ltemp
    if dtemp in visitadas:
        return False
    visitadas.append(dependencias)
    for key in dtemp:
        for i in dtemp[key]:
            if i != 0:
                return verifica_tarefas(dtemp, i, visitadas)
    return True

# . . .

# Leitura de dados
dependencias = {}
n = int(input())
dependencias[0] = [0]
for i in range(1, n+1):
    dependencias[i] = [int(x) for x in input().split()]

# Verificação das dependências entre as tarefas
visitadas = []
tarefas_possiveis = verifica_tarefas(dependencias, n, visitadas)

# Impressão da saída
if tarefas_possiveis:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma tarefa não pode ser realizada")

