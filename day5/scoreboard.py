from turtle import Turtle

FONT = ("Arial", 32, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 350)
        self.score_left = 0
        self.score_right = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(
            arg=f"{self.score_left} : {self.score_right}", align="center", font=FONT
        )

    def increase_right_score(self):
        self.score_right += 1

    def increase_left_score(self):
        self.score_left += 1

    def game_over(self):
        self.home()
        self.write("Game Over!", align="center", font=FONT)
