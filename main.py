from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
food = Food()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.calculate_score()
        snake.increase_snake_size()

    # Detect collision with wall and tail
    if snake.detect_collision():
        scoreboard.game_over()
        game_is_on = False
screen.exitonclick()
