# Crescimento da população brasileira 1980-2016
# DataSus

import matplotlib.pyplot as plt

dados = open("populacao brasileira/populacao-brasileira.csv").readlines()

ano = []
populacao = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        ano.append(int(linha[0]))
        populacao.append(int(linha[1]))

plt.bar(ano, populacao, color = "#e4e4e4")
plt.plot(ano, populacao, color = "k", linestyle = "--")
plt.title("Crescimento da população brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()
##plt.savefig("populacao-brasileira.png", dpi = 300)

        