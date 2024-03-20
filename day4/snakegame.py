import time
from turtle import Screen
from snake import Snake


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.5)
    snake.move()


screen.exitonclick()
