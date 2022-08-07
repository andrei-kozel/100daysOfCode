from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(COLORS))
        self.shapesize(1, 2)
        self.random_position()

    def random_position(self):
        pos_x = randint(-300, 300)
        pos_y = randint(-240, 260)
        self.goto(pos_x, pos_y)

    def move(self):
        if self.xcor() <= -280:
            self.goto(300, self.ycor())
        else:
            self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())
