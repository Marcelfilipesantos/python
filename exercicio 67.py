n = 0
cont = 1
multi = 0
print('-' * 35)
n = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 35)
while True:
    multi = n * cont
    print(f'{n} x {cont} = {multi}')
    cont += 1
    if cont == 11:
        n = int(input('Quer ver a tabuada de qual valor? '))
        cont = 1
    if n < 0:
        break
print('Obrigado por usar o nosso programa!')
