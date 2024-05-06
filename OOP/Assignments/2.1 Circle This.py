from math import pi


class Circle:
    def __init__(self, radius, height):
        self.height = height
        self.radius = radius

    def get_cylinder_v(self):
        return (self.radius ** 2) * pi * self.height

    def get_cylinder_sa(self):
        return 2 * pi * ((self.radius ** 2) + self.radius * self.height)

    def get_cone_v(self):
        return pi * (self.radius**2) * self.height / 3

    def get_cone_sa(self):
        return pi * (self.radius**2 + self.radius * ((self.height**2 + self.radius**2) ** 0.5))

    def get_torus_sa(self, ring_radius):
        return 4 * (pi**2) * ring_radius * self.radius


r = int(input("What is the radius of the circle? "))
h = int(input("What is the height of the cylinder/cone? "))
R = int(input("What is R for the torus? "))

circle = Circle(r, h)

print(f"\nCylinder Volume: {round(circle.get_cylinder_v(), 2)}")
print(f"Cylinder SA: {round(circle.get_cylinder_sa(), 2)}")
print(f"Cone Volume: {round(circle.get_cone_v(), 2)}")
print(f"Cone SA: {round(circle.get_cone_sa(), 2)}")
print(f"Torus SA: {round(circle.get_torus_sa(R), 2)}")