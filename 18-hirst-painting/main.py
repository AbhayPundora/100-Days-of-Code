import random
from turtle import Turtle, Screen

import colorgram
import random


screen = Screen()
colors = colorgram.extract('hirst_painting.jpg', 30)

screen.colormode(255)


rgb_list = [(202, 164, 189),(238, 248, 245),(158, 75, 49),(10, 162, 119), (170, 82, 52), (214, 77, 157), (189, 34, 164), (216, 63, 79), (131, 202, 186), (211, 90, 63), (41, 85, 129), (162, 63, 78), (19, 92, 52), (102, 53, 47), (219, 152, 134), (13, 81, 99), (23, 110, 60), (27, 58, 66), (235, 188, 158), (154, 220, 207), (122, 178, 186), (17, 193, 160), (75, 44, 41), (1, 121, 86), (216, 176, 182), (92, 49, 51), (69, 38, 41), (41, 145, 158)]


# rgb_list = []
#
# for color in colors:
#     rgb = color.rgb
#     hsl = color.hsl
#     proportion  = color.proportion
#     rgb_list.append((rgb.r, rgb.b, rgb.g))
#     # print(rgb, hsl, proportion)
#
#
# print(rgb_list)


# for i in range(11):
#     y = i * 50
#     x = -100
#     for _ in range(11):
#       rand_color = random.choice(rgb_list)
#       turtle = Turtle("circle")
#       turtle.color(rand_color)
#       turtle.penup()
#       turtle.goto(x , y)
#       x += 50

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")



turtle.setheading(220)
turtle.forward(300)
turtle.setheading(0)

for _ in range(10):
    for _ in range(10):
        rand_color = random.choice(rgb_list)
        turtle.penup()
        turtle.forward(50 )
        turtle.dot(20, rand_color)


    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.backward(500)





screen.exitonclick()