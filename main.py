import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        self.player = Player()
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()

    def key_listen(self):
        self.screen.listen()
        self.screen.onkey(self.player.go_up, "Up")

    def run(self):
        game_is_on = True
        while game_is_on:
            time.sleep(0.1)
            self.screen.update()
            self.key_listen()
            self.car_manager.create_car()
            self.car_manager.move_cars()

            # Detect collision with car
            for car in self.car_manager.all_cars:
                if car.distance(self.player) < 20:
                    game_is_on = False
                    self.scoreboard.game_over()

            # Detect successful crossing
            if self.player.is_at_finish_line():
                self.player.go_to_start()
                self.car_manager.level_up()
                self.scoreboard.increase_level()


if __name__ == '__main__':
    game = Game()
    game.run()
    game.screen.exitonclick()
