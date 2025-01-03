# so, this is the lecture file of day 19
# more turtle graphics, even listeners, state and multiple instances of an object
# will use this to make games: etch a sketch, turtle racing game (make your bet, random pace ) , etc
import turtle
# first of all we need to take input from users in order to use that in our programs
# there is  a bunch of functions in python turtle documentation for this purpose: Using screen events
# turtle.listen()

# from turtle import Turtle, Screen
# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
# def clear():
#     tim.clear() # clears all drawings done by this particular turtle
#     tim.penup()
#     tim.home() # to reach at initial position
#     tim.pendown()
# screen.listen()
# # .onkey
# screen.onkey(key='w', fun=move_forwards) # parenthesis not needed here
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key='a', fun=turn_left)
# screen.onkey(key='d', fun=turn_right)
# screen.onkey(key='c', fun=clear)
# # tim.stamp() # leaves a sign of turtle at home position
# # tim.clearstamp()
# # tim.undo()
# screen.exitonclick()


# FUNCTIONS as INPUT
# when this is done, function is passed without parenthesis at end
# the function which takes function as input is called HIGHER ORDER FUNCTION
# it is used pretty commonly in python
# for using such functions, use keyword arguments in order to avoid any error(S)
# project 18, day19: Etch a Sketch
# TODO: W key for forward, S: back, A: counter-clockwise, D: clockwise(right), C: clear drawing and turtle in center
# done

# project 19, day 19 : Turtle Race
# what if we need more turtles?
# we can, using different names
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will winn the race? Enter a color: ")  # we can
# also take input in python turtle
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


# timmy_1 = Turtle(shape='turtle')  # basically using init method of turtle class
# timmy_1.color(color[0])
# timmy_1.penup()  # turtle will move itself and we're never gonna move the turtle
# timmy_1.goto(x=-230, y=80)  # goto is used to go to a particular x and y
y_position = [-80, -40, 0, 40, 80, 120]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True  # so that it does not start prematurely

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()  # basically it returns pencolor and fill color both or holds them both
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


# timmy = Turtle()  # these both are different instances , means they both will work independently of each other
# tim.color = 'green'  # state of tim's color attribute is green
# timmy.color = 'purple'  # state of timmy's color attribute is purple
# # they have different states in terms of their color or attribute
# # they can also have different states in terms of what they are doing at the instant
# # i.e. we can have different turtle objects that cna participate in race and run independently of each other


screen.exitonclick()

# todo: open a dialog and ask user to chose his/her color of turtle
# todo: once okay, the turtles should assemble in their start position
# todo: race should start
# todo: as soon as any of the turtles reach the finish line, the race should stop
# todo: prompt in python shell should tell whether the user won the race or lose it

# learnt using turtle coordinate system, now can use x and y coordinate
# also we have got a little bit used to this coordinate system
# also can think certain things like if a turtle is 40px wide, then we need to subtract half of the width from the
# coordinates of the edges in order to make it reach the end actually
# play with these coordinates, size of screen, and size of turtle


# so, we have also learnt creating multiple object using same class
# also seen that different objects with same classes are different instances, and they can act independently
# this capability of creating different objects which can behave differently and independently and that's why oop is so
# powerful. Will see this concept of multiple instances with different states as we'll move further


# we can expand our past projects now or any other project which have been understood, and you are comfortable.
# it may need some googling, research, or you may also understand that I need something more to learn to be capable of
# doing this thing
