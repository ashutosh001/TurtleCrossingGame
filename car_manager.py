from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.level = 1
        self.all_cars = []

    def create_car(self):
        """Creates car using turtle and adds them to a list"""
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.up()
            new_car.setheading(180)
            new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_car(self):
        """Moves the cars randomly based on the current level"""
        move = STARTING_MOVE_DISTANCE + (self.level-1)*MOVE_INCREMENT
        for car in self.all_cars:
            car.forward(move)
