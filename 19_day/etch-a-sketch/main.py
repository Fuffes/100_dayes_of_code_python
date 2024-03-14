from turtle import Turtle, Screen


# a = counter-clockwise
# d = clockwise
# c = clear

tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(30)


def backward():
    tim.backward(30)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.reset()
    tim.pos()


screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
