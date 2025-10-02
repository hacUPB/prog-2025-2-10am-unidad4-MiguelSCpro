import random
lista=[]
for i in range (100):
    aleatorio = random.randint(100,1000)
    lista.append(aleatorio)
suma=0
for i in range(len(lista)):
    suma += lista[i]
prom = suma/len(lista)

print(f"Promedio = {prom}")
mayor = max(lista)
menor = min(lista)
print(mayor)
print(menor)

