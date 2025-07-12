import turtle
from itertools import count
from turtle import Turtle, Screen
import  random

timmy = Turtle()
# timmy.shape("circle")
# timmy.color("red")
# timmy.shape("arrow")

# for _ in range(4):
#     timmy.forward(200)
#     timmy.right(90)

# for _ in range(50):
#     timmy.pencolor("black")
#     timmy.forward(10)
#     timmy.pencolor("white")
#     timmy.forward(10)

# for _ in range(50):
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)

# timmy.forward(100)
# timmy.right(60)

# for _ in range(4):
#     timmy.right()
#     timmy.forward(100)

good_colors = [
    "crimson",
    "dodgerblue",
    "mediumseagreen",
    "goldenrod",
    "orchid",
    "tomato",
    "turquoise",
    "deepskyblue",
    "salmon",
    "limegreen",
    "hotpink",
    "steelblue",
    "coral",
    "slateblue",
    "lightcoral",
    "mediumvioletred",
    "teal",
    "khaki",
    "sienna",
    "plum"
]


# challenge --- 1

i = 3
colors = ["red", "blue", "green", "yellow", "cyan"]

while i < 8:
    for _ in range(i):
        timmy.forward(100)
        timmy.right(360 / i)

    timmy.pencolor(random.choice(colors))

    i += 1

# challenge --- 2

def move(r_angle):
    random.choice([timmy.right(r_angle), timmy.left(r_angle)])


angles = [0, 90, 180, 270]

for _ in range(100):
    timmy.forward(10)
    angle = random.choice(angles)
    move(angle)
    timmy.forward(10)
    random.choice(good_colors)

# angles = [0, 90, 180, 270]



turtle.colormode(255)
#
def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    return (r, g, b)
#
#
# for _ in range(200):
#     turtle.speed("fastest")
#     turtle.pensize(10)
#     turtle.color(random_color())
#     turtle.forward(30)
#     turtle.setheading(random.choice(angles))


# timmy.pencolor(random_color())

#challenge --- 3





turtle.speed("fastest")

for _ in range(100):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)

















screen  = Screen()
screen.exitonclick()