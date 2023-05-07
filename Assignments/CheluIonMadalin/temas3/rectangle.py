class Rectangle:
    def __init__(self, latime, lungime, culoare):
        self.latime = latime
        self.lungime = lungime
        self.culoare = culoare

    def describe(self):
        print(f'Dreptunghiul meu este de culoarea  {self.culoare}, are lungimea laturii de {self.lungime} Metri si latimea laturii de {self.latime} Metri')
    def get_area(self):
        print('Aria dreptunghiului meu este de', self.latime * self.lungime, 'Metri')

    def get_perimeter(self):
        print(f'Perimetrul dreptunghiului meu {self.culoare} este de {2*(self.latime+self.lungime)} Metri')

rectangle1 = Rectangle(6, 8 , 'Albastru')
rectangle1.describe()
rectangle1.get_area()
rectangle1.get_perimeter()
print('*' * 60)
rectangle2 = Rectangle(9, 7 , 'Rosu')
rectangle2.describe()
rectangle2.get_area()
rectangle2.get_perimeter()
