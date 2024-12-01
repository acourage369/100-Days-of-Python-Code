from turtle import Turtle, Screen
import random


my_screen = Screen()
my_screen.bgcolor("black")

brainy = Turtle()
colors = ["red", "blue", "yellow", "green", "brown", "violet", "pink", "orange"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        brainy.forward(100)
        brainy.right(angle)


for shapes_num in range(3, 10):
    brainy.color(random.choice(colors))
    draw_shape(shapes_num)

# my codes
# brainy.color("yellow")
# brainy.speed(5)
# for _ in range(3):
#     brainy.forward(100)
#     brainy.right(120)
#
#
# brainy.color("red")
# for _ in range(4):
#     brainy.forward(100)
#     brainy.right(90)
#
# brainy.color("blue")
# for _ in range(5):
#     brainy.forward(100)
#     brainy.right(72)
#
# brainy.color("orange")
# for _ in range(6):
#     brainy.forward(100)
#     brainy.right(60)
#
# brainy.color("green")
# for _ in range(8):
#     brainy.forward(100)
#     brainy.right(45)
#
# brainy.color("black")
# for _ in range(9):
#     brainy.forward(100)
#     brainy.right(40)



# tim = Turtle()
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


my_screen.exitonclick()
