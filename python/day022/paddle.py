from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.generate_paddle(x_position)
        self.move_up = True

    def generate_paddle(self, x_position):
        self.shape("square")
        self.speed("fastest")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")
        self.goto(x_position, 0)

    def up(self):
        if self.ycor() <= 220:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() >= -220:
            self.goto(self.xcor(), self.ycor() - 20)

    def auto_move(self):
        pos_y = self.ycor()
        if self.move_up:
            if pos_y == 220:
                self.move_up = False
            self.up()
        elif not self.move_up:
            if pos_y == -220:
                self.move_up = True
            self.down()

    def move_ball_cap(self, pos_y):
        self.goto(self.xcor(), pos_y)