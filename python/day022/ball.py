from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed('slow')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        pos_x = self.xcor()
        pos_y = self.ycor()
        self.goto(pos_x + self.x_move, pos_y + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
