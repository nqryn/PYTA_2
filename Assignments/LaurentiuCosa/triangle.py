import math

class Triangle:

    def __init__(self, a, b, c, name, colour):
        self.a = a
        self.b = b
        self.c = c
        self.name = name
        self.colour = colour

    def get_semiperimeter(self):
        return (self.a + self.b + self.c) / 2

    def get_area(self):
        return round(math.sqrt(self.get_semiperimeter() * ((self.get_semiperimeter() - self.a) * (self.get_semiperimeter() - self.b) * (self.get_semiperimeter() - self.c))),2)


t1 = Triangle(4,6,8,"Triunghiul 1", "Galben")

print(f"{t1.get_semiperimeter()}, {t1.get_area()}")