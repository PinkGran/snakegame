from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segment = []
        self.create_snake()  #mention the variables and methods you want to make and run when class is defined here
        self.head = self.snake_segment[0]
    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        a = Turtle("square")  # Creating a turtle
        a.color("pink")
        a.penup()
        a.goto(positions)
        self.snake_segment.append(a)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.snake_segment[-1].position())
    def move(self):
        for square_num in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[square_num - 1].xcor()
            new_y = self.snake_segment[square_num - 1].ycor()
            self.snake_segment[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            #heading_of_snake = self.snake_segment[0].heading()
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


