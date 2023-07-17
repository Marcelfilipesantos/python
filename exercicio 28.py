from random import randint
from time import sleep
print('-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
sort = randint(0, 5)
numero = int(input('Em que numero em pensei? '))
print('PROCESSANDO...')
sleep(2)
if sort == numero:
    print('Parabéns você conseguiu me vencer')
else:
    print(f'Ganhei! Eu pensei no numero {sort} e não no {numero}!')