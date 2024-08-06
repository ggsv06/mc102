import time as t
import random as rd

# Início
print('''\n
     _                         _                   _ _           _ 
    | | ___   __ _  ___     __| | __ _  __   _____| | |__   __ _| |
 _  | |/ _ \ / _` |/ _ \   / _` |/ _` | \ \ / / _ \ | '_ \ / _` | |
| |_| | (_) | (_| | (_) | | (_| | (_| |  \ V /  __/ | | | | (_| |_|
 \___/ \___/ \__, |\___/   \__,_|\__,_|   \_/ \___|_|_| |_|\__,_(_)
             |___/                                                  
      \n''')
t.sleep(1)

# Condição de vitória
def cond(list):
  # Linhas
  if list[0] == list[1] and list[1] == list[2]:
    return False
  elif list[3] == list[4] and list[4] == list[5]:
    return False
  elif list[6] == list[7] and list[7] == list[8]:
    return False
  #
  elif list[0] == list[3] and list[3] == list[6]:
    return False
  elif list[1] == list[4] and list[4] == list[7]:
    return False
  elif list[2] == list[5] and list[5] == list[8]:
    return False
  
  elif list[0] == list[4] and list[4] == list[8]:
    return False
  elif list[2] == list[4] and list[4] == list[6]:
    return False
  
  else:
    return True

# Inicio para escolher quem fica com x e o
nome1 = input('Nome do jogador 1: ')
p1 = input('x ou o? ')
print(f'{nome1} escolheu {p1}')

nome2 = input('\nNome do jogador 2: ')
if p1 == 'x':
  p2 = 'o'
else:
  p2 = 'x'

print(f'{nome2} ficou com {p2}')
t.sleep(1)
print(f'\nQue o desafio entre {nome1}({p1}) e {nome2}({p2}) comece!')

Lplayers = [nome1, nome2]
Lplayers = rd.choices(Lplayers, k=2)
Lxo = []
if Lplayers[0] == nome1:
  Lxo.append(p1)
  Lxo.append(p2)
else:
  Lxo.append(p2)
  Lxo.append(p1)



# Campo de jogo
Lcampo = ['0', '1', '2', '3', '4', '5', '6', '7', '8']







while cond(Lcampo):
  for p, x in zip(Lplayers, Lxo):
    erro = True
    while erro == True:
        campo_org = f'''
            {Lcampo[0]} {Lcampo[1]} {Lcampo[2]}
            {Lcampo[3]} {Lcampo[4]} {Lcampo[5]}
            {Lcampo[6]} {Lcampo[7]} {Lcampo[8]}
        '''
        print(f'\n{campo_org}')
        marca = input(f'É a vez de {p}. Escolha um dos números disponiveis: ')
        
        try:
            if marca == Lcampo[int(marca)]:
                del Lcampo[int(marca)]
                Lcampo.insert(int(marca), x)
                erro = False
                if cond(Lcampo) == False:
                    break
        except:
            print('digite um valor válido')
    
    vencedor = p
    if cond(Lcampo) == False:
        break

print(campo_org)
print(f'Parabéns {vencedor}!\nVocê venceu!\nObrigado por jogar')


