###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 09 - Álbum de Fotos
# Nome: Gian Gabriel SIlva Vianna
# RA: 278439
###################################################


# Leitura de dados
f = int(input())

d = {}
d = d.fromkeys([i for i in range(1, f+1)])

for i in range(1, f+1):
    d[i] = input().replace(f'foto {i}: ', '').strip().split(', ')
    if d[i] == [f'foto {i}:']:
        d.pop(i)

# Processamento de dados
lbruta = []
lbase = []
lqnt = []
lnomes_finais = []
lfotos = []

for item in d.keys():
    for nom in d.get(item):
        lbruta.append(nom)

for index, i in enumerate(lbruta):
    if i not in lbase:
        lbase.append(i)
        lqnt.append(lbruta.count(i))

for index, nom in enumerate(lbase):
    if lqnt[index] == max(lqnt):
        lnomes_finais.append(nom)

if len(lnomes_finais) > 1:
    ltemp = sorted(lnomes_finais)
    
    pessoa = ltemp[0]

else:
    pessoa = lnomes_finais[0]

for i in range(1, f+1):
    try:
        for nom in d.get(i):
            if nom == pessoa:
                lfotos.append(i)
    except:
        continue


fotos = ' '.join(map(lambda x: str(x), lfotos))
n = len(lbase)
# Saída de dados
print(f'No total, {n} pessoas apareceram nas fotos.')
print(f'{pessoa} foi a pessoa mais frequente, aparecendo na(s) foto(s): {fotos}')