from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print(f'O Atleta tem {idade} anos.')
if idade  <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print ('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificão: JUNIOR')
elif idade <= 25:
    print ('Classificação: SENIOR')
else:
    print ('Classificação: MASTER')