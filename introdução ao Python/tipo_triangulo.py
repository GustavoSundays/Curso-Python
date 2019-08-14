class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif (self.a == self.b and self.b != self.c) or (self.b == self.c and self.c != self.a) or (self.a == self.c and self.c != self.b):
            return "isósceles"
        else:
            return "escaleno"

t = Triangulo(5, 5, 6)

print(t.a)
print(t.b)
print(t.c)
print(t.tipo_lado())