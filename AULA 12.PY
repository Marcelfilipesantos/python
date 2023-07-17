#elif - senão se 
nome = str(input('Qual é o seu nome?'))
if nome == 'Marcel':
    print ('Que nome bonito!!!')
elif nome == 'Anne' or nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular no brasil!!')
else:
    print('Seu nome é bem normal!')    

print(f'Tenha um otimo dia, {nome}!')