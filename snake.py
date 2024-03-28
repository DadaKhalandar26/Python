from turtle import Turtle
Move_forward = 20


class Snake:

    def __init__(self):
        self.all_turtles = []
        x_con = 0
        for turtles in range(3):
            timmy = Turtle(shape="square")
            timmy.penup()
            timmy.goto(x_con, y=0)
            timmy.color("white")
            self.all_turtles.append(timmy)
            x_con -= 20

    def move(self):
        for segment in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[segment - 1].xcor()
            new_y = self.all_turtles[segment - 1].ycor()
            self.all_turtles[segment].goto(new_x, new_y)
        self.all_turtles[0].forward(Move_forward)

    def up(self):
        self.all_turtles[0].setheading(90)

    def down(self):
        self.all_turtles[0].setheading(270)

    def left(self):
        self.all_turtles[0].setheading(180)

    def right(self):
        self.all_turtles[0].setheading(0)
