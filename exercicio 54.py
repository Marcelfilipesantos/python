from datetime import date
datanow = date.today().year
maior = 0
menor = 0
for c in range(1, 7):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu?'))
    idade = datanow - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1        
print (f'Ao todo tivemos {maior} pessoas maiores de idade.')
print (f'E também tivemos {menor} pessoas menores de idade.') 
