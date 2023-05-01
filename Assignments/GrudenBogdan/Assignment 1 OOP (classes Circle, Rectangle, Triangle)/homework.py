import math
"""
Tema pentru acasa:

- clase pentru urmatoarele:Circle(cerc), rectangle(dreptunghi), triangle(triunghi)
-Fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
 iar ca metode se vor face cele geometrice care au sens(area si perietru) plus o metoda de describe.
- din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa testati.
"""

class Circle:
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color

    def describe(self):
       return f'Cercul are culoarea {self.color} si raza de {self.raza} metri'

    def area(self):
        return f'Aria cercului este de {3.14 * (self.raza ** 2)} metri'

    def diameter(self):
        return f'Diametru cercului este de {2 * self.raza} metri'

    def perimeter(self):
        return f'Perimetrul cercului este de {2 * self.raza * 3.14} metri'


cerc1 = Circle(4, 'Albastru')
print(cerc1.describe())
print(cerc1.area())
print(cerc1.diameter())
print(cerc1.perimeter())


class Rectangle:
    def __init__(self, lungime, latime, culoare):
         self.lungime = lungime
         self.latime = latime
         self.culoare = culoare
    def describe(self):
        print(f'Dreptughiul are culoare {self.culoare}, lungimea laturii de {self.lungime} si latime laturii de {self.latime}')

    def area(self):
        print('Aria dreptunghiului este de', self.latime * self.lungime, 'metri')

    def perimeter(self):
        print(f'Perimetrul dreptunghiul este de {2*(self.latime+self.lungime)}')


drept1 = Rectangle(5, 3, 'Rosu')
drept1.describe()
drept1.area()
drept1.perimeter()


class Triangle:
    def __init__(self, latura1, latura2, baza, culoare):
         self.latura1 = latura1
         self.latura2 = latura2
         self.culoare = culoare
         self.baza = baza


    def describe(self):
        print(f'Triughiul are o latura egala cu {self.latura1}, a doua egala cu {self.latura2}, baza egala cu {self.baza} si culoare {self.culoare}')

    def area(self):
        if self.latura1 == self.latura2 and self.latura1 != self.baza:
             h = self.latura2 ** 2 - (self.latura1 ** 2) / 4
             h_value = math.sqrt(h)
             print('Inaltimea este egala cu:',h_value)
             print(f'Aria triunghiului este {(self.baza * h_value) / 2}')

        elif self.latura1 == self.latura2 == self.baza:
            print(f'Aria triunghiului este de {(math.sqrt(3)/4)*(self.latura1 * self.latura1)}')

        else:
            P = self.latura1 + self.latura2 + self.baza
            p = P / 2
            area_tri = p * (p-self.latura1) * (p - self.latura2) * (p-self.baza)
            print(f'Aria triunghiuli este de {math.sqrt(area_tri)}')

    def perimeter(self):
            print(f'Perimetrul triunghiului este de {self.latura1 + self.latura2 + self.baza}')



tri1 = Triangle(5, 5, 6, 'Rosu')  #  Isoscel
tri1.describe()
tri1.area()
tri1.perimeter()

tri2 = Triangle(5, 5, 5, 'Rosu')  #  Echilateral
tri2.describe()
tri2.area()
tri2.perimeter()

tri3 = Triangle(2,3,4, 'Rosu') #  Oarecare
tri3.describe()
tri3.area()
tri3.perimeter()
