nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2 
print (f'Tirando {nota1} e {nota2} a media do aluno é {media}')
if media < 5:
    print('Aluno está reprovado')
elif media >=  5 and media < 7:
    print ('Aluno está de recuperação')
elif media >= 7:
    print('Aluno APROVADO')