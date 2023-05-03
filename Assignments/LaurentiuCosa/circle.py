import math

class Circle:

    def __init__(self, r, name, colour):
        self.r = r
        self.colour = colour
        self.name = name

    def get_area(self):
        return self.r ** 2 * math.pi

    def get_primeter(self):
        return 2 * self.r * math.pi

    def describe(self):
        print(f"{self.name} are raza {self.r}, aria {round(self.get_area(),2)}, perimetrul {round(self.get_primeter(),2)} si culoarea {self.colour}")


c1 = Circle(9, "Cercul 1", "Rosu")

# print(f"sunt cerc cu raza {c1.r}, am aria {round(c1.get_area(),2)} si perimetrul {round(c1.get_primeter(),2)}")

c2 = Circle(13, "Cercul 2", "Negru")

# print(f"nu sunt cerc cu raza {c2.r}, am aria {round(c2.get_area(),2)} si perimetrul {round(c2.get_primeter(),2)}")

c1.describe()
c2.describe()