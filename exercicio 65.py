status = ''
n1  = 0
cont = 0
media = 0
soma = 0
maior = 0
menor = float('inf')
while status != 'N':
    n1 = float(input('Digite um numero: '))
    status = str(input('Quer continuar?[S/N]')).strip().upper()
    cont += 1
    soma += n1
    media  = soma / cont
    if status not in "SN":
        status = status = str(input('Comando invalido tente novamente!! Quer continuar?[S/N]')).strip().upper()
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

print(f'você digitou {cont} números e a media é de {media:.2f}')
print(f'{maior:.0f} e {menor:.0f}')