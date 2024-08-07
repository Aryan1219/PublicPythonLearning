import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.update()
        snake.extend()
    if (
        snake.head.xcor() < -295
        or snake.head.xcor() > 295
        or snake.head.ycor() < -295
        or snake.head.ycor() > 295
    ):
        scoreboard.reset()
        snake.reset_snake()

    for part in snake.body_parts[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset_snake()
screen.exitonclick()
