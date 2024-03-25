from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.direction = direction
        self.hideturtle()
        self.penup()
        self.shapesize(1, 3)
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        if self.direction == "left":
            self.goto(-350, 0)
            self.setheading(90)
            self.showturtle()

        elif self.direction == "right":
            self.goto(350, 0)
            self.setheading(90)
            self.showturtle()

    def move_up(self):
        if 360 > self.ycor():
            self.forward(20)

    def move_down(self):
        if self.ycor() > -360:
            self.backward(20)

    def restart(self):
        if self.direction == "left":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)
