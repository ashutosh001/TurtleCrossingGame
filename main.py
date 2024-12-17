import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
screen.onkey(player.move,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()

    #Detect collision of turtle with the car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    #Detect if turtle reaches the finishing line
    if player.race_finish():
        car_manager.level += 1
        scoreboard.write_level(car_manager.level)

screen.exitonclick()


