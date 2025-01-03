from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.move_x = 10
        self.move_y = 10
        self.goto(0,0)
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
        # todo: basically have to define the equation deciding the motion of the ball so that it move as wanted with
        # this function in while loop so that screen will also keep updating. i.e. this problem is also solves , only
        # problem is this function which basically will define the motion of the ball

    def bounce_y(self):
        self.move_y *= -1
        self.move_speed *= 0.9
    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        time.sleep(0.1)
        self.bounce_x()