###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Processamento de Dados
# Nome: Gian Gabriel SIlva Vianna
# RA: 278439
###################################################


# Leitura de dados
N = int(input())

d = {}
t = ('name', 'date', 'add', 'tel')

def paranomes(nome):
    l = []
    for palavra in nome.split():
        l.append(palavra.capitalize() if palavra.lower() not in ['de', 'da', 'das', 'do', 'dos'] else palavra.lower())
    return ' '.join(i for i in l)

for i in range(N):
    d = d.fromkeys(t)
    ltemp = []

    n = input()
    date = input()
    add = input()
    tel = input()

# Processamento de dados
    d['name'] = paranomes(n)



    if '/' in date:
        ltemp = date.split('/')
    elif '/' not in date and '-' not in date:
        ltemp = [date[0:2], date[2:4], date[4:]]
    if len(ltemp) != 0:
        date = '-'.join(i for i in ltemp)
    d['date'] = date

    ltemp = []

    if '-' in add:
        ltemp = add.split('-')
    else:
        ltemp = add.split(',')
    ltemp = [paranomes(ltemp[0]), ltemp[1]]
    add = ','.join(i for i in ltemp)
    d['add'] = add

    ltemp = []

    if '(' in tel and '-' not in tel:
        ltemp = [tel[1:3], tel[4:9], tel[9:]]
    elif '-' in tel and '(' not in tel:
        ltemp = [tel[0:2], tel[2:7], tel[8:]]
    elif '-' not in tel and '(' not in tel:
        ltemp = [tel[0:2], tel[2:7], tel[7:]]
    if len(ltemp) != 0:
        tel = f'({ltemp[0]}){ltemp[1]}-{ltemp[2]}'
    d['tel'] = tel

# Saída de dados
    for i in t:
        print(d[i])