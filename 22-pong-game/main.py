from turtle import  Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()



    #detect if the ball miss

    if ball.xcor() > 410 :
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()


























screen.exitonclick()