from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = randint(1,6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.car_speed = 0.1
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            rand_y = randint(-240, 240)
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        [car.backward(self.car_speed) for car in self.all_cars]
        # for car in self.all_cars:
        #     car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



