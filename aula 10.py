# condicionais #

#carro.siga() - o Carro é o objeto e o siga é o comando!

#tempo = int(input('Quantos anos tem o seu carro?'))
#if tempo <= 3:
#    print('Carro novo')
#else:
#    print('Carro velho, por favor comprar um carro novo!')
#print ('--fim--')

# condição simplificada

#tempo = int(input('Quantos anos tem o seu carro?'))
#print('carro novo'if tempo <=3 else 'carro velho')
#print('--fim--')

#nome =  str(input('Qual é o seu nome?'))
#if nome == 'Marcel':
#    print('Que nome lindo você tem!')
#else:
#    print('Seu nome é Maravilhoso!!!')
#print(f'Bom dia, {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua media foi {m:.1f}')
if m >= 6.0:
    print('Sua media foi boa! PARABÉNS!!!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')