from turtle import Turtle

FONT = ("courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = self.get_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.speed("fastest")
        self.print_score()

    def get_highscore(self) -> int:
        with open("highscore.txt", "r") as file:
            value = file.read()
        return int(value)

    def update_highscore(self, value):
        with open("highscore.txt", "w") as file:
            file.write(str(value))

    def print_score(self):
        self.clear()
        self.write(
            arg=f"SCORE: {self.score}  HIGHSCORE : {self.get_highscore()}",
            align=ALIGNMENT,
            font=FONT,
        )

    def update(self):
        self.score += 1
        self.print_score()

    def reset(self):
        if self.score > self.get_highscore():
            self.update_highscore(self.score)
        self.score = -1
        self.update()

    # def game_over(self):
    #     self.home()
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
