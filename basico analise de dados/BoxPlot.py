import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    numeroAleatorio = random.randint(0,2)
    vetor.append(numeroAleatorio)

plt.boxplot(vetor)
plt.show()