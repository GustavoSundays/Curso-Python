def primeiro_lex(lista):
    index = 0
    for i in range(len(lista)):
        if lista[index] > lista[i]:
            index = i
    return lista[index]


print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))