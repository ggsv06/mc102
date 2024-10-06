###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Kungsleden
# Nome: Gian Gabriel Silva Vianna
# RA: 23062009
###################################################


# Leitura de dados
l_input = [int(x) for x in input().split()]

x = l_input[0]
y = l_input[1]

mapa = []
for linha in range(0, y):
    mapa.append([x for x in input().split()])

# Processamento de dados
def avaliar(x,y):
    tupla = ((x, y-1),(x+1, y),(x, y+1),(x-1, y))
    output = []
    for direção, caso in enumerate(tupla):
        try:
            i = mapa[caso[1]]
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
            continue
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

# Saída de dados

