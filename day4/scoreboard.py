from turtle import Turtle

FONT = ("courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.speed("fastest")
        self.print_score()

    def print_score(self):
        self.write(arg=f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
