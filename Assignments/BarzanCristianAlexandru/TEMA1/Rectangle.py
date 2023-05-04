class Rectangle:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def get_area(self):
        return  self.lungime * self.latime

    def get_perimeter(self):
        return 2 * (self.lungime + self.latime)
    def describe(self):
        return self.culoare

d1 = Rectangle(2, 3, 'Rosu')
print(f'Eu sunt primul dreptunghi de culoare {d1.culoare}, am lungimea {d1.lungime}, latimea {d1.latime} cu aria {d1.get_area()} si perimetrul {d1.get_perimeter()}')