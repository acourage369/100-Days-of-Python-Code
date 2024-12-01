import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
tom = Turtle()
tom.pensize(10)
tom.speed(50)

for _ in range(2000):
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
