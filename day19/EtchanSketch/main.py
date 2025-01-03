# project number: 18, day:19, name: Etch a Sketch
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear() # clears all drawings done by this particular turtle
    tim.penup()
    tim.home() # to reach at initial position
    tim.pendown()
screen.listen()
# .onkey
screen.onkey(key='w', fun=move_forwards) # parenthesis not needed here
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
# tim.stamp() # leaves a sign of turtle at home position
# tim.clearstamp()
# tim.undo()
screen.exitonclick()