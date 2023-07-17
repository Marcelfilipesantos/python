#soma = 0
#for c in range(1, 7):
#    n1 = int(input(f'Digite o {c}º valor: '))
#    if n1 % 2 == 0:
#        soma = soma + n1    
#print(f'O resultado da soma dos numeros pares será igual a {soma}' if soma != 0 else 'Não tem numeros pares para somar.')
soma = 0 
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print (f'Você informou {cont} pares e a soma foi {soma}')

