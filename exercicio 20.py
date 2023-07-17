import random
aluno01 = input('Primeiro aluno: ')
aluno02 = input('Segundo aluno: ')
aluno03 = input('terceiro aluno: ')
aluno04 = input ('Quarto aluno: ')
lista = [aluno01, aluno02, aluno03, aluno04]
print(f'O aluno escolhido foi: {random.choice(lista)}')