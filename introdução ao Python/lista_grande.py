import random as r
def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(r.randint(0,n))
    return lista


print(lista_grande(10))