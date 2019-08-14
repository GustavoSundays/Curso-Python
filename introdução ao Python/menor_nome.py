def menor_nome(nomes):
    index = 0
    for i in range(len(nomes)):
        nomes[i] = nomes[i].strip().capitalize()
        if len(nomes[i]) < len(nomes[index]):
            index = i
    menor_nome = nomes[index]
    return menor_nome

print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))

print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))

print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))