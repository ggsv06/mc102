###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Jogos Olímpicos
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

# Leitura da quantidade de provas e pesos
N, O, P, B = [int(i) for i in input().split()]

# Leitura das provas
# Layout master:
# 0:prova/1:MF/2:1st/3:2nd/4:3th/5:ro
master = []
paises_temp = []
for _ in range(N):
    master.append([i for i in input().split(' - ')])
for l in master:
    paises_temp.extend([l[2], l[3], l[4]])
paises = list(set(paises_temp))

# Criação de quadro de medalhas
quadro = []
for pais in paises:
    ouros = 0
    pratas = 0
    bronzes = 0
    ro = 0
    mod_em_primeiro = []
    dobradinhas = 0
    for l in master:
        if pais == l[2]:
            ouros+=1
            if len(l) == 6:
                ro += 1
            mod_em_primeiro.append(l[0])
        if pais == l[3]:
            pratas+=1
        if pais == l[4]:
            bronzes+=1
    dobradinhas = len(mod_em_primeiro) - len(list(dict.fromkeys(mod_em_primeiro)))
    quadro.append((pais, ouros, pratas, bronzes, ro, dobradinhas))

# Ordenação pelo Critério Oficial
loff = sorted(quadro, key=lambda x: (-x[1], -x[2], -x[3], x[0]))

temp = []
for tupla in loff:
    temp.append(tupla[0])

stroff = ' - '.join(temp)
print('Critério Oficial:')
print(stroff)


# Ordenação Ponderado
pontuação = []
for tupla in quadro:
    pontuação.append((tupla[0], tupla[1]*O + tupla[2]*P + tupla[3]*B ))

lpon = sorted(pontuação, key=lambda x: (-x[1], x[0]))

temp = []
for tupla in lpon:
    temp.append(tupla[0])
    
strpon = ' - '.join(temp)
print('Ponderado:')
print(strpon)


# Ordenação por Recordes Olímpicos
lrec = sorted(quadro, key=lambda x: (-x[4], -x[1], -x[2], -x[3], x[0]))

temp = []
for tupla in lrec:
    temp.append(tupla[0])

strrec = ' - '.join(temp)
print('Recorde Olímpico:')
print(strrec)


# Ordenação por Dobradinha
ldob = sorted(quadro, key=lambda x: (-x[5], -x[1], -x[2], -x[3], x[0]))

temp = []
for tupla in ldob:
    temp.append(tupla[0])

strdob = ' - '.join(temp)
print('Dobradinha:')
print(strdob)
