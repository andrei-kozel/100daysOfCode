from turtle import Turtle, Screen
from random import choice, random

turtle = Turtle()
turtle.pensize(10)
turtle.speed("fast")


# Challenge 4: random walk
def get_random_color():
    r = random()
    g = random()
    b = random()
    turtle.color(r, g, b)


for _ in range(100):
    get_random_color()
    turtle.left(choice([0, 90, 180, 270]))
    turtle.forward(20)

screen = Screen()
screen.exitonclick()
