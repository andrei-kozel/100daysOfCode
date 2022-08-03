import colorgram
from turtle import Turtle, Screen
from random import choice

# screen setup
screen = Screen()
screen.colormode(255)

# turtle setup
turtle = Turtle()
turtle.shape("circle")
turtle.pensize(1)
turtle.speed("fast")

board_side_size = 700
rgb_colors = []
dots_per_side = 20
dot_size = 20
gap = board_side_size / (dots_per_side - 2)
row_number = 0

start_x = -board_side_size / 2
start_y = -board_side_size / 2

# generate colors palette
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

turtle.up()
turtle.goto(start_x, start_y)

while row_number != dots_per_side:
    for _ in range(dots_per_side):
        for _ in range(dots_per_side):
            turtle.color(choice(rgb_colors))
            start_x += gap
            turtle.goto(start_x, start_y)
            turtle.dot(dot_size)
        start_y += gap
        start_x = -board_side_size / 2
        row_number += 1

screen.exitonclick()
