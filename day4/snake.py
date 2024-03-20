from turtle import Turtle


class Snake:
    bodyparts = []

    def __init__(self):

        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in starting_positions:

            new_part = Turtle(shape="square")
            new_part.color("yellow")
            new_part.penup()
            new_part.goto(pos)
            self.bodyparts.append(new_part)

    def move(self):
        for part in range(len(self.bodyparts) - 1, 0, -1):
            next_x = self.bodyparts[part - 1].xcor()
            next_y = self.bodyparts[part - 1].ycor()
            self.bodyparts[part].goto(next_x, next_y)
        self.bodyparts[0].forward(20)
