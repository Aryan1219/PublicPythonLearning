from turtle import Turtle, Screen, resetscreen


t = Turtle()
scr = Screen()


def move_fwd():
    t.forward(10)


def move_bkwd():
    t.backward(10)


def move_right():
    t.right(10)


def move_left():
    t.left(10)


def clearscr():
    resetscreen()


scr.listen()

scr.onkey(move_fwd, "w")
scr.onkey(move_bkwd, "s")
scr.onkey(move_left, "a")
scr.onkey(move_right, "d")
scr.onkey(clearscr, "c")


scr.exitonclick()
