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
scoreboard = Scoreboard()
screen.listen()

cars = []

for num in range(0, 25):
    car = CarManager()
    cars.append(car)


screen.onkey(key="Up", fun=player.up)

level = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()
        if car.xcor() < -350:
            car.goto(randint(310, 400), randint(-250, 250))
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        level += 1
        scoreboard.update_score(level)
        player.reset()
        for car in cars:
            car.increase_speed()


screen.exitonclick()
