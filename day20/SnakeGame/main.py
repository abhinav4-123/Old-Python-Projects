# file day 20
# project number:20, day:20, name: Snake Game
# day 20 goals
# todo: create the snake
# todo: move the snake
# todo: control the snake

import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()

# screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


# so this prev code will basically keep hold of movement of snake and except this for movement, we just have to move the
# first segment in a direction to allow rest to move behind it and ultimately causing snake to bend
# also see, how we are using this concept of stopping the cursor and then updating the screen according to our needs
# in order to make it look like it's happening in real as if it was like a snake game

screen.exitonclick()
# from turtle import Turtle, Screen
#
# snake = Turtle(shape='turtle')
# snake.color('red')
# snake.width(10)
# snake.speed('slowest')
#
#
# def turn_left():
#     snake.left(90)
#
#
# def turn_right():
#     snake.right(90)
#
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title('My Snake Game')
# snake.penup()
# # snake.setx(-280)
# # snake.sety(-280)
# isTrue = True
# while (isTrue):
#     screen.onkey(key='a', fun=turn_left)
#     screen.onkey(key='d', fun=turn_right)
#     while(isTrue):
#         snake.forward(10)
#         if (snake.xcor() > 272 or snake.xcor() < -272 or snake.ycor() > 280 or snake.ycor() < -280):
#             isTrue = False
#
# snake.forward(20)
# if (not isTrue):
#     print("You lose!. \nYour final score is {score}.")
#
# screen.exitonclick()


# see things like that update thing, time thing
# will see next things in day21
# also, focus on understanding the things and not on memorizing. You can google things if forgot.
# we even forget some game complex key combinations. So its normal.
