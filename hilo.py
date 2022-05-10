import random
from collections import deque
class game_logic:
    def __init__(self):
        self.points = 300
        self.answer = ''
        self.high_low = ''
        self.number = 0
        self.alive = True
        self.randomNumber = deque([random.randint(1,13),random.randint(1,13)])
    def start_game(self):
    #TODO Start the game calling get_input method, handle all subordinate methods on this function. This method also runs the loop and ends when points are 0 or player selects N
        while self.alive == True:
            self.display()
            self.get_input()
            self.roll_card()
            self.handle_input()
            self.score()
            self.answer = input(f"Play again?[y/n] ").lower()
            self.update()
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
    def display(self):
    #TODO Display Information
        print(f"\nThe card is: {self.randomNumber[0]}")
    def handle_input(self):
    #TODO Process input, calculate points and decide if the game ends.
        if self.high_low == 'l'.lower():
            if self.randomNumber[0] < self.randomNumber[1]:
                self.points += 100
            else:
                self.points -= 75
        if self.high_low == 'h'.lower():
            if self.randomNumber[0] > self.randomNumber[1]:
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
    def roll_card(self): 
        self.randomNumber.popleft()
        self.randomNumber.append(random.randint(1,13))
    def score(self):
        #TODO create a method that prints what the number was and the score
        print(f"The next card was: {self.randomNumber[0]}")
        print(f"Your score is {self.points}")

        


