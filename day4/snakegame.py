import time
from turtle import Turtle, Screen


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
startingpositions = [(0,0),(-20,0),(-40,0)]
screen.tracer(0)

bodyparts = []
for pos in range(len(startingpositions)) :
    bodyparts.append(Turtle(shape="square"))
    bodyparts[pos].color("yellow")
    bodyparts[pos].penup()
    bodyparts[pos].goto(startingpositions[pos])

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for part in range(len(bodyparts) -1, 0,-1):
        next_x = bodyparts[part-1].xcor()
        next_y = bodyparts[part-1].ycor()
        bodyparts[part].goto(next_x,next_y)
    bodyparts[0].forward(20)


screen.exitonclick()