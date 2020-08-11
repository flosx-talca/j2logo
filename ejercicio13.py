import random
def acumulado(lista):
    for i in range(1,len(lista)):
        lista[i]=lista[i]+lista[i-1]
    return lista


lista = [random.randint(1, 5)for i in range(5)]
print(f"Lista inicial: {lista}")
print (f"Lista final: {acumulado(lista)}")
