from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()

        direction = direction.lower()
        if direction == "left":
            self.penup()
            self.shapesize(1, 3)
            self.shape("square")
            self.color("white")
            self.speed("fastest")
            self.goto(-350, 0)
            self.setheading(90)

        elif direction == "right":
            self.penup()
            self.shapesize(1, 3)
            self.shape("square")
            self.color("white")
            self.speed("fastest")
            self.goto(350, 0)
            self.setheading(90)

    def move_up(self):
        if 360 > self.ycor():
            self.forward(20)

    def move_down(self):
        if self.ycor() > -360:
            self.backward(20)
