# import colorgram


# colors = colorgram.extract("Day 18\image.jpg", 30)

# cs = []

# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     cs.append((r, g, b))

# print(cs)

from turtle import Turtle, Screen, screensize
import random
import turtle

color_list = [
    (202, 164, 110),
    (240, 245, 241),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

t = Turtle()
turtle.colormode(255)
screensize(2000, 2000)
t.speed("fastest")

for column in range(0, 10):
    t.goto(0, column * 50)
    for row in range(0, 10):
        random_color = random.choice(color_list)
        t.pendown()
        t.dot(20, random_color)
        t.penup()
        t.forward(50)

t.hideturtle()

screen = Screen()

screen.exitonclick()
