from random import randint
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()

cars = []

for num in range(0, 25):
    car = CarManager()
    cars.append(car)


screen.onkey(key="Up", fun=player.up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()
        if car.xcor() < -350:
            car.goto(randint(310, 400), randint(-250, 250))


screen.exitonclick()
