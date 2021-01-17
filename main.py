from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.bgcolor('black')
sc.setup(900, 600)
sc.title('PONG')
sc.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(r_paddle.up, "Up")
sc.onkey(l_paddle.up, "w")
sc.onkey(r_paddle.down, "Down")
sc.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    # Right Paddle Missing
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_point()

    # Left Paddle Missing
    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_point()

sc.exitonclick()
