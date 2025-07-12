from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#
# snake = Turtle("square")
# snake2 = Turtle("square")
# snake3 = Turtle("square")
#
# snake.color("white")
# snake2.color("white")
# snake3.color("white")
#
#
# snake2.goto(-20,0)
# snake3.goto(-40,0)


snake = Snake()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update() #we move those 3 segment by for loop and then only in the next iteration we can see them
    time.sleep(0.1)
    snake.move()


screen.exitonclick()