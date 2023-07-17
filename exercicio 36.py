valorimovel = float(input('Valor do imovel: R$'))
salario = float(input('Qual a renda do comprador: R$'))
tempofinanciado = float(input('Quantos anos de financiamento?'))
meses = tempofinanciado * 12
financiamento = valorimovel / meses
print(f'Para pagar uma casa de R${valorimovel:.0f} em {tempofinanciado:.0f} anos a prestação será de R${financiamento:.2f}')
if financiamento <= salario * 30 / 100:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo não pode ser concedido')