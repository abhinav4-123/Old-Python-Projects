import turtle

import colorgram
from turtle import Turtle,Screen
import random
turtle.colormode(255)
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = [] # will get colors sorted based upon their frequencies
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list=[ (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]
def random_color():
        return random.choice(color_list)

# todo: paint 10X10 dots , spaced by 50 , and each dot is 10 in diameter
t = Turtle()
t.speed("fastest")
# for _ in range(5):
#     t.fillcolor(random_color())
#     t.begin_fill()
#     t.circle(5)
#     t.end_fill()
#     t.penup()
#     for __ in range(9):
#
#         t.forward(50)
#         t.pendown()
#         t.fillcolor(random_color())
#         t.begin_fill()
#         t.circle(5)
#         t.end_fill()
#         t.penup()
#
#
#     t.left(90)
#     t.forward(50)
#     t.left(90)
#     t.fillcolor(random_color())
#     t.begin_fill()
#     t.circle(5)
#     t.end_fill()
#     t.penup()
#     for __ in range(9):
#
#         t.forward(50)
#         t.pendown()
#         t.fillcolor(random_color())
#         t.begin_fill()
#         t.circle(5)
#         t.end_fill()
#         t.penup()
#
#     t.right(90)
#     t.forward(50)
#     t.right(90)
t.penup()
t.ht()
t.setheading(225) # for changing initial coordinates for the wanted pattern
# , angle anticlockwise this basically will set heading of the turtle. i.e. in which direction it will move from here is decided by
t.forward(300)
t.setheading(0)
number_of_dots = 100
# t.pendown()
for dot_count in range(1, number_of_dots + 1):
    # t.pendown()
    t.dot(20,random_color()) # actually there is no need of pendown
    # t.penup()
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



screen = Screen()
screen.exitonclick()