import turtle
import pandas

IMAGE = "blank_states_img.gif"

turtle.screensize(canvwidth=725, canvheight=491)
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

states_guessed = 0
data = pandas.read_csv("50_states.csv")

while states_guessed <= 50:
    answer_state = screen.textinput(title=f"{states_guessed}/50 States Correct", prompt="What's another state's name?")
    row = data[data.state == answer_state.capitalize()]
    if not row.empty:
        states_guessed += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(row.x), int(row.y))
        t.write(str(row.state.item()))

screen.exitonclick()
