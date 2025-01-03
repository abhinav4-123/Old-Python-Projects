# todo: creating paddle and making them movable(width:20, height: 100, x_pos:350, y_pos:0) up and down by 20 pixels
from turtle import Turtle
MOVEMENT = 40

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def up(self):
        new_y = self.ycor() + MOVEMENT
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVEMENT
        self.goto(self.xcor(), new_y)