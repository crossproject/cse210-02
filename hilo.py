import random
from collections import deque
class game_logic:
    def __init__(self):
        self.points = 300
        self.answer = ''
        self.high_low = ''
        self.number = 0
        self.alive = True
        self.randomNumber = deque()
    def start_game(self):
    #TODO Start the game calling get_input method, haddle all subordinate methods on this function. This method also runs the loop and ends when points are 0 or player selects N
        while self.alive == True:
            self.get_input()
            self.display()
            self.answer = input(f"Play again?")
    def get_input(self):
    #TODO Collect inputs.
        self.high_low = input(f"Higher or lower? [h/l]")
    def display(self):
    #TODO Display Information
        print("")
    def haddle_input(self):
    #TODO Process input, calculate points and decide if the game ends.
        if self.answer == 'l'.lower():
            if self.high_low < self.randomNumber:
                self.points += 100
            else:
                self.points -= 75
        if self.answer == 'h'.lower():
            if self.high_low < self.randomNumber:
                self.points += 100
            else:
                self.points -= 75
    #TODO Determine the next card available
    def update(self):
        #TODO Determine when the game is over
        if self.points <= 0:
            self.alive = False
        else:
            self.alive = True
    def roll_card(self): 
        self.randomNumber.popleft()

        


