d = float(input('Uma distancia em metros '))
km = (d/1000)
hm = (d/100)
dam = (d/10)
dm = round(d*10)
cm = round(d*100)
mili = round(d*1000)
print(f"A medida de {d} m corresponde a:\n {km} km \n {hm} hm \n {dam} dam \n {dm} dm \n {cm} cm \n {mili} mili ")