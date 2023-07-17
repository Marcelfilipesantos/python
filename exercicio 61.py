print('=' * 35)
print('   10 TERMO DE UMA PA')
print('='*35)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
while c <= 10:
    print(f'{termo}', end='-')
    c += 1
    termo += razao
print('ACABOU')



