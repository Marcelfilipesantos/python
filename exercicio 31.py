distancia = float(input('Qual é a distancia da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {distancia}km.')
if distancia <= 200:
    passagem = (distancia * 0.50)
    
else:
    passagem = (distancia * 0.45)
    
print(f'E o preço da sua passagem será de R${passagem:.2f} reais!')