###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Tit for Tat
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

# Leitura da entrada
k = int(input())
c1 = [0]
c2 = []
p1 = 0
p2 = 0
# Processamento dos dados
c2.append(int(input()))
if c1[-1] == c2[-1] and c1[-1] == 0:
    p1+=3
    p2+=3
elif c1[-1] == c2[-1] and c1[-1] == 1:
    p1+=1
    p2+=1
elif c1[-1] > c2[-1]:
    p1+=5
else:
    p2+=5
for k in range(1, k):
    print(c1[-1])
    c1.append(c2[-1])
    c2.append(int(input()))
    if c1[-1] == c2[-1] and c1[-1] == 0:
        p1+=3
        p2+=3
    elif c1[-1] == c2[-1] and c1[-1] == 1:
        p1+=1
        p2+=1
    elif c1[-1] > c2[-1]:
        p1+=5
    else:
        p2+=5
# Saída de dados
print(c1[-1])
print(p1)
print(p2)
