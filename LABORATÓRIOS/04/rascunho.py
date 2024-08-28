acabou = 0
c=0
while True:
    horas, minutos, tempo_pedido = [int(x) for x in input().replace(":", " ").split()]

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
print(c)