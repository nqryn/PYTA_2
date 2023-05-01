"""
TEMA PENTRU ACASA:
- clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
- fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
  iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati
"""

import math

class Triangle:


    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def get_perimeter(self):
        return self.l1 + self.l2 + self.l3

    def get_semiperimeter(self):
        return (self.l1 + self.l2 + self.l3) * 0.5

    def get_area(self):
        sp = (self.l1 + self.l2 + self.l3) * 0.5
        return (sp*(sp-self.l1)*(sp-self.l2)*(sp-self.l3))

t1 = Triangle(7, 8, 3)
print(f"Perimetrul este {t1.get_perimeter()}")
print(f"Semiperimetrul este {t1.get_semiperimeter()}")
print(f"Aria este {t1.get_area()}")