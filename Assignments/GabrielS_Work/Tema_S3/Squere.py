class Squere:
    def __init__(self, l):
        self.l = l

    def get_area(self):
        return self.l * self.l

    def get_perimeter(self):
        return self.l * 4

s1 = Squere(12)
print(f"Primul patrat, cu Latura {s1.l}cm, cu Aria {s1.get_area()}cm2 si Perimetru {s1.get_perimeter()}cm.")
