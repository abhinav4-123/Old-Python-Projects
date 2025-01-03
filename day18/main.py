# this is day 18
# todo: turtle graphics , tuples, importing modules in python
# damien hirst kinda things , using python turtle ,(beautiful dotted art piece)
import turtle
import random
# turtle with paintbrush at back;
# can take help of turtle graphics documentation available at python org,
# or simply you can use stackoverflow  i.e. need google to achieve certain things

from turtle import Turtle, Screen

turtle.colormode(255)

new_turtle = Turtle()
# new_turtle.shape("turtle")  # will set the shape to turtle or other available
# new_turtle.color(
#     'olive drab')  # these colors can be defined using tkinter (used to create GUI), before which we had text interface like our python console

# tkinter is on which turtle module relies for creating graphics
# colors: https://cs111.wellesley.edu/reference/colors
# colors: https://trinket.io/docs/colors
# here we will learn reading and using documentation while learning python turtle


# new_turtle.forward(100)
# new_turtle.right(90)
# new_turtle.forward(100)
# new_turtle.right(90)
# new_turtle.forward(100)
# new_turtle.right(90)
# new_turtle.forward(100)
# new_turtle.right(90)

# # challenge 1: draw a square
#
# for _ in range(4):
#     new_turtle.forward(100)
#     new_turtle.left(90)


# # bhasad
# for _ in range(10):
#     new_turtle.forward(115)
#     new_turtle.right(90)
#     new_turtle.forward(100)
#     new_turtle.right(90)
#     new_turtle.forward(100)
#     new_turtle.right(90)
#     new_turtle.forward(15)
#     new_turtle.forward(100)
#     new_turtle.right(90)


# # all ways we can import modules:
#
# # import turtle #i.e. import module name
# # then turtle.Class(), etc
# from module import class
# # this is important if you want to use some particular classes
#
# # advanced 2nd way
# # from turtle import *
# # but then it has some disadvantages
# # e.g.
# from random import *
# # now if we will write choice , it will identify it as method , but from which module it is , this is the problem with this method
# # so, this is less expressive actually
#
# # method 3
# # we can import a module with an alias name
# # we can use it for the modules having large names:
# # e.g.
# import turtle as t
#
# # method 4 : for the modules which are not available basically : so it is installing module actually
# # e.g.
# # import heroes
# # the reason is turtle is available in the standard python library which contains very small number of packages and modules
# # so, basically we can install the modules according to our need from internet
# # basically pycharm gives advice and prompt to install the package
# import heroes
# print(heroes.gen())


# # turtle challenge 2: draw dashed line
# for _ in range(25):
#     new_turtle.forward(7)
#     new_turtle.penup()
#     new_turtle.forward(6)
#     new_turtle.pendown()
# or maybe could have changed the pencolor to white in between


# # turtle challenge 3: drawing triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon ,
# # all with different colors and side 100
# # angle= 360/5
#
# turtle.colormode(255)
# def change_color():
#     r = random.randrange(0, 257, 10)
#     g = random.randrange(0, 257, 10)
#     b = random.randrange(0, 257, 10)
#     new_turtle.color((r,g,b))
#
# for sides in range(3, 11):
#     for i in range(sides):
#         angle1 = 360/sides
#         new_turtle.right(angle1)
#         new_turtle.forward(100)
#     change_color()

# color= ['medium aquamarine', 'chocolate', 'dark slate blue', 'red', 'gold', 'spring green', 'dark slate gray', 'maroon']
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         new_turtle.right(angle)
#         new_turtle.forward(100)
#
# for side in range(3,11):
#     new_turtle.color(random.choice(color))
#     draw_shape(side)


# # turtle challenge 4: Random walk (can model various real life things)
# # todo: can move in any of the four direction after every 10 steps
# # todo: changes color for every 10 steps
# # todo: increase thickness of paintbrush (4 pts ig)
# # todo: also, speed up the turtle
#
# color = ['blue2', 'brown', 'aquamarine', 'BlueViolet', 'Red', 'DarkGreen', 'cyan1', 'DeepPink', 'DarkSlateBlue',
#          'gray0']
#
#
# # def move_random():
# #     brush_color = random.choice(color)
# #     while new_turtle.color() == brush_color:
# #         brush_color = random.choice(color)
# #     new_turtle.color(brush_color)
# #     random_choice = random.randint(1,4)
# #     if(random_choice == 1):
# #         new_turtle.left(90)
# #     elif( random_choice == 2):
# #         new_turtle.right(90)
# #     elif( random_choice == 3):
# #         new_turtle.right(180)
# #     else:
# #         pass
# #     new_turtle.forward(30)
#
# #
# # new_turtle.width(10)
# # turtle.speed(10)
# # for _ in range(100):
# #    move_random()

# # directions =[0,90,180,270]
# # new_turtle.pensize(15)
# # new_turtle.speed("fastest")
# # for _ in range(200):
# #     new_turtle.color(random.choice(color))
# #
# #     new_turtle.forward(30)
# #     new_turtle.setheading(random.choice(directions))


# # how to generate random RGB colors
# # python tuples: (23,31,213) (like list, but it is like stone carved, i.e.: immutable )
# # why using this then?? when we want to use list which cannot be changed in any case .
# # converting tuple to list: list(my_tuple)
# # color is defined by a tuple
# # rgb(r,g,b) values differ from 0 to 255 and their combination creating colors
# # turtle.colormode(255) # basically changing colormode
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_clr = (r,g,b)
#     return random_clr
#
#
# directions =[0,90,180,270]
# new_turtle.pensize(15)
# new_turtle.speed("fastest")
# for _ in range(200):
#     new_turtle.color(random_color())
#
#     new_turtle.forward(30)
#     new_turtle.setheading(random.choice(directions))

# Challenge 5: Make a spirograph
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_clr = (r,g,b)
#     return random_clr
#
#
# # # todo: draw circles with radius 100
# t = Turtle()
# t.pensize(1)
# t.speed('fastest')
# # # todo: use random color for each circle
# #
# #
# # # todo: how repeatedly circles can be drawn
# # for angle in range(0,360,4):
# #     t.seth(angle) # it basically changes the face of the turtle pointer by angle
# #     t.color(random_color())
# #     # t.heading() # basically it will give the current x and y coordinates
# #     t.circle(100) # we basically can draw circle using this method
# # def draw_spirograph(size_of_gap):
# #
# #     for _ in range(int(360/size_of_gap)):
# #         t.color(random_color())
# #         t.circle(100)
# #         t.setheading(t.heading() + size_of_gap)
# #
# # draw_spirograph(5)

# # this at the bottom because we want to make it happen at last
# screen = Screen()
# screen.exitonclick()


# Now there is project day 18 : Project 17: The Hirst Painting Project.
# file is in the separate folder

# colorgram: module that is used to extract colors from the images
# colorgram.extract(images, number of colors)