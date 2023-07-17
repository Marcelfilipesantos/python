n1 = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
(print (f'[1] Converte para binario'))
(print(f'[2] Converte para Octal'))
(print(f'[3] Converte para hexadecimal'))
list = [1 , 2 , 3]
opcao = int(input('Sua opção: '))

if opcao == 1:
    print (f'{n1} convertido para Binario é igual a {bin(n1)[2:]}') 
elif opcao == 2:
     print (f'{n1} Convertido para Octal é igual a {oct(n1)[2:]}')
elif opcao == 3:
     print(f'{n1} Convertido para Hexadicimal é igual a {hex(n1)[2:]}')

else:
     print('Opção invalida')



