from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
Move_forward = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            timmy = Turtle(shape="square")
            timmy.penup()
            timmy.goto(position)
            timmy.color("white")
            self.all_turtles.append(timmy)

    def move(self):
        for segment in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[segment - 1].xcor()
            new_y = self.all_turtles[segment - 1].ycor()
            self.all_turtles[segment].goto(new_x, new_y)
        self.head.forward(Move_forward)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
