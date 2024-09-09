###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Lista de Compras
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

# Leitura de dados
D = float(input())
N = int(input())
pymarket = [float(item) for item in input().split()]
bytebazar = [float(item) for item in input().split()]
devshop = [float(item) for item in input().split()]

# Processamento dos dados
l_py = []
l_by = []
l_dev = []
p = 0
for n, i, j, k in zip(range(1, N+1), pymarket, bytebazar, devshop):

    if i <= j and i <= k and D-i >= 0:
        l_py.append(n)
        D = D-i

    elif j < i and j <= k and D-j >= 0:
        l_by.append(n)
        D = D-j
    
    elif k < i and k < j and D-k >= 0:
        l_dev.append(n)
        D = D-k
    else:
        p+=1
        continue
# Saída de dados
if len(l_py) != 0:
    print('Itens comprados no PyMarket:')
    print(" ".join(map(str,l_py)))
elif len(l_py) == 0:
    print('Nenhum item foi comprado no PyMarket')

if len(l_by) != 0:
    print('Itens comprados no ByteBazar:')
    print(' '.join(map(str,l_by)))
elif len(l_by) == 0:
    print('Nenhum item foi comprado no ByteBazar')

if len(l_dev) != 0:
    print('Itens comprados no DevShop:')
    print(' '.join(map(str, l_dev)))
elif len(l_dev) == 0:
    print('Nenhum item foi comprado no DevShop')

if p == 0:
    print('Foi possível terminar a receita')
elif p != 0:
    print('Não foi possível terminar a receita')