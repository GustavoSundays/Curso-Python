import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 8]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]

title = "Scatterplot"
axisX = "Axis x"
axisY = "Axis y"

plt.title(title)
plt.xlabel(axisX)
plt.ylabel(axisY)

plt.scatter(x, y, label = "My points", color = "k", marker = ".", s = z)
plt.plot(x, y, color = "#009900", linestyle = "-")
plt.legend()
#plt.show()
plt.savefig("Figure1.png", dpi = 300)