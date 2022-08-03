from turtle import Turtle, Screen

turtle = Turtle()
turtle.color("red")

# challenge 1: draw a square
for _ in range(4):
    turtle.right(90)
    turtle.forward(200)

screen = Screen()
screen.exitonclick()
