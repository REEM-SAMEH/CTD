from turtle import  *
import random

speed(5)
bgcolor("black")
colors = ['teal', 'navy','turquoise','cyan','blue']
pensize(5)
 
for i in range (8):
    left(45)
    for i in range (8):
        color(random.choice(colors))
        forward(100)
        left(45)


hideturtle()