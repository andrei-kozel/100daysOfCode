from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
turtle.pensize(1)
turtle.speed("fastest")
angle = 0
screen = Screen()
screen.colormode(255)


# Challenge 4: random walk
def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        turtle.color(get_random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap_size)


draw_spirograph(5)

screen.exitonclick()
