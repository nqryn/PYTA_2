"""
TEMA PENTRU ACASA:
- clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
- fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
  iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati
"""


class Circle:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def get_area(self):
        return 3.14 * self.raza * self.raza

    def get_perimeter(self):
        return 2 * 3.14 * self.raza

c1 = Circle(2, 'Rosu')
print(f'Eu sunt primul cerc, am raza {c1.raza}, cu aria {c1.get_area()} , perimetrul {c1.get_perimeter()} si sunt {c1.culoare}')

c2 = Circle(3, 'Verde')
print(f'Eu sunt al doilea cerc, am raza {c2.raza}, cu aria {c2.get_area()} , perimetrul {c2.get_perimeter()} si sunt {c2.culoare}')
