"""
TEMA PENTRU ACASA:
- clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
- fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
  iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati
"""

class Rectangle:

    def __init__(self, lat, lun, color):
        self.lat = lat
        self.lun = lun
        self.color = color

    def get_perimeter(self):
        return self.lat * 2 + self.lun * 2

    def get_area(self):
        return self.lat * self.lun

    def describe(self):
        print(f"Acesta este un dreptunghi cu latimea de {self.lat}, lungimea de {self.lun} si culoarea {self.color}.")

r1 = Rectangle(10, 15, "Red")
r1.describe()
print(f"Rectangle perimeter is {r1.get_perimeter()}, rectangle area is {r1.get_area()}")