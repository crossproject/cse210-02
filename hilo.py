import random
from collections import deque
class player():
    def __init__(self):
        self.points = 300
        self.answer = 'y'
        self.high_low = ''
    def get_input(self):
    #TODO Collect inputs.
        while True:
            try:
                self.high_low = input(f"Higher or lower? [h/l] ").lower()
            except ValueError:
                print(f'Invalid input: {self.high_low}')
            else:
                if self.high_low == 'l' or self.high_low =='h':
                    break
                else:
                    print(f'Invalid input: {self.high_low}')
class card():
    def __init__(self):
        self.randomNumber = deque([random.randint(1,13),random.randint(1,13)])
    def roll_card(self): 
        self.randomNumber.popleft()
        self.randomNumber.append(random.randint(1,13))

class game_logic(card, player):
    def __init__(self):
        super().__init__()
        self.points = 300
        self.alive = True
    def start_game(self):
    #TODO Start the game calling get_input method, handle all subordinate methods on this function. This method also runs the loop and ends when points are 0 or player selects N
        while self.alive == True:
            self.display()
            self.get_input()
            self.roll_card()
            self.handle_input()
            self.score()
            if self.points <= 0:
                print("Game Over")
                self.alive = False
                break
            self.answer = input(f"Play again?[y/n] ").lower()

            self.validation()
    def display(self):
    #TODO Display Information
        print(f"\nThe card is: {self.randomNumber[0]}")
    def handle_input(self):
    #TODO Process input, calculate points and decide if the game ends.
        if self.high_low == 'l'.lower():
            if self.randomNumber[0] < self.randomNumber[1]:
                self.points -= 100
            else:
                self.points -= 75
        if self.high_low == 'h'.lower():
            if self.randomNumber[0] > self.randomNumber[1]:
                self.points -= 100
            else:
                self.points -= 75
    #TODO Determine the next card available
    def validation(self):
        while True:
            try:
                if self.answer == 'n':
                    self.alive = False
            except ValueError:
                print(f'Invalid input: {self.answer}')
            else:
                if self.answer == 'n' or self.answer =='y':
                    break
                else:
                    print(f'Invalid input: {self.answer}')
                    self.answer = input(f"Play again?[y/n] ").lower()
    def score(self):
        #TODO create a method that prints what the number was and the score
        print(f"The next card was: {self.randomNumber[0]}")
        print(f"Your score is {self.points}")

     


