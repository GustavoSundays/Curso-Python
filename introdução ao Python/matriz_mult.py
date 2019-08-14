def sao_multiplicaveis(m1, m2):
    tam1 = len(m1[0])
    tam2 = len(m2)
    if tam1 == tam2:
        return True
    else:
        return False


m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(m1, m2))