from turtle import Turtle
import time


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setpos(0, 0)
        self.speed()
        # self.setheading(45)
        self.x_move = 10
        self.y_move = 10
        self.pong_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # self.setheading(-self.heading())
        self.y_move *= -1

    def bounce_x(self):
        # self.setheading(s)
        self.x_move *= -1
        self.pong_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.pong_speed = 0.1

