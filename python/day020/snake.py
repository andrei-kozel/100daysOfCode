from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.length = 3
        self.snake = []
        self.generate_snake()
        self.head = self.snake[0]

    def generate_snake(self):
        pos_x = 0
        for index in range(self.length):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(pos_x, 0)
            self.snake.append(segment)
            pos_x -= 20

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
