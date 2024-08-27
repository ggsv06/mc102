###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Chefe de Cozinha
# Nome:Gian Gabriel Silva Vianna
# RA: 278439
###################################################
  
# Leitura da entrada
c=0

horas_acabei, minutos_acabei = 0, 0
while True:
    horas, minutos, tempo_pedido = [int(x) for x in input().replace(":", " ").split()]
    
# Processamento dos dados
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
        break

    elif horas == minutos & horas == 00:
        break
    
    horas_acabei, minutos_acabei = horas, minutos
    c+=1
    
 

# Saída de dados
print(c)


