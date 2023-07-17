print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
termo = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print('~' * 30)
print (f'{t1} - {t2} ', end='')
while c <= termo:
    t3 = t1 + t2
    print(f'{t3}  ', end ='')
    c += 1
    t1 = t2
    t2 = t3
print('- fim')
print('~' * 30)