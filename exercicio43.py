peso = float(input('Qual é o seu peso?(kg)'))
altura = float(input('Qual é a sua altura?(m)'))
imc = peso / (altura ** 2)
print(f'O IMC da pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('Abaixo do peso ideal')
elif imc <= 25:
    print('PARABÉns você está no Peso ideal')
elif imc <= 30:
    print('CUIDADO você está com Sobrepeso')
elif imc <= 40:
    print ("Por favor procure um medico, você está com OBESIDADE.")
else:
    print('Muito cuidado você está com OBESIDADE MORBIDA.')