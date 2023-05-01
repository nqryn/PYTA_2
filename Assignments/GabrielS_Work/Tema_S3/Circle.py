class Circle:

    def __init__(self, d, r, pi, colour, description):
        self.d = d
        self.r = r
        self.pi = pi
        self.colour = colour
        self.description = description

    def get_area(self):
        return self.pi * (self.r * self.r)

    def get_perimeter(self):
        return (2 * self.pi) * self.r

    def get_colour(self):
       return (self.colour)

    def get_definition(self):
        return (self.description)

c1 = Circle(15, 4, 9.18, "Rosu", "Medie")
print(f"Primul cerc cu Diametrul de {c1.d}mm, Raza de {c1.r}mm, cu Aria de {c1.get_area()}mm2, si Perimetru de {c1.get_perimeter()}mm in Culoarea {c1.colour} si are Dimensiune {c1.get_definition()}.")
