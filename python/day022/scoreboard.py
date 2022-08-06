from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.ai_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.ai_score, align="center", font=("Courier", 80, "normal"))

    def player_win(self):
        self.player_score += 1
        self.update_scoreboard()

    def ai_win(self):
        self.ai_score += 1
        self.update_scoreboard()
