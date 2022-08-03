from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.color("red")
timmy_the_turtle.shape("circle")

# challenge 1: draw a square
for _ in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(200)

screen = Screen()
screen.exitonclick()
