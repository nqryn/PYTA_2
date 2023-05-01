
class Rectangle:

    def __init__(self, nume, lungime, latime, culoare):
        self.nume = nume
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def get_area(self): # Aria
        return self.lungime * self.latime

    def describe(self):
        print('*' * 10, f'Informatii {self.nume}', '*' * 10)
        print(f'culoare: {self.culoare} , lungime: {self.lungime}, latime: {self.latime}')

    def add_dreptunghi(self, nume, lungime, latime, culoare):
        self.nume = nume
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare


dreptunghi = Rectangle('dreptunghi1', 6, 7, 'Rosu')
dreptunghi.describe()
print(f'Eu sunt primul dreptunghi si am aria {dreptunghi.get_area()}')
dreptunghi.add_dreptunghi('dreptunghi2', 10, 20, 'Verde')
dreptunghi.describe()
print(f'Eu sunt al doilea dreptunghi si am aria {dreptunghi.get_area()}')