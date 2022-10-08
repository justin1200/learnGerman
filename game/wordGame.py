from game.game import game
from global_constants import *
import os

"""This is the class that handles games where the user has to write a word."""
class wordGame(game):

    """Constructor to create the sub menu."""
    def __init__(self, title: str, instruction: str, welcomeMessage: str):
        # Call to super function to have access to all attributes / methods
        super().__init__(title)

        # Run validations.
        assert instruction != "" or instruction is not None, f"{instruction} is a valid instruction."
        assert welcomeMessage != "" or welcomeMessage is not None, f"{welcomeMessage} is a valid welcome message."

        # Assign values
        self.__instruction = instruction
        self.__welcomeMessage = welcomeMessage



    # Getters and Setters.
    @property
    def instruction(self):
        return self.__instruction

    @property
    def welcomeMessage(self):
        return self.__welcomeMessage



    """Runs the functionality for playing and ending the game."""
    def playGame(self):

        self.welcome()


    "Prints the welcome message of the game."
    def welcome(self):

        os.system('cls')
        print(SEPERATOR)
        print(f"{str.upper(self.title)}")
        print(SEPERATOR)
        print(f"{self.__welcomeMessage}")
        print(SEPERATOR)

    def playRound(self):

        pass