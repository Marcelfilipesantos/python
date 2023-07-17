from random import sample
aluno1 = input('Primeiro aluno: ')
aluno02 = input('Segundo aluno: ')
aluno03 = input ('terceiro aluno: ')
aluno04 = input ('Quarto aluno: ')
lista = [aluno1, aluno02, aluno03, aluno04]
ordem = sample (lista, len(lista))
print(f'A ordem da apresentação será : {ordem} ')