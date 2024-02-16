from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi*(self.radius**2)

    def get_circumference(self):
        return 2*pi*self.radius


circle = Circle(int(input("What is the radius of the circle: ")))

print(f'The area of the circle is {round(circle.get_area(), 2)}')
print(f'The circumference of the circle is {round(circle.get_circumference(), 2)}')
