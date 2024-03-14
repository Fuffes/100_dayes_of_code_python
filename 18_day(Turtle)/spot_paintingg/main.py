from turtle import Turtle, Screen
import random


# 10x10
# dots_wight = 20
# gaps = 50


timmy = Turtle()
# timmy.color("red")
# timmy.pensize(20)

screen = Screen()
screen.exitonclick()
# screen.colormode(255)

def random_color():
    color_bank = [(232, 254, 243), (253, 234, 245), (43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107)]
    color = random.choice(color_bank)
    return color


# r = (43, 2, 176)

def draw_line():
    timmy.dot(20)
    timmy.forward(50)
    timmy.dot(20)

draw_line()

