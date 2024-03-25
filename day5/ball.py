import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(random.choice([0, 180]))
        self.speed("fast")
        self.shape("circle")

    def bounce_right(self):
        self.setheading(random.randrange(315, 405))

    def bounce_left(self):
        self.setheading(random.randrange(135, 225))

    def move(self):
        self.forward(20)
