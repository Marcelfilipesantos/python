import math
angulo = int(input('Digite o angulo que você deseja: '))
rad = math.radians(angulo)
seno = math.sin(rad)
conseno = math.cos(rad)
tangente = math.tan(rad)
print(f'O ângulo de {angulo} tem seno de {seno :.2f}')
print(f'O ângulo de {angulo} tem conseno de {conseno :.2f}')
print(f'O ângulo de {angulo} tem tangente de {tangente :.2f}')