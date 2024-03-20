from turtle import Turtle


class Snake:

    body_parts = []

    def __init__(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in starting_positions:
            new_turtle = Turtle(shape="square")
            new_turtle.color("yellow")
            new_turtle.penup()
            new_turtle.goto(pos)
            self.body_parts.append(new_turtle)

    def move(self):
        for part in range(len(self.body_parts) - 1, 0, -1):
            next_x = self.body_parts[part - 1].xcor()
            next_y = self.body_parts[part - 1].ycor()
            self.body_parts[part].goto(next_x, next_y)
        self.body_parts[0].forward(20)
