nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu sobrenome é {nome.split()[-1]}')