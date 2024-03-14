from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(500, 400)
bet = screen.textinput("Make your bet", "Which turtle will win the race. Enter color...")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


y = -50
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-240, y=y)
    y += 25
    all_turtles.append(turtle)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()