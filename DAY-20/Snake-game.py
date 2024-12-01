from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

level = [0.3, 0.2, 0.1]
is_game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
player_input = screen.textinput(title="My Snake Game", prompt="Input your level: Easy, Medium, Hard").lower()
print(player_input)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

if player_input == "easy":
    new_level = level[0]
elif player_input == "medium":
    new_level = level[1]
elif player_input == "hard":
    new_level = level[2]
else:
    is_game_on = False
    scoreboard.input()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while is_game_on:
    screen.update()
    time.sleep(new_level)

    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Collision with wall
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 270) or (snake.head.ycor() < -280):
        is_game_on = False
        scoreboard.game_over()

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
