cont = 0
numero = 0
soma = 0
numero = int(input('Digite um número [999 para parar]:'))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]:'))
     
       
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')
