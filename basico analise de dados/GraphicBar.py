import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 8]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

title = "Graphic Bar 2"
axisX = "Axis x"
axisY = "Axis y"

plt.title(title)
plt.xlabel(axisX)
plt.ylabel(axisY)

plt.bar(x1, y1, label = "Group 1")
plt.bar(x2, y2, label = "Group 2")
plt.legend()
plt.show()