
c=0
fim=0
horas_acabei, minutos_acabei = 0, 0
while True:
    horas, minutos, tempo_pedido = [int(x) for x in input().replace(":", " ").split()]
    
    if horas_acabei < horas or (horas_acabei == horas and minutos_acabei <= minutos):
        
        horas += tempo_pedido // 60
        minutos += tempo_pedido % 60

        if minutos >= 60:
            horas += minutos // 60
            minutos = minutos % 60
    else:

        horas_acabei += tempo_pedido // 60
        minutos_acabei += tempo_pedido % 60

        if minutos >= 60:
            horas_acabei += minutos // 60
            minutos_acabei = minutos % 60
        
        horas, minutos = horas_acabei, minutos_acabei
    

    if horas >= 23:
        fim = 1

    elif horas == minutos & horas == 00:
        break
    
    horas_acabei, minutos_acabei = horas, minutos
    c+=1
    
    if fim == 1:
        break
print(c)
