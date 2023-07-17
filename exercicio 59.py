valor01 = int(input('Digite o primeiro valor: '))
valor02 = int(input('Digite o segundo valor: '))
menu = 0
while menu !=5:
    print('''    [1] somar'
    [2] Multiplicar
    [3] Maior
    [4] novos numeros
    [5] Sair do programa''')
    menu = int(input('Qual é a sua opção? '))

    if menu == 1:
        soma = valor01 + valor02
        print(f'A Soma dos numeros {valor01} e {valor02} é {soma}.')
    elif menu == 2:
        mult = valor01 * valor02
        print(f'A multiplicação dos numeros {valor01} e {valor02} é {mult}')
    elif menu == 3:
        if valor01 > valor02:
            maior = valor01
        else:
            maior = valor02
        print(f'Entre {valor01} e {valor02} o maior valor é {maior}')
    elif menu == 4:
        print('Informe os numeros novamente: ')
        valor01 = int(input('Primeiro valor: '))
        valor02 = int(input('Segundo valor: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente.')
print('FIm do programa! volte sempre!')