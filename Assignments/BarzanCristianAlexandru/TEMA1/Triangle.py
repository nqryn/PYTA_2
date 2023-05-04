class Triangle:
    def __init__(self, latura1, latura2, baza, culoare):
         self.latura1 = latura1
         self.latura2 = latura2
         self.culoare = culoare
         self.baza = baza

    def get_perimeter(self):
        return self.latura1 + self.latura2 + self.baza

    def get_aria(self):
        sp = self.get_perimeter() / 2 # acesta e semiperimetrul triunghiului
        return (sp * (sp - self.latura1) * (sp - self.latura2) * (sp - self.baza)) ** 0.5
t1 = Triangle(2, 3, 4 , 'Galben')
print(f'Eu sunt primul triunghi de culoare {t1.culoare}, am latura1 {t1.latura1}, latura2 {t1.latura2} si baza {t1.baza}')
print(f'Perimetrul este {t1.get_perimeter()}')
print (f'Aria este {t1.get_aria()}')
