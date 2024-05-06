import turtle as t
import random


def colour_generator() -> str:

    def char_generator() -> str:
        values = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        value = ''
        funny = random.randint(0, 9)

        if funny == 0:
            value += '00'
        else:
            for i in range(0, 2):
                value += random.choice(values)

        return value

    r = char_generator()
    g = char_generator()
    b = char_generator()
    hex_code = f'#{r}{g}{b}'

    return hex_code


def draw_s(size, pensize, pos, colour, angle):
    t.tracer(1)
    t.tracer(0)
    for i in range(2):
        if i == 1:
            t.right(90)
        t.penup()
        t.pencolor(colour)
        t.setpos(pos)
        t.pensize(pensize)
        t.forward(size/2)
        t.down()
        t.left(angle)
        t.forward((((size**2)+(size**2))**0.5)/2)
        t.left(angle)
        t.forward(size)
        t.left(angle)
        t.forward((((size**2)+(size**2))**0.5))
        t.left(angle*2)
        t.forward((((size**2)+(size**2))**0.5))
        t.left(angle)
        t.forward(size)
        t.left(angle)
        t.forward(((size**2)+(size**2))**0.5)
        t.right(angle)
        t.forward(size)


t.Screen()
t.title("Cool S")
t.hideturtle()
count = 0

while True:
    seg_size = random.randint(20, 50)
    s_colour = colour_generator()
    turtle_pos = (random.randint(-300, 300), random.randint(-300, 300))
    seg_wid = 5
    t.speed(20)
    s_angle = 45
    # count += 1
    # print(count)

    draw_s(seg_size, seg_wid, turtle_pos, s_colour, s_angle)
