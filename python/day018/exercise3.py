from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.color("red")
turtle.shape("circle")

# Challenge 3: drawing different forms
lines = 3
line_length = 100
is_drawing = True


def get_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r, g, b)


def drew_a_shape(num_lines):
    angle = 360 / num_lines
    for _ in range(num_lines):
        turtle.forward(line_length)
        turtle.left(angle)


for _ in range(10):
    get_random_color()
    drew_a_shape(lines)
    lines += 1

screen = Screen()
screen.exitonclick()
