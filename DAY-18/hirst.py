import random
import colorgram
import turtle as t

t.colormode(255)
screen = t.Screen()
# screen.bgcolor("black")

color_list = [(227, 230, 236), (243, 236, 242), (244, 239, 226), (235, 243, 239), (194, 166, 108), (135, 167, 193),
(49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165),
(69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135),
(120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182), (181, 100, 88), (22, 92, 65),
(68, 152, 169), (210, 177, 202), (88, 77, 15)]

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

tim.setheading(140)
tim.forward(400)
tim.setheading(0)

number_of_dots = 811

for dot_num in range(1, number_of_dots + 1):
    tim.dot(10, random.choice(color_list))
    tim.forward(20)

    if dot_num % 30 == 0:
        tim.setheading(270)
        tim.forward(20)
        tim.setheading(180)
        tim.forward(600)
        tim.setheading(0)

screen.exitonclick()
