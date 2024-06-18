from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
initial_speed = 0.1  # Initial sleep time
speed_increment = 0.01  # Amount to decrease sleep time each cycle
min_speed = 0.02  # Minimum sleep time

while game_is_on:
    screen.update()
    time.sleep(initial_speed)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        initial_speed -= speed_increment
        if initial_speed < min_speed:
            initial_speed = min_speed

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        initial_speed -= speed_increment
        if initial_speed < min_speed:
            initial_speed = min_speed

screen.mainloop()