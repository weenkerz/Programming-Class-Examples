import turtle
import itertools
import math
import random
import time


def colour_combiner() -> str:
    def colour_generator() -> str:
        values = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        value = ''
        funny = random.randint(0, 9)

        if funny == 0:
            value += 'ff'
        else:
            for i in range(2):
                value += random.choice(values)

        return value

    r = colour_generator()
    g = colour_generator()
    b = colour_generator()
    hex_code = f'#{r}{g}{b}'

    return hex_code


class SolarSystemBody(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1

    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity

        # Scale objects to visible size
        self.display_size = max(math.log(self.mass, self.display_log_base), self.min_display_size)

        self.up()
        self.hideturtle()

        if not isinstance(self, Moon):
            solar_system.add_body(self)

    def draw(self):
        if not isinstance(self, Moon):
            self.clear()
            self.dot(self.display_size)

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])


class Sun(SolarSystemBody):
    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.color('Yellow')


class Planet(SolarSystemBody):
    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.moons = []
        self.solar_system = solar_system
        self.color(colour_combiner())

    def moon_combiner(self, moon):
        self.moons.append(moon)

    def moon_positions(self):
        for i in self.moons:
            i.time += 0.01
            i.setposition(
                self.xcor() + (i.radius * math.cos(i.time * i.random)),
                self.ycor() + (i.radius * math.sin(i.time * i.random)))

            i.clear()
            if i.real:
                i.dot(i.size)


class Moon(Planet):
    colours = itertools.cycle(['white', 'grey', 'lightgrey'])

    def __init__(self, planet, size, distance):
        super().__init__(planet.solar_system, mass=1, velocity=(0, 0))
        self.color(next(Moon.colours))
        self.random = random.randint(1, 5)
        self.size = size
        self.time = 0
        self.radius = distance
        self.real = True

        planet.moon_combiner(self)


def moon_removal(body):
    if isinstance(body, Planet):
        for moon in body.moons:
            if moon in body.moons:
                moon.real = False


class SolarSystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor('black')
        self.solar_system.title('Solar System')

        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        body.clear()
        if body in self.bodies:
            self.bodies.remove(body)

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()

            if isinstance(body, Planet):
                for j in body.moons:
                    j.move()
                    j.draw()

        self.solar_system.update()

    def calculate_all(self):
        bodies_copy = self.bodies.copy()
        for i, j in enumerate(bodies_copy):
            for k in bodies_copy[i + 1:]:
                self.check_collision(j, k)
                self.acceleration_due_to_gravity(j, k)

        for i in bodies_copy:
            if isinstance(i, Planet):
                i.moon_positions()

    @staticmethod
    def acceleration_due_to_gravity(body1: SolarSystemBody, body2: SolarSystemBody):
        force = (body1.mass * body2.mass) / (body1.distance(body2) ** 2)
        angle = body1.towards(body2)
        reverse = 1

        for body in body1, body2:
            acceleration = force / body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))

            body.velocity = (body.velocity[0] + (reverse * acc_x), body.velocity[1] + (reverse * acc_y))
            reverse = -1

    def check_collision(self, first, second):
        if first.distance(second) < first.display_size / 2 + second.display_size / 2:
            for body in first, second:
                if isinstance(body, Planet):
                    moon_removal(body)
                    self.remove_body(body)

#
# if __name__ == '__main__':
#     planets = []
#
#     solar_system = SolarSystem(width=900, height=600)
#     sun = Sun(solar_system, mass=1_000, position=(0, 0))
#
#     for i in range(5):
#         position = (
#             random.randint(-solar_system.width / 2, solar_system.width / 2),
#             random.randint(-solar_system.height / 2, solar_system.height / 2)
#         )
#         velocity = (
#             random.randint(-5, 5),
#             random.randint(-5, 5)
#         )
#         planet = Planet(solar_system, mass=(random.randint(1, 10)), position=position, velocity=velocity)
#         planets.append(planet)
#
#     for j in range(10):
#         planet = random.choice(planets)
#
#         moon = Moon(planet, random.randint(3, 8), random.randint(15, 40))
#
#     while True:
#         solar_system.calculate_all()
#         solar_system.update_all()
#
#         time.sleep(1 / 120)
#
# turtle.done()
