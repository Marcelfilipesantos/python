velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade <= 80:
    print('Tenha um bom dia! dirija com segurança!')
else:
    print('MULTADO!Você execedeu o limite permitido que é de 80km/h')
    velocidade -= 80
    multa = velocidade * 7
    print(f'você deve pagar uma multa de R${multa:.2f} reais!')
    print('Tenha um bom dia! dirija com segurança!')