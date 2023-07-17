print('=' * 35)
print('   10 TERMO DE UMA PA')
print('='*35)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
soma = termo + (10 - 1)* razao
for c in range(termo, soma + razao, razao):
    print(f'{c}', end='-')
print('ACABOU')