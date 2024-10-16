###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - No Man's Sky
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

PROTOTIPOS = ('PD', 'PA', 'PTR', 'PTE', 'PC', 'PR', 'PO', 'PV')
PROTOTIPOS = ' '.join(PROTOTIPOS)
PAISAGENS = ('SOA', 'SVM', 'SCO', 'SF1', 'SF2', 'SF3', 'SL', 'SPC')
CONDICOES_CLIMATICAS = ('CC0', 'CC1', 'CC2', 'CN1', 'CN2', 'CN3', 'CN4', 'CV', 'CTA1', 'CTA2', 'CTE1')

#TERRENO_PROTO = {
    #'PD':  ('TD', 'TA2'),
    #'PA':  ('TA1 TA2', 'TD TP TM'),
    #'PTR': ('TP TM', 'TAR TO1 TO2'),
    #'PTE': ('TP TM', 'TAR TO1 TO2 TC'),
    #'PC':  ('TC TM', 'TO1 TO2 TP'),
    #'PR':  ('TC TM', 'TO1 TO2'),
    #'PO':  ('TO1 TO2', 'TAR TM'),
    #'PV':  ('TM', 'TP TC')
#}

TERRENO_PROTO = {
    'PD':  'TD TA2',
    'PA':  'TA1 TA2 TD TP TM',
    'PTR': 'TP TM TAR TO1 TO2',
    'PTE': 'TP TM TAR TO1 TO2 TC',
    'PC':  'TC TM TO1 TO2 TP',
    'PR':  'TC TM TO1 TO2',
    'PO':  'TO1 TO2 TAR TM',
    'PV':  'TM TP TC'
}

d_terreno_proto = {}
for key in TERRENO_PROTO:
    d_terreno_proto[key] = TERRENO_PROTO[key].split()

TERRENO_ADJACENCIA = {
    'TAR': 'TAR TO1 TP TC TM',
    'TO1': 'TAR TO1 TO2 TM',
    'TO2': 'TO1 TO2',
    'TA1': 'TA1 TA2 TP TC TM',
    'TA2': 'TA1 TA2 TD TC TM',
    'TD': 'TA2 TD',
    'TP': 'TAR TA1 TA2 TP TC TM',
    'TC': 'TAR TA1 TA2 TP TC TM',
    'TM': 'TAR TO1 TA1 TA2 TP TC TM'
}
d_terreno_adja = {}
for key in TERRENO_ADJACENCIA:
    d_terreno_adja[key] = TERRENO_ADJACENCIA[key].split()


ELEMENTOS = {
    # Scenarios
    'SOA' : ('PA',               'TA1 TA2'),
    'SVM' : ('PTR PTE PR PO',    'TO1 TO2'),
    'SCO' : ('PTR PTE PR PO',    'TO1'),
    'SF1' : ('PTR PTE',          'TP TM'),
    'SF2' : ('PTR PTE',          'TP TM'),
    'SF3' : ('PA PTR PTE',       'TP TM'),
    'SL'  : ('PTR PTE',          'TP TM TC'),
    'SPC' : (PROTOTIPOS,         'TC TM'),
    # Weather conditions
    'CC0' : ('PTR PTE PC PR PO', 'TAR TO1 TO2 TP TC TM'),
    'CC1' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
    'CC2' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
    'CN1' : ('PTE PR PO',        'TAR TP TC TM'),
    'CN2' : ('PTE PC PR PO',     'TAR TP TC TM'),
    'CN3' : ('PTE PC',           'TAR TP TC TM'),
    'CN4' : ('PC',               'TAR TP TC TM'),
    'CV'  : ('PV',               'TP TC TM'),
    'CTA1': ('PD PA',            'TD'),
    'CTA2': ('PD PA PV',         'TD TA2 CV'),
    'CTE1': ('PR',               'TM TO1 TO2'),
    # Animals
    'AMA' : (PROTOTIPOS,         'TD TA2'),
    'AAV' : (PROTOTIPOS,         'TAR TP TA1 TC TM'),
    'AMM' : (PROTOTIPOS,         'TO1 TO2 TAR'),
    'APE' : (PROTOTIPOS,         'TO1 TO2 SL TAR'),
    'AAL' : (PROTOTIPOS,         'TAR TP SL TO1'),
    'ACR' : (PROTOTIPOS,         'TAR TO1'),
    'AHQ' : (PROTOTIPOS,         'TAR TA1 TP TM'),
    'ARO' : (PROTOTIPOS,         'TAR TA1 TA2 TD TC TM'),
    'AFE' : (PROTOTIPOS,         'TAR TA1 TP TC TM SF1'),
    'ACA1': (PROTOTIPOS,         'TP TC TM SF1'),
    'ACA2': (PROTOTIPOS,         'TP TC TM SF1'),
    'AHOT': (PROTOTIPOS,         'TP TC TM SF1 SF2 SF3')
}

