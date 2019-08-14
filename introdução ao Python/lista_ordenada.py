def ordenada(lista):
    index = 1;
    for i in range(len(lista)):
        if index > len(lista) - 1:
            return True
        if lista[i] < lista[index]:
            index = index+1;
        else:
            return False
    return True

print(ordenada([1,2,3,5,6]))
        