###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Geladeiras Subzero
# Nome: Gian Gabriel Silva Vianna
# RA: 278439
###################################################

# leitura de dados
tipo = input()
pessoas = int(input())
potencia = int(input())

# Verificação e impressão do nome do modelo a ser recomendado
if tipo == 'S':
    if potencia > 130:
        print('Frost++')
    elif pessoas in [1,2]:
        if potencia <= 70:
            print('Gel-S')
        elif potencia <= 130:
            print('Gel-SPlus')
    elif pessoas == 3:
        if potencia <= 130:
            print('DeluxFF')
    elif pessoas > 3:
        if potencia <= 100:
            print('IceCold')
        elif potencia <= 130:
            print('DeluxFF')
        
elif tipo == 'D':
    if pessoas == 1:
        print('Gel-D')
    elif pessoas >= 4:
        if potencia <= 100:
            print('IceCold')
        elif potencia > 100:
            print('Frost++')
    elif pessoas == 2:
        if potencia <= 150:
            print('Gel-DPlus') 
        elif potencia > 150:
            print('DupCold')
    elif pessoas == 3:
        if potencia <= 100:
            print('Gel-DPlus')
        elif potencia > 100:
            print('DupCold')
