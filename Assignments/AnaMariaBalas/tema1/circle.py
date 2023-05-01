import math

pi = math.pi
print(f'Valoarea lui pi: {pi} ')

class Circle:

    def __init__(self, r, color):  #r - raza cercului
        self.r = r
        self.color = color

    def get_area(self): # Aria cercului
        return int(pi * (self.r * self.r))

    def describe(self):
        print('*' * 15, f'Descriere cerc', '*' * 15)
        print(f'culoare: {self.color} si raza: {self.r}')


cerc1 = Circle(7, 'Rosie')
cerc1.describe()
print(f'Eu sunt primul cerc, am raza {cerc1.r}, cu aria {cerc1.get_area()} si culoarea {cerc1.color}')

cerc2 = Circle(5.3, 'Albastru')
cerc2.describe()
print(f'Eu sunt al doilea cerc, am raza {cerc2.r}, cu aria {cerc2.get_area()} si culoarea {cerc2.color}')
