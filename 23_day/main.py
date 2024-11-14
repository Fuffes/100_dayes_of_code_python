import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    screen.listen()

    screen.onkey(player.move, "Up")
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.is_the_edge_reached():
        score.level_up()
        score.update_score()
        player.take_start_position()
        car_manager.level_up()


screen.exitonclick()