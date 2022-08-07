import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []
for _ in range(20):
    car = CarManager()
    cars.append(car)

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 260:
        scoreboard.win()
        player.reset()

screen.exitonclick()
