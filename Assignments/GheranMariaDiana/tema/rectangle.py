class Rectangle:
#inside the class we have a Constructor with 3 parameters
    def __init__(self, l, L, color='Blue'):
        self.l = l
        self.L = L
        self.color = color

    def get_area(self):
        return self.l*self.L

    def get_perimeter(self):
        return 2*self.l+2*self.L

    #metoda de descriere
    def describe(self):
        print('=' *20, f'Dreptunghi cu latime {self.l}, lumgine {self.L} si culoare {self.color}','=' *20)
        print(f'Color: {self.color}')
        if self.l > self.L:
            print(f'Latimea mai mare decat lungimea')
        else:
            print(f'OK')


L = int(input('Lungimea este: '))
l = int(input('Latimea este: '))
# cream obiectul r1 pentru clasa Rectangle
r1 = Rectangle(l,L)
r1.describe()
print(f'Aria dreptunghiului este {r1.get_area()} iar perimetrul este {r1.get_perimeter()}')
print()

r2 = Rectangle(12,4)
r2.describe()
print(f'Aria dreptunghiului este {r2.get_area()} iar perimetrul este {r2.get_perimeter()}')