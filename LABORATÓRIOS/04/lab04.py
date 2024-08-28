###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Chefe de Cozinha
# Nome:Gian Gabriel Silva Vianna
# RA: 278439
###################################################
  
# Leitura da entrada
acabou = 0
c=0
while True:
    horas, minutos, tempo_pedido = [int(x) for x in input().replace(":", " ").split()]

# Processamento dos dados
    mins = horas*60 +minutos

    if acabou <= mins:
        acabou = mins + tempo_pedido
    
    elif acabou > mins:
        acabou += tempo_pedido


    if acabou >= 1380:
        break
    if horas == 00 and minutos == 00:
        break
    c+=1
    
# Saída de dados
print(c)
    
   



