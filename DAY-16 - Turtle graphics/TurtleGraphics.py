# from turtle import Turtle, Screen
# brainy = Turtle()
# # print(brainy)
# brainy.shape("turtle")
# brainy.color("red")
# brainy.forward(200)
# # brainy.left(90)
# # brainy.forward(100)
# # brainy.left(90)
# # brainy.forward(100)
# # brainy.left(90)
# # brainy.forward(100)

# Attributes
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)



# from turtle import *
#
# bgcolor('black')
# speed(0.1)
# hideturtle()
# for i in range(120):
#     color('red')
#     circle(i)
#     color('orange')
#     circle(i * 0.8)
#     right(90)
#     forward(3)
# done()