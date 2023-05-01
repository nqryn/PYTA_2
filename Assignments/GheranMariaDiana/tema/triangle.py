class Triangle:

    def __init__(self,l1,l2,l3,color='Green'):
        #urmeaza valorile atributelor obiectului pe self
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.color = color

    def get_perimeter(self):
        return self.l1 + self.l2 + self.l3

    def get_semi_perimeter(self):
        return (self.l1 + self.l2 + self.l3) / 2

    def get_area(self):
        sp = (self.l1 + self.l2 + self.l3) / 2
        return (sp * (sp-self.l1)*(sp-self.l2)*(sp-self.l3)) ** 0.5

    # metoda de descriere
    def describe(self):
        print('=' * 20, f'Triungi cu laturile:  {self.l1}, {self.l2}, {self.l3} si culoare {self.color}', '=' * 20)
        print(f'Color: {self.color}')
        if self.l1 == self.l2 and self.l2==self.l3 and self.l1==self.l3:
            print(f'Triunghi echilateral')
        else:
            if self.l1 == self.l2 or self.l2==self.l3 or self.l1==self.l3:
                print(f'Triunghi isoscel')
            else:
                print(f'Triunghi oarecare')

lat1 = int(input('Latura 1 este:'))
lat2 = int(input('Latura 2 este:'))
lat3 = int(input('Latura 3 este:'))
t1 = Triangle(lat1,lat2,lat3)
t1.describe()
print(f'Perimetrul triunghiului este {t1.get_perimeter()}')
print(f'Semiperimetrul triunghiului este {t1.get_semi_perimeter()}')
print(f'Aria triunghiului este {t1.get_area()}')
print()


t2 = Triangle(4,8,8)
t2.describe()
print(f'Primetrul este {t2.get_perimeter()} si aria este {t2.get_area()}')
