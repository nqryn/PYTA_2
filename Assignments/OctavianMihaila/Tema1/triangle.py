"""
TEMA PENTRU ACASA:
- clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
- fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
  iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati
"""
import math


class Triangle:
    def __init__(self, side1, side2, base, color='Grey'):
        self.side1 = side1
        self.side2 = side2
        self.base = base
        self.color = color

    def is_triangle(self):
        if self.side1 + self.side2 <= self.base:
            return False
        else:
            return True

    def get_perimeter(self):
        return float(self.side1 + self.side2 + self.base)

    def get_area(self):
        half_p = float(self.get_perimeter()/2)
        # print(half_p)
        return math.sqrt(half_p*(half_p-self.side1)*(half_p-self.side2)*(half_p-self.base))

    def describe(self):
        print('-' * 40)
        print(f"Triangle with Base = {self.base}, Side One = {self.side1} and Side Two = {self.side2}")
        if self.is_triangle():
            print(f"Perimeter = {self.get_perimeter()}")
            print(f"Area = {self.get_area():.2f}")
            print(f"Color = {self.color}")
        else:
            print("Triangle is not valid")
        print('-' * 40)


t1 = Triangle(3, 3, 5)
t2 = Triangle(1, 4, 10, 'Blue')

t1.describe()
t2.describe()
