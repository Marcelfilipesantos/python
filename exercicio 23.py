nome =  str(input('Digite seu nome completo: ')).strip()
print ('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas {nome.upper()}')
print(f'Seu nome em letras minusculas {nome.lower()}')
print(f"Seu nome tem ao todo {(len(nome) - nome.count(' '))} letras")
#print(f'Seu primeiro nome tem {((nome.find(" ")))} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {(len(separa[0]))} letras')