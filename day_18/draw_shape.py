
from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green", "red")
timmy_the_turtle.penup()
timmy_the_turtle.goto(-50,500)
timmy_the_turtle.pendown()
timmy_the_turtle.speed(0)

for turns in range(3,33):
    timmy_the_turtle.pencolor(randint(1,255),randint(1,255),randint(1,255))
    turn_degree = 360/turns
    for i in range(turns):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(turn_degree)



screen.exitonclick()