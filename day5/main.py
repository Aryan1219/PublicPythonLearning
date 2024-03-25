from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
left_paddle = Paddle("left")
right_paddle = Paddle("right")
screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")


screen.exitonclick()
