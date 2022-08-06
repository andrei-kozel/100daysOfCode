from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

player = Paddle(-350)
ai = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    ai.move_ball_cap(ball.ycor())

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(ai) < 50 and ball.xcor() > 320 or ball.distance(player) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player_win()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.ai_win()

screen.exitonclick()
