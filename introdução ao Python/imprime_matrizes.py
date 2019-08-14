def imprime_matriz(minha_matriz):
    for i in range(len(minha_matriz)):
        for j in range(len(minha_matriz[0])):
            if j != len(minha_matriz[0]) - 1:
                print(minha_matriz[i][j], end = " ")
            else:
                print(minha_matriz[i][j], end="")
        print()


minha_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
imprime_matriz(minha_matriz)
