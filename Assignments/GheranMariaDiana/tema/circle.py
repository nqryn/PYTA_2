class Circle:

    def __init__(self,r, color='Red'):
        self.r = r
        self.color = color

    def get_diameter(self):
        return self.r * 2

    def get_area(self):
        return self.r * self.r * 3.14

    #metoda de descriere
    def describe(self):
        print('=' *20, f'Cerc cu raza de {self.r} cm si culoare {self.color}','=' *20)
        print(f'Color: {self.color}')
        if self.r > 20:
            print(f'Cerc mare')
        else:
            print(f'Cerc mic')


c = Circle(4)
c.describe()
print()

c1 = Circle(10)
c1.describe()
print(f'Cerc cu raza de {c1.r}, de culoare {c1.color} cu diametrul {c1.get_diameter()} si aria {c1.get_area()}')
print()

c2 = Circle(25)
c2.describe()
print(f'Cerc cu raza de {c2.r}, de culoare {c2.color} cu diametrul {c2.get_diameter()} si aria {c2.get_area()}')
print()