from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # new_car.setheading(180)
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

        # while(new_car.xcor() > -340):
        #     new_car.forward(STARTING_MOVE_DISTANCE)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT

        # for car in self.all_cars:
        #     car.clear()
        # above three lines were for giving realistic touch of starting of a level



