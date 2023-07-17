somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for ordem in range(1, 5):
    print(f'----- {ordem}º PESSSOA ------')
    nome =  str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if ordem == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade:.0f} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos.')