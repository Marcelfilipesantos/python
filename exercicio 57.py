'''sexo = str(input('Infome seu sexo: [M/F]')).strip().upper()[0]
while sexo != 'M'and sexo !='F':
    sexo  = str(input('Dados invalidos, por favor informe seu sexo:')).upper()    
print(f'Sexo {sexo} registrado como sucesso!')'''

sexo = str(input('Infome seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo  = str(input('Dados invalidos, por favor informe seu sexo:')).strip().upper()[0]  
print(f'Sexo {sexo} registrado como sucesso!')
idade = int(input('Digite sua idade:'))
while idade == int :
    idade = int(input('Dados invalidos, por favor sua idade:'))
print(f'idade {idade} registrada com sucesso.')    