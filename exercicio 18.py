#from math import sqrt
#co = float(input('Comprimento do cateto oposto: '))
#cad = float(input('Comprimento do cateto adjacente: '))
#hipo = sqrt (co **2 + cad **2)
#print(f'A hipotenusa vai medir {hipo:.2f}')


from math import hypot
co = float(input('Comprimento do cateto aposto: '))
cad = float(input('comprimento do cateto adjacente: '))
hipo = hypot (co, cad)
print(f'A hipotenusa vai medir {hipo:.2f}')