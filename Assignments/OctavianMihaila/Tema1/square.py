"""
TEMA PENTRU ACASA:
- clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
- fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
  iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati
"""
import math


class Circle:
    def __init__(self, radius, color='Gri'):
        self.radius = radius
        self.color = color

    def get_area(self):
        return math.pi*self.radius*self.radius

    def get_perimeter(self):
        return 2*math.pi*self.radius

    def describe(self):
        print("-" * 40)
        print(f"Cerc de raza {self.radius}")
        print(f"Aria de {self.get_area():.2f}")
        print(f"Perimetru de {self.get_perimeter():.2f}")
        print(f"Culoare {self.color}")
        print("-" * 40)


c1 = Circle(5)
c2 = Circle(10, 'Mov')

c1.describe()
c2.describe()
