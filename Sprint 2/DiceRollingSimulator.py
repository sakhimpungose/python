import random
import time

"""
@author: Sakhile Mpungose

Dice Rolling Simulator

This is a simple dice rolling simulater. It prompts the user to roll a single dice.
You can roll the dice as many times as you wish.
When you are done, it will tell you how many times you rolled the dice.
"""

class Dice():
    
    def __init__(self):
        self.roll() # Initialising the dice with an appropriate random value
        
    def roll(self):
        # Generate a random integer between 1 and 6 (both included)
        self.__value = random.randint(1, 6)
    
    # String representation of the dice
    def __str__(self):
        return str(self.__value)
    
class DiceRollingSimulator():
    # Defining messages that will be displayed to the user beforehand
    __welcomeMessage = "Dice Rolling Simulator"
    __readyToPlayMessage = "Are you ready to roll the dice? Enter Yes or No."
    __playAgainMessage = "Play again? Enter Yes or No."
    __rolledDiceMessage = "You rolled a %s!"
    __rollingDiceMessage = "Dice rolling..."
    __thankYouMessage = "Thank you for playing!"
    
    
    __playing = False # True if the user is paying the game, otherwise False
    
    __numberOfPlays = 0 # Number of times the user has played the game
    
    def __init__(self):
        self.play() # Setting up the game
        
    """Game play logic.

        
    Returns
    -------
        None
    """    
    def play(self):
        #Display welcome message
        print(self.burgerMessage(self.__welcomeMessage, n = 6))
        # Does the user wants to play?
        readyToPlay = self.getUserInput(self.__readyToPlayMessage)
        
        if readyToPlay == "yes" or readyToPlay == "y":
            # The user wants to play
            self.__playing = True 
            self.__numberOfPlays += 1 # Increment number of plays by 1 because the user is playing
        
        while self.__playing:
            dice = Dice() # Instantiating a Dice object
            
            dice.roll() # Rolling the dice
            print(self.__rollingDiceMessage) # Telling the user that the dice is rolling
            
            # Haulting the execution for 2 to 4 seconds as the dice is still "rolling"            
            time.sleep(random.randint(2,4)) 
            
            print(self.__rolledDiceMessage % (dice)) # Display the rolled dice to the user
            
            # Ask the user if they want to play or no
            playAgain = self.getUserInput(self.__playAgainMessage)
            
            # If the user wants to play
            if playAgain == "yes" or playAgain == "y":
                self.__numberOfPlays += 1 # Increment number of plays by 1 because the user decided to play again
                continue
            # If the user is done playing
            else:               
                self.__playing = False # Stop the Game
        
        # Check if the user played at least once before exiting
        if self.__numberOfPlays > 0:
            # If the user played at least once, display the number of times they have played along with he default thank message
            self.__thankYouMessage = f"You played {self.__numberOfPlays} time{'s' if self.__numberOfPlays > 1 else ' only'}. {self.__thankYouMessage}"
            
        print(self.burgerMessage(self.__thankYouMessage, "*", 6))
            
            
    """Prompts a user for input.

    Parameters
    ----------
    message : str
        A message to be displayed to the user
        
    Returns
    -------
        str
            User input
    """
    def getUserInput(self, message):
        return input(f"{message} \n>>> ")
    
    """Creates a burger like message
     
    Parameters
    ----------
    message : str
        A message to be displayed to the user
        
    decorator : str
        A string to decorate the message
        
    n : int
        How many times should the decorator be used as prefix and suffix to the message
    
    """
    def burgerMessage(self, message, decorator = '-', n = 3):
        mainLine = f"{decorator * n} {message} {decorator * n}" # Concatenating the message with a prefix and a suffix
        secondaryLine = decorator * len(mainLine)
        
        return "{}\n{}\n{}\n".format(secondaryLine, mainLine, secondaryLine)
    
    
if __name__ == '__main__':    
    diceGame = DiceRollingSimulator()
