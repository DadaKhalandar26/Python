#  Just run the commented code for first time to extract the colours from the image
# you have downloaded from the internet and prepare your colours_list
# import colorgram
#
# colours = colorgram.extract('Hirst_painting.jpg', 30)   # Need to give the location on images which is in jpg formate
#                                                         # and second position to define how many colours to extract
#
# rgb_colours = []
# for i in range(30):  # Need to change range according to the number of colors extracted
#     rgb_list = []
#     for _ in range(0, 3):
#         rgb_list.append(colours[i].rgb[_])
#     rgb_colours.append(tuple(rgb_list))
#
# print(rgb_colours)

import random
import turtle
turtle.colormode(255)


def random_colours():
    return random.choice(colours_list)


colours_list = [(250, 248, 242), (252, 248, 250), (244, 251, 248), (244, 247, 251), (205, 160, 107),
                (230, 212, 103), (147, 78, 40), (79, 28, 18), (136, 30, 18), (185, 157, 23), (14, 51, 75),
                (36, 95, 132), (235, 174, 158), (49, 121, 77), (198, 153, 156), (196, 95, 80), (115, 162, 185),
                (13, 99, 71), (59, 20, 24), (80, 82, 25), (139, 168, 152), (178, 206, 170), (38, 54, 45), (137, 23, 29),
                (236, 212, 8), (78, 149, 164), (131, 68, 71), (5, 82, 113), (102, 143, 123), (227, 178, 182)]

my_turtle = turtle.Turtle()


my_turtle.shape("circle")
my_turtle.pensize(20)
my_turtle.hideturtle()


y = -100
for _ in range(10):
    x = -100
    for i in range(10):
        my_turtle.penup()
        my_turtle.color(random_colours())
        my_turtle.setposition(x, y)
        my_turtle.stamp()
        x += 50
    y += 50


screen = turtle.Screen()
screen.screensize(2000, 1500)
screen.exitonclick()
