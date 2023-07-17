'''from random import randint
from time import sleep
print('-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
sort = randint(0, 10)
numero = int(input('Qual é o seu palpite? '))
tentativas = 0
while sort != numero:
    if numero < sort:
        print('mais... tente novamente.')
        numero = int(input('Qual é o seu palpite? '))
        tentativas += 1
    if numero > sort:
        print('Menos... tente novamente.')
        numero = int(input('Qual é o seu palpite? '))
        tentativas += 1
print('PROCESSANDO...')
sleep(2)
if sort == numero:
    print(f'Acertou com {tentativas} tentativas. Parabéns!!!')'''

from random import randint
computer = randint(0, 10)
print('Sou seu computador... acabei de pensar em um numero entre 0 a 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites +=1
    if jogador == computer:
        acertou = True
    else:
        if jogador < computer:
            print('Mais...Tente mais uma vez.')
        elif jogador > computer:
            print('Menos... Tente mais uma vez.')
print(f'Acertou {palpites} tentativas. Parabéns!')
