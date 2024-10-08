###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Kungsleden
# Nome: Gian Gabriel Silva Vianna
# RA: 23062009
###################################################

import copy
# Leitura de dados
l_input = [int(x) for x in input().split()]

x = l_input[0]
y = l_input[1]

mapa = []
for linha in range(0, y):
    mapa.append([x for x in input().split()])

# Processamento de dados
def avaliar(x,y,lmapa):
    tupla = [(x, y-1),(x+1, y),(x, y+1),(x-1, y)]
    output = []
    for direção, caso in enumerate(tupla): 
        try:
            i = lmapa[caso[1]]
            a = i[caso[0]]           
            if a == 'C':
                output.append('C')
                break
            elif a == 'F':
                continue
            else:
                if direção == 0 and a == 'S':
                    output.append((x, y-1))
                elif direção == 1 and a == 'O':
                    output.append((x+1, y))
                elif direção == 2 and a == 'N':
                    output.append((x,y+1)) 
                elif direção == 3 and a == 'L':
                    output.append((x-1,y))
        except:
            pass
    if 'C' in output:
        return ['C']
    else:
        return output

for i, linha in enumerate(mapa):
    for j, a in enumerate(linha):
        if a == 'C':
            xo = j
            yo = i
        elif a == 'F':
            xf = j
            yf = i

lsaidas = []
while True:
    mapa_temp = []
    mapa_temp[:] = mapa[:]
    lf = []
    for j, linha in enumerate(mapa):
        for i, a in enumerate(linha):
            if a == 'F':
                lf.append((i, j))
    
    for f in lf:
        i = f[0]
        j = f[1]

        for p in avaliar(i, j, mapa_temp):
            print(p)
            if p == 'C':
                lsaidas.append((i,j))
                continue
            else:
                mapa_avaliar = []
                mapa_avaliar[:] = mapa_temp[:]
                linha = mapa_temp[p[1]]
                linha.insert(p[0], 'F')
                del linha[p[0]+1]
                mapa_temp.insert(p[1], linha)
                del mapa_temp[p[1]+1]
                print(mapa_avaliar)
                print(mapa_temp)
                if mapa_avaliar == mapa_temp:
                    break
                continue

        else:
            continue
        break
    else:
        continue
    break
sem_saida1 = '-'
if 'N' in mapa[0]:
    while True:
        mapa_temp = []
        mapa_temp[:] = mapa[:]
        ln = []
        for j, a in enumerate(mapa[0]):
            if a == 'N':
                ln.append((i, j))     
        for f in ln:
            i = f[0]
            j = f[1]

            for p in avaliar(i, j, mapa_temp):
                
                if p == 'C':
                    sem_saida1 = (i,j)
                    break
                else:
                    linha = mapa_temp[p[1]]
                    linha.insert(p[0], 'F')
                    del linha[p[0]+1]
                    mapa_temp.insert(p[1], linha)
                    del mapa_temp[p[1]+1]
            else:
                continue
            break
        else:
            continue
        break
sem_saida2 = '-'
if 'S' in mapa[-1]:
    while True:
        mapa_temp = []
        mapa_temp[:] = mapa[:]
        ln = []
        for j, a in enumerate(mapa[-1]):
            if a == 'S':
                ln.append((i, j))     
        for f in ln:
            i = f[0]
            j = f[1]

            for p in avaliar(i, j, mapa_temp):
                
                if p == 'C':
                    sem_saida2 = (i,j)
                    break
                else:
                    linha = mapa_temp[p[1]]
                    linha.insert(p[0], 'F')
                    del linha[p[0]+1]
                    mapa_temp.insert(p[1], linha)
                    del mapa_temp[p[1]+1]
            else:
                continue
            break
        else:
            continue
        break
sem_saida3 = '-'


while True:
    mapa_temp = []
    mapa_temp[:] = mapa[:]
    lf = []
    for j, linha in enumerate(mapa):
        if linha[0] == 'O':
            lf.append((0, j))
            
    if len(lf) == 0:
        break
    
    for f in lf:
        i = f[0]
        j = f[1]
        
        for p in avaliar(i, j, mapa_temp):
            
            if p == 'C':
                sem_saida3 = (i,j)
                break
            else:
                linha = mapa_temp[p[1]]
                linha.insert(p[0], 'F')
                del linha[p[0]+1]
                mapa_temp.insert(p[1], linha)
                del mapa_temp[p[1]+1]
        else:
            continue
        break
    else:
        continue
    break
sem_saida4 = '-'
while True:
    mapa_temp = []
    mapa_temp[:] = mapa[:]
    lf = []
    for j, linha in enumerate(mapa):
        if linha[-1] == 'L':
            lf.append((len(linha)-1,j))
    if len(lf) == 0:
        break

    for f in lf:
        i = f[0]
        j = f[1]

        for p in avaliar(i, j, mapa_temp):
            
            if p == 'C':
                sem_saida4 = (i,j)
                break
            else:
                linha = mapa_temp[p[1]]
                linha.insert(p[0], 'F')
                del linha[p[0]+1]
                mapa_temp.insert(p[1], linha)
                del mapa_temp[p[1]+1]
        else:
            continue
        break
    else:
        continue
    break
print(lsaidas)
print(sem_saida1)
print(sem_saida2)
print(sem_saida3)
print(sem_saida4)

# Saída de dados

