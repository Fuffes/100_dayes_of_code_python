import random
from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_c = (r, g, b)
    print(type(r_c))
    return r_c


# TODO 1
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# TODO 2
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# TODO 3
# ANGLE = 360
#
#
# def draw_n_angle(sides):
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(ANGLE/sides)
#
#
# for _ in range(3, 11):
#     timmy.color(choice(COLOR_BANK))
#     draw_n_angle(_)

# TODO 4
# def random_color():
#     timmy.pensize(10)
#     timmy.color()
#
# def random_direction():
#     directions = [0, 90, 180, 270]
#     timmy.setheading(choice(directions))
#     timmy.forward(30)
#
#
# for _ in range(200):
#     random_color()
#     random_direction()


# TODO 5
# timmy.color("deep pink")
# timmy.pensize(10)
#
# timmy.setheading(45)
# timmy.forward(30)
#
# timmy.setheading(0)
# timmy.forward(30)
#
# timmy.setheading(-45)
# timmy.forward(30)
#
# timmy.setheading(-90)
# timmy.forward(30)
#
# timmy.setheading(-140)
# timmy.forward(90)
#
# timmy.setheading(140)
# timmy.forward(90)
#
# timmy.setheading(90)
# timmy.forward(30)
#
# timmy.setheading(45)
# timmy.forward(30)
#
# timmy.setheading(0)
# timmy.forward(30)
#
# timmy.setheading(-45)
# timmy.forward(30)
#

#TODO 6
tilt = 0
timmy.speed("fastest")

def spirograph(size_of_tilt):
    for _ in range(int(360 / size_of_tilt)):
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_tilt)
        timmy.circle(100)

spirograph(10)


screen = Screen()
screen.exitonclick()