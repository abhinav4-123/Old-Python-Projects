from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)
import time

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_is_on = True
while (game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with upper and lower wall
    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

    # detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if ball.xcor() > 388 or ball.xcor() < -388:
    #     ball.move_x *= -1

    # detect if R paddle misses (both separately in order to count scores)
    if ball.xcor() > 350 :
        ball.reset_position()
        scoreboard.l_point()

    # detect if L paddle misses
    if ball.xcor() < -350 :
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()