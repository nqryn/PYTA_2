
class Triangle:

    def __init__(self, nume, l1, l2, l3, culoare):
        self.nume = nume
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.culoare = culoare

    def get_perimeter(self):
        return self.l1 + self.l2 + self.l3

    def describe(self):
        print('*' * 2, f'Informatii {self.nume}', '*' * 2)
        print(f'culoare: {self.culoare} , latura 1: {self.l1}, latura 2: {self.l2}, latura 3: {self.l3}')

    def add_triunghi(self, nume, l1, l2, l3, culoare):
        self.nume = nume
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.culoare = culoare

triunghi = Triangle('triunghi1', 6, 7, 12, 'Roz')
triunghi.describe()
print(f'Eu sunt primul triunghi si am perimetrul {triunghi.get_perimeter()}')
triunghi.add_triunghi('triunghi2', 10, 20, 25, 'Verde')
triunghi.describe()
print(f'Eu sunt al doilea triunghi si am perimetrul {triunghi.get_perimeter()}')