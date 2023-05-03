class Triangle:
    def __init__(self, latura1, latura2, baza, culoare):
         self.latura1 = latura1
         self.latura2 = latura2
         self.culoare = culoare
         self.baza = baza

    def get_perimeter(self):
        return self.latura1 + self.latura2 + self.baza

    def get_semiperimeter(self):
        return (self.latura1 + self.latura2 + self.baza) * 0.5
    def describe(self):
        return self.culoare

t1 = Triangle(2, 3, 4 , 'Galben')
print(f'Eu sunt primul triunghi de culoare {t1.culoare}, am latura1 {t1.latura1}, latura2 {t1.latura2} ,baza{t1.baza}  cu perimetrul {t1.get_perimeter()} si semiperimetrul {t1.get_semiperimeter()}')

