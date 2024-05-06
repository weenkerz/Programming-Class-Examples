import turtle as t
import random


def colour_generator() -> str:
    def char_generator() -> str:
        values = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        value = ''
        funny = random.randint(1, 10)

        if funny == 1:
            value += 'ff'
        else:
            for i in range(0, 2):
                value += random.choice(values)

        return value

    r = char_generator()
    g = char_generator()
    b = char_generator()
    hex_code = f'#{r}{g}{b}'

    return hex_code


def screen_startup(w, h):
    t.Screen()
    t.setup(w, h)
    t.bgcolor('#ffffff')
    t.title('Dot placer guy thing (idk)')
    t.penup()
    t.pensize(5)
    t.pencolor('#000000')
    t.hideturtle()
    t.speed(20)
    t.tracer(False)


def grid_drawer():
    t.penup()
    for i in range(min_x + border, max_x - border + 1, cell_dim):
        t.penup()
        t.goto(i, min_y + border)
        t.pendown()
        t.goto(i, max_y - border)

    t.penup()
    for i in range(min_y + border, max_y - border + 1, cell_dim):
        t.penup()
        t.goto(min_x + border, i)
        t.pendown()
        t.goto(max_x - border, i)


def place_dot(row, column, colour):
    t.up()
    x_pos = min_x + border + cell_dim/2 + (cell_dim * (column-1))
    y_pos = max_y - border - cell_dim/2 - (cell_dim * (row-1))

    t.goto(x_pos, y_pos)
    t.dot(cell_dim, colour)


def draw_turtle():
    t.tracer(False)
    # Feets
    place_dot(4, 3, 'lightgreen')
    place_dot(4, 9, 'lightgreen')
    place_dot(8, 9, 'lightgreen')
    place_dot(8, 3, 'lightgreen')

    # Shell
    for i in range(5, 8):
        place_dot(3, i, 'darkgreen')
        place_dot(9, i, 'darkgreen')
    for i in range(4, 9):
        place_dot(i, 4, 'darkgreen')
        place_dot(i, 8, 'darkgreen')
    for i in range(4, 9):
        for j in range(5, 8):
            place_dot(i, j, 'yellowgreen')

    # Head and Tail
    place_dot(1, 6, 'lightgreen')
    for i in range(5, 8):
        place_dot(2, i, 'lightgreen')
    place_dot(10, 6, 'lightgreen')
    place_dot(11, 6, 'lightgreen')


# Parameters
columns = 11
rows = 11
cell_dim = 50
border = 20
num_of_dots = 2_718

# Window stuff
width = columns * cell_dim + (2 * border)
height = rows * cell_dim + (2 * border)

# Min's and Max's
min_x = - width // 2
max_x = width // 2
min_y = - height // 2
max_y = height // 2

screen_startup(width, height)
grid_drawer()

# Demo 1
# draw_turtle()

# Demo 2
# for i in range(num_of_dots):
#     t.tracer(True)
#     place_dot(random.randint(1, rows), random.randint(1, columns), colour_generator())

t.done()
