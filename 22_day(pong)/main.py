import time
from turtle import Screen
from paddle import Paddle
from pong import Pong
from score import Score

RIGHT_START_POSITION = (350, 0)
LEFT_START_POSITION = (-350, 0)


screen = Screen()

screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(False)


r_paddle = Paddle(RIGHT_START_POSITION)
l_paddle = Paddle(LEFT_START_POSITION)
pong = Pong()
score = Score()

screen.listen()
screen.onkey(r_paddle.down, "Down")
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "w")

game_is_on = True

speed = 0.1
while game_is_on:
    time.sleep(pong.pong_speed)
    screen.update()
    pong.move()

    #bounce
    if pong.ycor() > 300 or pong.ycor() < -300:
        pong.bounce_y()

    #collision
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()

    if pong.xcor() > 380:
        pong.reset_position()
        score.l_point()

    if pong.xcor() < -380:
        pong.reset_position()
        score.r_point()

screen.exitonclick()