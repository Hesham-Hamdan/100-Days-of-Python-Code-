from turtle import Turtle, Screen
import random


t = Turtle()
# t.shape("turtle")


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

# for num in range(3, 11):
#     t.pencolor(random.choice(colours))
#     for num in range(0, sides):
#         t.forward(100)
#         t.right(360 / sides)
#     sides += 1


# challenge 4


angles = [0, 90, 180, 270, 360]
t.speed("fastest")
for num in range(0, 100):
    t.pencolor(random.choice(colours))
    t.right(random.choice(angles))
    t.forward(20)
    t.pensize(t.pensize() + 0.1)


screen = Screen()


screen.exitonclick()
