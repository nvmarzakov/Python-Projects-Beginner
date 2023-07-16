from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.new_apple()
        snake.extend()
        scoreboard.increase_score()

    # Detect collusion with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collusion with tail
    for segment in snake.snake_body[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()





