import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FINISH_LINE = 280
CAR_COLLISION = 20


def play_game():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    turtle = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(turtle.go_up, "Up")
    screen.onkey(turtle.go_left, "Left")
    screen.onkey(turtle.go_right, "Right")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
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