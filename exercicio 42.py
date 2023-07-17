#print('------------------------')
#print('ANALISADOR DE TRIÂNGULO')
#print('------------------------')
#n1 = float(input('Primeiro segmento: '))
#n2 = float(input('Segundo segmento: '))
#n3 = float(input('Terceiro segmento: '))
#triangulo = n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2
#if triangulo and n1 == n2 == n3:
#    print('Os segmentos podem formar um tringulo equilátero!')
#elif  triangulo and n1 != n2 == n3 or n2 != n3 == n1 or n3 != n2 == n1:
#    print ('Os segmentos acima formam um triangulo ISÓSCELES ')
#elif triangulo and n1 != n2 != n3 and n2 != n1 != n3 and n3 != n2 !=n1:
#    print('Os segmentos acima foram um triangulo ESCALENO')
#else:
#    print('Não podem formar um triangulo é um triangulo')


print('------------------------')
print('ANALISADOR DE TRIÂNGULO')
print('------------------------')
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if n1 == n2 == n3:
        print('EQUILATERO')
    elif n1 != n2 != n3 !=n1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Não podem formar um triangulo é um triangulo')

