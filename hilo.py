import random
class game_logic:
    def __init__(self):
        self.points = 300
        self.answer = ''
        self.high_low = ''
        self.number = 0
        self.randomNumber = random.randint(1,13)
    def start_game(self):
    #TODO Start the game calling get_input method, haddle all subordinate methods on this function. This method also runs the loop and ends when points are 0 or player selects N
        pass
    def get_input(self):
    #TODO Collect inputs.
        self.high_low = input(f"Higher or lower? [h/l]")
        self.answer = input(f"Play again?")
    def display(self):
    #TODO Display Information
        pass
    def haddle_input(self):
    #TODO Process input, calculate points and decide if the game ends.
        pass

    


