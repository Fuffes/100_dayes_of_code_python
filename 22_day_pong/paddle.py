from turtle import Turtle

MOVIENG_DISTANSE = 20


class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(start_position)
        self.speed("fastest")

    def down(self):
        new_y = self.ycor() - MOVIENG_DISTANSE
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + MOVIENG_DISTANSE
        self.goto(self.xcor(), new_y)