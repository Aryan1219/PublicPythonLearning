import random
from turtle import Turtle

SPEED = 1
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.from_direction = None
        self.start()
        self.penup()
        self.color("white")
        self.speed(SPEED)
        self.shape("circle")

    def start(self):
        self.from_direction = random.choice([0, 180])
        self.setheading(self.from_direction)

    def bounce_right(self):
        self.setheading(random.randrange(315, 405))

    def bounce_left(self):
        self.setheading(random.randrange(135, 225))

    def bounce_towards_right_up(self):
        self.setheading(random.randrange(30, 60))

    def bounce_towards_left_up(self):
        self.setheading(random.randrange(110, 140))

    def bounce_towards_right_down(self):
        self.setheading(random.randrange(300, 330))

    def bounce_towards_left_down(self):
        self.setheading(random.randrange(210, 240))

    def move(self):
        self.forward(20)

    def got_hit_from(self, paddle):
        if paddle == "left":
            self.from_direction = "left"
        elif paddle == "right":
            self.from_direction = "right"

    def restart(self):
        self.hideturtle()
        self.home()
        self.showturtle()
        self.start()
