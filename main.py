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

def print_row_of_dots(row_length, colour_palette):
    for _ in range(row_length):
        donatello.dot(20, random.choice(colour_palette))
        donatello.fd(70)

def paint_dot_painting(row_count, column_count):
    # TODO: stretch - centre the painting
    colour_palette = get_colour_palette()
    for row_number in range(row_count):
        print_row_of_dots(column_count, colour_palette)
        donatello.home()
        donatello.setpos(0, (70 * (row_number + 1)))

paint_dot_painting(10, 10)

screen.exitonclick()
