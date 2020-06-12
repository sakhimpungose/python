
class Dice():
    
    def __init__(self):
        self.roll() # Initialising the dice with an appropriate random value
        
    def roll(self):
        # Generate a random integer between 1 and 6 (both included)
        self.__value = random.randint(1, 6)
    
    # String representation of the dice
    def __str__(self):
        return str(self.__value)
    
