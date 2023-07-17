numero = float(input('Me diga um numero qualquer: '))
## No python quando um numero é inteiro não vai existe resto por tanto sempre transformar em numero real quando for fazer uma divisão e utilizar o resto.
if numero % 2 == 0: # o resto "%" só funciona com numeros reais.
    print(f'O numero é par {numero:.0f}')
else:
     print(f'O numero é impar {numero:.0f}')