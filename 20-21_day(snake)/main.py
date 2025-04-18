from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()

"""seting up the screen"""
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""game"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    #collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_game()
        snake.reset_snake_position()

    #collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset_game()
            snake.reset_snake_position()












screen.exitonclick()