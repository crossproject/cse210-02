#from game.player import Player
import random

# Main execution control
class Game_logic():
    """
    Control the game sequence of play.
    Attr.
        is_playing = [Boolean] Maintain loop
        first_card = [Int] First Card
        new_card = [Int] Second Card
        card_evaluation = [String] Helps to compare the player desition.
        player = [Class instance] Save a Player class instance
    """
    def __init__(self):
        self.is_playing = True
        self.first_card = 0
        self.new_card = 0
        self.card_evaluation = None
        self.player = Player()

    def start_game(self):
        """
        Execute the game main loop.
        """
        while self.is_playing:
            print()
            self.get_new_cards()
            print(f"The card is: {self.first_card}")
            self.do_evaluation()
            print(f"Next card was: {self.new_card}")
            print(f"Your score is: {self.player.score}")
            self.is_playing = self.get_input()
            self.restart_values()

    def get_new_cards(self):
        """
        Load two cards and compare if the second
        is higher or lower.
        """
        # Ensure the cards are different
        while self.first_card == self.new_card:
            self.first_card = random.randint(1,13)        
            self.new_card = random.randint(1,13)
        
        # Compare if the second card is higher or lower
        if self.first_card > self.new_card:
            self.card_evaluation = "l"
        else:
            self.card_evaluation = "h"

    def do_evaluation(self):
        """
        Compares if the player desition is equal or
        different from the get_new_card method
        comparison.
        """
        option = self.player.player_card_option()
        if self.card_evaluation == option:
            self.player.up_score()
        else:
            self.player.down_score()

    def get_input(self):
        """
        Ask the user if want to keep playing.
        Return: Boolean
        """
        option = self.player.player_continue_option()
        return option == "y"

    def restart_values(self):
        """
        Restart the card and comparison values.
        """
        self.first_card = 0
        self.new_card = 0
        self.card_evaluation = None


# Player class
class Player():
    """
    Keep the score value and control the player input.
    """
    def __init__(self):
        self.score = 300

    def player_card_option(self):
        """
        Main question.
        Return: String
        """
        return input("Higher or lower? [h/l] ")

    def player_continue_option(self):
        """
        Continue playing question.
        Return: String
        """
        return input("Play again? [y/n] ")

    def up_score(self):
        """
        Add 100 to score.
        """
        self.score += 100

    def down_score(self):
        """
        Subtract 75 to score.
        """
        self.score -= 75