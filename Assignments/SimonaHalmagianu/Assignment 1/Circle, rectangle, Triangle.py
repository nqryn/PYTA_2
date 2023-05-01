class Circle:
    def __init__(self, r, color=None):
        self.r = r
        self.color = color
    def get_area(self):
        return 3.14 * self.r ** 2
    def get_circumference(self):
        return 2 * 3.14 * self.r
    def describe(self):
        return self.color
circle1 = Circle(5)
print(f'Eu sunt primul cerc de culoare {circle1.color}, am raza {circle1.r},'
      f' cu aria {circle1.get_area()} si circumferinta {circle1.get_circumference()}')
circle2 = Circle(3, "albastra")
print(f'Eu sunt al doilea cerc de culoare {circle2.color}, am raza {circle2.r},'
      f' cu aria {circle2.get_area()} si circumferinta {circle2.get_circumference()}')

class Rectangle:
    def __init__(self, l, L, color=None):
        self.l = l
        self.L = L
        self.color = color
    def get_area(self):
        return self.l * self.L
    def get_perimeter(self):
        return 2 * (self.l + self.L)
    def describe(self):
        return self.color
rectangle1 = Rectangle(2, 5)
print(f'Eu sunt primul dreptunghi de culoare {rectangle1.color}, am perimetrul {rectangle1.get_perimeter()}'
      f' si aria {rectangle1.get_area()}')
rectangle2 = Rectangle(2, 8, "rosie")
print(f'Eu sunt al doilea dreptunghi de culoare {rectangle2.color}, am perimetrul {rectangle2.get_perimeter()}'
      f' si aria {rectangle2.get_area()}')

class Triangle:
    def __init__(self, l1, l2, base, h, color=None):
        self.l1 = l1
        self.l2 = l2
        self.base = base
        self.h = h
        self.color = color
    def get_perimeter(self):
        return self.l1 + self.l2 + self.base
    def get_area(self):
        return 0.5 * self.base * self.h
    def describe(self):
        return self.color
triangle1 = Triangle(2, 2, 4, 2)
print(f'Eu sunt primul triunghi de culoare {triangle1.color}, am perimetrul {triangle1.get_perimeter()}'
       f' si aria {triangle1.get_area()}')
triangle2 = Triangle(5, 2, 3, 4, "verde")
print(f'Eu sunt al doilea triunghi de culoare {triangle2.color}, am perimetrul {triangle2.get_perimeter()}'
       f' si aria {triangle2.get_area()}')