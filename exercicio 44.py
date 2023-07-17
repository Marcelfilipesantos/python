print('======== Lojas MARCEL ======== ')
compras = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO')
print ('[1] à vista dinheiro/pix')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print ('[4] 3x ou mais no cartão')
opcao = int(input(('Digite a opção de pagamento? ')))
if opcao == 1:
    desconto = float(compras - (compras * 10 / 100))
    print (f'Suas compra é de R${compras:.2f} vai custar R${desconto:.2f} com o desconto')
elif opcao == 2:
    desconto = float(compras - (compras * 5/100))
    print(f'Suas compra é de R${compras:.2f} vai custar R${desconto:.2f} com o desconto')
elif opcao == 3:
    parcelamento = compras / 2 
    print(f'Suas compras é de R${compras:.2f} e será parcelada em 2x de R${parcelamento:.2f} sem juros')
elif opcao == 4:
    qts = int(input('Quantas parcelas? '))
    juros = float(compras * 20/100)
    parcelamento = (compras + juros) / qts
    valort = compras + juros
    print(f'Sua compras será parcelada em {qts}x de R${parcelamento:.2f} com juros.')
    print(f'Sua compra de R${compras:.2f} vai custar R${valort} no final ')
else:
    total = preço
    print('Opção invalida! tente novamente.')

