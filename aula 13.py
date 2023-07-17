#laço  c no intervalo(1, 10)
#    passo
#pega
#for c in range(1, 10):
#    passo
#pega

# for c in range(0,3)
# if coin
#    pega
#   passo
#   pula
# passo
# pega

# -----------------------------------
#for c in range(10,0, -1):
#    print(c)
#print('FIM')

inicio =  int(input('Digite um numero:'))
fim =  int(input('Digite um numero:'))
passo = int(input('Digite um numero:'))
for c in range(inicio, fim+1,  passo):
    print(c)
print('FIM')