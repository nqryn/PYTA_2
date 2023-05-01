"""
TEMA PENTRU ACASA:
- clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
- fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
  iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati
"""

import math

class Circle:

    def __init__(self, r, color):
        self.r = r
        self.color = color

    def get_diameter(self):
        return self.r * 2

    def get_area(self):
        return math.pi * self.r * self.r

    def describe(self):
        print(f"Acesta este un cerc cu raza {self.r}, culoarea {self.color}")

c1 = Circle(9, 'Blue')
print(f"Acesta este un cerc cu diametrul {c1.get_diameter()} si aria {c1.get_area()}")

c1.describe()

c2 = Circle(10, "Red")
c2.describe()
