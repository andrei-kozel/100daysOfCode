from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start_position = 100

for index in range(6):
    timmy = Turtle(shape="turtle")
    timmy.up()
    timmy.color(colors[index])
    timmy.goto(-230, start_position)
    start_position -= 40
    turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print("You win")
            else:
                print(f"You lost. Thi winner is {winner}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
