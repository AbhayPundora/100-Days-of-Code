import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

y_axis = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for i in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -230, y = y_axis[i])
    turtles.append(new_turtle)



if user_bet:
    is_race_on = True

# print(turtles)

while is_race_on:
    for turtle in turtles:
        if  turtle.xcor() < 230:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
        else:
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"you won! The {winner} turtle is the winner!")
            else:
                print(f"you lose! The {winner} turtle is the winner!")
            is_race_on = False







































screen.exitonclick()