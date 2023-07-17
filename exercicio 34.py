salario = float(input('Qual é o salario do funcionario?'))

if salario <= 1250:
    novo = float(salario + (salario * 15 / 100)) 

else:
    novo = float(salario + (salario * 10 / 100)) 

print(f'seu salario atual é de {salario:.2f} e após o aumento será {novo:.2f}')    