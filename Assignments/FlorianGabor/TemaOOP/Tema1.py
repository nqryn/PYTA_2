# TEMA PENTRU ACASA:
# - clase pentru urmatoarele: Circle (cerc), Rectangle (dreptunghi) si Triangle (triunghi)
# - fiecare clasa va avea pe langa atributele evidente (geometrice) si un atribut de culoare optional,
#   iar ca metode, se vor cele geometrice care au sens, plus o metoda de describe.
# - din fiecare clasa, va rog sa faceti 1-3 obiecte cu care sa va jucati

class Circle:
    make = "Compas"
    color = None
    def __init__(self, radius, color="Gray"):
        self.radius = radius
        self.color = color

    def description1(self):
        print(f"Cerc cu raza : {self.radius} . Culoarea {self.color}")

    def description2(self):
        print(f"{'=' * 20} Cerc {self.color} {'=' * 20}")
        print(f"Raza = {self.radius}")

    def get_area(self):
        PI = 3.14
        return PI * self.radius**2
    def get_color(self):
        return self.color

    def get_perimeter(self):
        return 2 * PI * self.radius

    def get_diameter(self):
        return 2 * self.radius

# M-am "jucat" putin cu crearea de obiecte

radius = int(input("Raza cercului este radius = "))
color = input("Tastati o culoare pentru cerc = ")

circle0 = Circle(radius, color)
circle0.description2()
print(circle0)

circle1 = Circle(5, "Red")
circle2 = Circle(2, "Blue")
circle3 = Circle(3, "Green")
circle4 = Circle(6, "Yellow")
circle5 = Circle(4, "Pink")
print(circle1.make)

list1 =[circle1.color, circle2.color, circle3.color, circle4.color, circle5.color]
print(f"Lista de culori pentru cercuri este: {list1}")
print(f'list1 = {list1}')
list1.sort()
print(f"list1 = {list1}")
list2 = [circle1.get_color(), circle2.get_color()]
print(f"list2 = {list2}")

circle1.description2()
circle2.description2()
circle3.description2()
circle4.description2()
circle5.description2()
print()

print('*' * 70)

print(f"Diametrul cercului3 este : {circle3.get_diameter()}")
print(f"Aria cercului2 este : {circle2.get_area()}")
print(f"Culoare cercului5 este {circle5.get_color()}")

2.Exercitiul_2
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().

class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def description(self):
        print(f"{'<' * 20} Dreptunghi {self.color} {'>' * 20}" )
        print(f"Lungime latura = {self.length}")
        print(f"Latime latura = {self.width}")

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_color(self):
        return self.color

    def get_diagonal(self):
        return (self.length**2 + self.width**2)**0.5

    def get_change_color(self):
        self.color = "Violet"


rectangle1 = Rectangle(5, 4, "Red")
rectangle2 = Rectangle(3, 2, "Pink")
rectangle3 = Rectangle(1, 4, "Blue")
rectangle4 = Rectangle(4, 6, "Gray")

print(f"Aria pentru dreptinghi1 este: {rectangle1.get_area()}")
print(f"Perimetrul pentru dreptunghi2 este: {rectangle1.get_perimeter()}")
print(f"Culoare pentru dreptunghi3 este: {rectangle3.get_color()}")
print(f"Diagonala pentru dreptunghi4 este: {rectangle4.get_diagonal()}")
rectangle2.get_change_color()
print()
rectangle2.description()
print()