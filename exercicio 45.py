from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("Suas opções:\n[0] Pedra\n[1] PAPEL\n[2] TESOURA")
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: # computado jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada invalida!')


elif computador == 1: # computador jogou Papel
    if jogador == 0:
        print ('Computador vence')
    elif jogador == 1:
        print ('EMPATE')
    elif jogador == 2:
        print ('Jogador vence')
    else:
        print('Jogada invalida!')

elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print ('Computador vence')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida!')