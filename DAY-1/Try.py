from turtle import Turtle, Screen

movement = [100, 10, 100, 10]
positions = [90, 180, 270, 270]



screen = Screen()
tim = Turtle()
# tim.hideturtle()
tim.speed("slowest")
tim.fillcolor("red")
tim.begin_fill()
for num in range(4):
    tim.forward(movement[num])
    tim.setheading(positions[num])
tim.end_fill()

tim.penup()
tim.color("black")
tim.goto(x=40, y=45)
tim.forward(50)
tim.fillcolor("yellow")
tim.begin_fill()
tim.pendown()
tim.circle(10)
tim.end_fill()

tim.penup()
tim.color("black")
tim.goto(x=95, y=10)
tim.setheading(45)
tim.fillcolor("blue")
tim.begin_fill()
tim.pendown()

def head(size):
    while 180/size:
        tim.circle(50)
        # for _ in range(180/size):
        #     tim.circle(50)

head(5)

tim.end_fill()






screen.exitonclick()