# Leitura de dados
proto = input()
tamanho_matriz = [int(x) for x in input().split()]
matriz_terrenos = []
matriz_mobs = []
for i in range(tamanho_matriz[0]):
    linha = input().split()
    nw_line = []
    nwmb_line = []
    for j in linha:
        la = j.split(',')
        nw_line.append(la[0])
        la.pop(0)
        nwmb_line.append(la)
    matriz_terrenos.append(nw_line)
    matriz_mobs.append(nwmb_line)

# Processamento de dados

def adjacentes(i, j):
    if i < tamanho_matriz[0] - 1 and j < tamanho_matriz[1] - 1:
        if i > 0 and j > 0:
            adja = ((i+1, j), (i, j+1), (i-1, j), (i, j-1))
        elif i > 0 and j == 0:
            adja = ((i+1, j), (i, j+1), (i-1, j), (i, tamanho_matriz[1] - 1))
        elif i == 0 and j > 0:
            adja = ((i+1, j), (i, j+1), (tamanho_matriz[0] - 1, j), (i, j-1))
        else:
            adja = ((i+1, j), (i, j+1), (tamanho_matriz[0] - 1, j), (i, tamanho_matriz[1] - 1))
    else:
        if i == tamanho_matriz[0] - 1 and j < tamanho_matriz[1] - 1:
            adja = ((i-1, j), (i, j+1), (i, j-1), (0, j))
        elif i < tamanho_matriz[0] - 1 and j == tamanho_matriz[1] - 1:
            adja = ((i-1, j), (i, 0), (i, j-1), (i+1, j))
        elif i == tamanho_matriz[0] - 1 and j == 0:
            adja = ((0, j), (i, j+1), (i-1,j), (i, tamanho_matriz[1]-1))
        elif i == tamanho_matriz[0] - 1 and j == tamanho_matriz[1] - 1:
            adja = ((0, j), (i, 0), (i-1,j), (i, j-1))
        else:
            adja = ((i+1, j), (i, j-1), (tamanho_matriz[0]-1, j), (i, 0))
        
    output = []
    for a in adja:
        i = a[0]
        j = a[1]
        output.append(matriz_terrenos[i][j])
    return output        


regra1 = 'ok'
l_regra1 = []
regra2 = 'ok'
l_regra2 = []
for i, linha in enumerate(matriz_terrenos):
    for j, a in enumerate(linha):
        if a not in d_terreno_proto[proto]:
            l_regra1.append(f'{i},{j}:{a}')
            regra1 = 'falha'
        for ad in adjacentes(i, j):
            if ad not in d_terreno_adja[a]:
                l_regra2.append(f'{i},{j}:{a}')        
                regra2 = 'falha'
                break
regra3 = 'ok'
l_regra3 = []
for i, (lmapa, lmob) in enumerate(zip(matriz_terrenos, matriz_mobs)):
    for j, (a, m) in enumerate(zip(lmapa, lmob)):
        for numero, mob in enumerate(m):
            tupla = ELEMENTOS[mob]        
            ntupla = tupla[0]+' '+tupla[1]
            ntupla = ntupla.split()
            if numero > 0:
                if anterior not in ntupla and a not in ntupla:
                    print(anterior, mob, i, j)
                    print(ntupla)
                    l_regra3.append(f'{i},{j}:{a}')
                    regra3 = 'falha'
            elif numero == 0:
                if proto not in ntupla or a not in ntupla:
                    l_regra3.append(f'{i},{j}:{a}')
                    regra3 = 'falha'
                anterior = mob
            


# Saída de dados
for num, (regra, lista) in enumerate(zip([regra1, regra2, regra3], [l_regra1, l_regra2, l_regra3])):
    num += 1
    print(f'regra {num}')
    if regra == 'falha':
        for a in lista:
            print(a)
    print(regra)