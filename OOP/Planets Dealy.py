import turtle
import random
import time
from Solar_system_main_code import SolarSystem, Sun, Planet, Moon

if __name__ == '__main__':
    planets = []

    solar_system = SolarSystem(width=900, height=600)
    sun = Sun(solar_system, mass=10_000, position=(0, 0))

    for i in range(5):
        position = (
            random.randint(-solar_system.width/2, solar_system.width/2),
            random.randint(-solar_system.height/2, solar_system.height/2)
        )
        velocity = (
            random.randint(-5,5),
            random.randint(-5,5)
        )
        planet = Planet(solar_system, mass=(random.randint(10, 30)), position=position, velocity=velocity)
        planets.append(planet)

    for j in range(10):
        planet = random.choice(planets)

        moon = Moon(planet, random.randint(3, 8), random.randint(15, 40))

    while True:
        solar_system.calculate_all()
        solar_system.update_all()

        time.sleep(1/120)


turtle.done()
