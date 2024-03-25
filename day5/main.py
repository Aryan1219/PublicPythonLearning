from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")

left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    ball.move()

    if scoreboard.score_right < 3 and scoreboard.score_left < 3:
        if -400 < ball.xcor() < 400:
            if ball.distance(left_paddle) < 22:
                ball.got_hit_from("left")
                ball.bounce_right()

            if ball.distance(right_paddle) < 22:
                ball.got_hit_from("right")
                ball.bounce_left()
            if ball.ycor() < -370:
                if ball.from_direction == "left":
                    ball.bounce_towards_right_up()
                else:
                    ball.bounce_towards_left_up()

            if ball.ycor() > 370:
                if ball.from_direction == "left":
                    ball.bounce_towards_right_down()
                else:
                    ball.bounce_towards_left_down()
        else:
            if ball.from_direction == "left":
                scoreboard.increase_left_score()
                ball.restart()
                left_paddle.restart()
                right_paddle.restart()
                scoreboard.print_score()

            else:
                scoreboard.increase_right_score()
                ball.restart()
                left_paddle.restart()
                right_paddle.restart()
                scoreboard.print_score()

    else:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
