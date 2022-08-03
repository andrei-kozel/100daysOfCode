from turtle import Turtle, Screen

turtle = Turtle()
turtle.color("red")

# challenge 2: drew a dashed line
for _ in range(15):
    turtle.forward(10)
    turtle.up()
    turtle.forward(10)
    turtle.down()

screen = Screen()
screen.exitonclick()
