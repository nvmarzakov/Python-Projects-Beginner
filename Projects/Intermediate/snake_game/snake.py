from turtle import Turtle


class Snake:
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.snake_body = []
        self.create_snake_body()
        self.head = self.snake_body[0]

    def create_snake_body(self):

        for position in self.STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_new_part = Turtle("square")
        snake_new_part.color("green")
        snake_new_part.penup()
        snake_new_part.goto(position)
        self.snake_body.append(snake_new_part)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake_body()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

        self.head.forward(self.MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def move_down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def move_left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def move_right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

