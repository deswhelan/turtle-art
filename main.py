import turtle
from turtle import Screen, Turtle
import random

donatello = Turtle()
screen = Screen()
turtle.colormode(255)

donatello.shape("turtle")
donatello.color("purple")
donatello.speed(50)

def randomise_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    donatello.color(r, g, b)

def draw_square_with_stamps():
    for _ in range(4):
        donatello.dot()
        donatello.fd(100)
        donatello.left(90)

def draw_dashed_line():
    for _ in range(15):
        donatello.fd(10)
        donatello.penup()
        donatello.fd(10)
        donatello.pendown()

def draw_polygons(min_sides_count, max_sides_count):
    polygon_sides_count = min_sides_count

    while polygon_sides_count <= max_sides_count:
        randomise_color()
        turn_angle = 180 - (((polygon_sides_count - 2) * 180) / polygon_sides_count)
        for _ in range(polygon_sides_count):
            donatello.fd(50)
            donatello.right(turn_angle)
        polygon_sides_count += 1

def random_walk():
    donatello.pensize(10)
    turn_count = random.randint(1, 100)

    for _ in range(turn_count):
        randomise_color()
        donatello.right(random.randint(0, 360))
        donatello.fd(random.randint(1, 100))

def draw_spirograph():
    for _ in range (0, 36):
        randomise_color()
        donatello.right(10)
        donatello.circle(75)

# draw_square_with_stamps()
# draw_dashed_line()
# draw_polygons(3, 10)
# random_walk()
draw_spirograph()
screen.exitonclick()