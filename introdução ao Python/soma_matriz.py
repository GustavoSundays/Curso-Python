def soma_matrizes(m1, m2):
    if len(m1) == len(m2):
        if len(m1[0]) == len(m2[0]):
            matriz = []
            for i in range(len(m1)):
                resultado = []
                for j in range(len(m1[0])):
                    soma = m1[i][j] + m2[i][j]
                    resultado.append(soma)
                matriz.append(resultado)
            
            return matriz

        else:
            return False

    else:
        return False

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))