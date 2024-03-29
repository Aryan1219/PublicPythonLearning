from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # initializing the snake body
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):

        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_part = Turtle(shape="circle")
        new_part.color("yellow")
        new_part.penup()
        new_part.goto(pos)
        self.body_parts.append(new_part)

    def extend(self):
        self.add_segment(self.body_parts[-1].pos())

    def move(self):
        for part in range(len(self.body_parts) - 1, 0, -1):
            next_x = self.body_parts[part - 1].xcor()
            next_y = self.body_parts[part - 1].ycor()
            self.body_parts[part].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
