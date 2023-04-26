"""
Functiile sunt ACTIUNI, asa ca numele lor trebuie sa fie verbe.
De exemplu:
print, say_hello, get_area, is_even

In general, pentru functiile care returneaza ceva, vom avea un nume cu get:
get_area, get_number_of_smth

In general, pentru functiile care verifica o conditie, vom avea un nume cu is/has
is_even, has_children, etc.

"""


class Square:

    def __init__(self, l):
        self.l = l

    def get_area(self):
        return self.l * self.l

    def get_perimeter(self):
        return self.l * 4

s1 = Square(5)
print(f'Eu sunt primul patrat, am latura {s1.l}, cu aria {s1.get_area()} si perimetrul {s1.get_perimeter()}')

s2 = Square(12)
print(f'Eu sunt al doilea patrat, am latura {s2.l}, cu aria {s2.get_area()} si perimetrul {s2.get_perimeter()}')


"""
TEMA PENTRU ACASA:
- clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
- fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
  iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati
"""