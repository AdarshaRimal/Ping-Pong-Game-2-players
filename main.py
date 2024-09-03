from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
game_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Ping Pong")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #Up and Down wall collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #collision with paddle

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    #left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    #right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
screen.exitonclick()
