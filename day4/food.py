from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        random_x = randint(-250, 250)
        random_y = randint(-250, 250)
        self.goto(random_x, random_y)

