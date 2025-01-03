# day 19, project number: 19, name: TurtleRace
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