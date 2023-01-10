from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_x_START = 300
CAR_WIDTH = 1
CAR_LENGTH = 2
Y_MIN = -280
Y_MAX = 280
RANDOM_INT_RANGE = (1, 6)
CAR_SHAPE = "square"
INT_TO_SPAWN_CAR = 1


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(RANDOM_INT_RANGE[0], RANDOM_INT_RANGE[1])
        if random_chance == INT_TO_SPAWN_CAR:
            car = Turtle(CAR_SHAPE)
            car.shapesize(CAR_WIDTH, CAR_LENGTH)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(CAR_x_START, random.randint(Y_MIN, Y_MAX))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



