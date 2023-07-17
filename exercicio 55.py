maior = 0
menor = 0
for pe in range(1, 6):
    peso = float(input(f"Peso da {pe}º pessoa: "))
    if pe == 1: 
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:.2f} kg')
print(f'O menor peso lido foi de {menor:.2f} kg')