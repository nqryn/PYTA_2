class Rectangle:
    def __init__(self, l, L):
        self.l = l
        self.L = L

    def get_area(self):
        return self.l * self.L

    def get_perimeter(self):
        return 2 * self.l + self.L

Dr1 = Rectangle(6, 8)
print(f"Primul dreptunghi, cu Lungimea {Dr1.L}cm, Latimea {Dr1.l}cm cu Aria {Dr1.get_area()}cm2 si Perimetru {Dr1.get_perimeter()}cm.")
