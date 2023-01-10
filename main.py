import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FINISH_LINE = 280
CAR_COLLISION = 20
SLEEP_TIME = 0.1
SCREEN_TITLE = "Turtle Crossing"
UP_ARROW = "Up"
RIGHT_ARROW = "Right"
LEFT_ARROW = "Left"
ANIMATION_OFF = 0


def play_game():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(SCREEN_TITLE)
    screen.tracer(ANIMATION_OFF)

    turtle = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(turtle.go_up, UP_ARROW)
    screen.onkey(turtle.go_left, LEFT_ARROW)
    screen.onkey(turtle.go_right, RIGHT_ARROW)

    game_is_on = True
    while game_is_on:
        time.sleep(SLEEP_TIME)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # detect finish
        if turtle.ycor() > FINISH_LINE:
            turtle.reset()
            scoreboard.increase_score()
            car_manager.increase_speed()

        # detect collision
        for car in car_manager.all_cars:
            if car.distance(turtle) < CAR_COLLISION:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    play_game()