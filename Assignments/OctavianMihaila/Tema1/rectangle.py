"""
TEMA PENTRU ACASA:
- clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
- fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
  iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati
"""


class Rectangle:
    def __init__(self, length, width, color='Grey'):
        self.length = length
        self.width = width
        self.color = color

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def describe(self):
        print("-" * 40)
        print(f"Dreptunghi cu lungimea de {self.length} si latimea de {self.width}")
        print(f"Aria de {self.get_area()}")
        print(f"Perimetrul de {self.get_perimeter()}")
        print(f"Culoare {self.color}")


r1 = Rectangle(10, 5)
r2 = Rectangle(6, 3, 'Green')

r1.describe()
r2.describe()

