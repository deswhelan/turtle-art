import colorgram
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

donatello = Turtle()
donatello.speed(250)
donatello.penup()

screen = Screen()
screen.screensize(2000, 2000)

def get_colour_palette():
    colour_palette = []
    colors = colorgram.extract('img_2.png', 15)
    for color in colors:
        colour_palette.append(color.rgb)
    return colour_palette

def print_row_of_dots(dot_size, step_size, row_length, colour_palette):
    for _ in range(row_length):
        donatello.dot(dot_size, random.choice(colour_palette))
        donatello.fd(step_size)

def paint_dot_painting(dot_size, gap_size, row_count, column_count):
    step_size = dot_size + gap_size

    # offset position of first dot so that painting is centred on screen
    dot_1_x_pos = -(((column_count / 2) * step_size) - (step_size / 2))
    dot_1_y_pos = -(((row_count / 2) * step_size) - (step_size / 2))
    donatello.setpos(dot_1_x_pos, dot_1_y_pos)

    colour_palette = get_colour_palette()

    for row_number in range(row_count):
        print_row_of_dots(dot_size, step_size, column_count, colour_palette)
        donatello.setpos(dot_1_x_pos, (dot_1_y_pos + (step_size * (row_number + 1))))

    donatello.home()
    donatello.hideturtle()

paint_dot_painting(20, 50, 10, 10)

screen.exitonclick()
