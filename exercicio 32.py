from datetime import date
ano = float(input('Que ano você quer analisar? Coloque zero para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano:.0f} é BISSEXTO!')
else:
    print(f'O ano de {ano:.0f} Não é BISSEXTO')