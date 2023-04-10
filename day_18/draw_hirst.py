from turtle import Turtle, Screen
from random import randint
import sys
import colorgram
"""

rgb_colors = []
colors = colorgram.extract('hirst_dots.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
print(rgb_colors)
"""

rgb_colors = [(233, 239, 246),(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

screen = Screen()
screen.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color(0,0,0)
timmy_the_turtle.speed(0)
timmy_the_turtle.penup()

def hirst(size):

    timmy_the_turtle.goto(-500,-500)
    step = 1000//size

    for col in range(size+1):
        for row in range(size):
            color_index = randint(0,len(rgb_colors)-1)
            timmy_the_turtle.color(rgb_colors[color_index])
            timmy_the_turtle.stamp()
            timmy_the_turtle.fd(step)
        timmy_the_turtle.setx(-500)
        timmy_the_turtle.left(90)
        timmy_the_turtle.fd(step)
        timmy_the_turtle.right(90)
    screen.exitonclick()


hirst(20)