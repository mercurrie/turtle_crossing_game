from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90
EAST = 0
WEST = 180


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.reset()

    def go_up(self):
        self.setheading(NORTH)
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_right(self):
        self.setheading(EAST)
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def go_left(self):
        self.setheading(WEST)
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def reset(self):
        self.goto(STARTING_POSITION)
