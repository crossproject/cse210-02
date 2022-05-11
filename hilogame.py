import random
from game.player import Player


class Dealer:
    def __init__(self):
        self.playing = True
        self.player = Player()

    def input(self):
        self.player.get_card_number()

    def start_game(self):
        # if we are playing we need to get stuff
        while self.playing:
            self.out_puts()
            self.input()
            self.updates()
            self.keep()

    def updates(self):
        return self.player.points_calculation()

    def out_puts(self):

        self.player.get_card_number()
        print(f"\nThis card is {self.player.card_number}")

    def keep(self):
        keep = input("Keep playing? [y/n]")
        if keep == "y":
            self.playing = True
        elif keep == "n":
            self.playing = False

class Player:
    def __init__(self):
        self.card_number = 0
        self.player = 0
        self.card_number = 0
        self.score = 300

    def get_card_number(self):
        self.card_number = random.randint(1, 13)

    def points_calculation(self):
        self.get_card_number()
        card_guess = input("Higher or lower? [h/l]: ")
        second_number = random.randint(1, 13)
        if second_number >= self.card_number and card_guess == "h":
            self.score += 100
        elif second_number <= self.card_number and card_guess == "h":
            self.score -= 75
        elif second_number >= self.card_number and card_guess == "l":
            self.score -= 75
        elif second_number <= self.card_number and card_guess == "l":
            self.score += 100
        print(f"Next card was:{second_number}")
        print(f"Your score is: {self.score}")