from turtle import Turtle, Screen
import random


t = Turtle()


# challenge 3

sides = 3

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

for num in range(3, 11):
    t.pencolor(random.choice(colours))
    for num in range(0, sides):
        t.forward(100)
        t.right(360 / sides)
    sides += 1


screen = Screen()


screen.exitonclick()
