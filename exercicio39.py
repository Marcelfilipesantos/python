import datetime 
nas = int(input('Ano de nascimento: '))
ano = datetime.datetime.now().year
idade = ano - nas
atraso = (idade - 18)
alistamento = (ano - atraso)
prazo = 18 - idade
idadef = ano + prazo
print(f'Quem nasceu em {nas} tem {idade} anos em {ano} ')
if idade == 18:
    print ('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {atraso} anos atrás seu alistamento foi em {alistamento}')
elif idade < 18:
    print(f'Ainda faltam {prazo} anos para seu alistamento seu alistamento será em {idadef} .')