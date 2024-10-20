###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - O Caso do Medalhão Roubado 
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

# Leitura da entrada
N = int(input())

museu = []
for _ in range(N):
    museu.append(list(input()))

M = int(input())
suspeitos = {}
for _ in range(M):
    letra, pistas = input().split()
    suspeitos[letra] = list(map(int,pistas.split(",")))

# Verificação da posição do detetive
# Coleta das pistas
encontrado = []
avaliar = True
while avaliar:
    detetive = []
    avaliar = False
    for i, lin in enumerate(museu):
        for j, a in enumerate(lin):
            if a == 'D':
                detetive.append([i, j])

    for coordenadas in detetive:
        i = coordenadas[0]
        j = coordenadas[1]
        u = [i-1, j]
        d = [i+1, j]
        l = [i, j+1]
        r = [i, j-1]
    
        for a, b in zip([u[0], d[0], l[0], r[0]], [u[1], d[1], l[1], r[1]]):
            try:
                if museu[a][b] == '.' or museu[a][b].isnumeric():
                    if museu[a][b].isnumeric():
                        encontrado.append(museu[a][b])
                    avaliar = True
                    museu[a][b] = 'D'
            except:
                pass

encontrado = list(map(int, encontrado))

# Verificação dos suspeitos e impressão da saída
valores = []
output = []

for key in suspeitos:
    contador = 0
    for a in encontrado:
        if a in suspeitos[key]:
            contador += 1
    suspeitos[key] = contador
    valores.append(contador)
maximo = max(valores)
 
for key in suspeitos:
    if suspeitos[key] == maximo:
        output.append(key)

print(' '.join(output))

