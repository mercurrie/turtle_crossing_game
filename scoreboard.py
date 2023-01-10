from turtle import Turtle
POSITION = (-290, 260)
FONT = ("Courier", 24, "normal")
STARTING_SCORE = 0
SCOREBOARD_COLOR = "black"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = STARTING_SCORE
        self.color(SCOREBOARD_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
