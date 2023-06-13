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

        answer = ""

        # Welcome user
        self.welcome()

        # Play game rounds until prompted to return to menu.
        while (answer != "*"):
            num = self.getNum(0, len(self.answersByNumber) - 1)
            answer = self.playRound(num)

        return answer



    "Prints the welcome message of the game."
    def welcome(self):

        os.system('clear')
        print(SEPERATOR)
        print(f"{str.upper(self.title)}")
        print(SEPERATOR)
        print(f"{self.__welcomeMessage}")
        print(SEPERATOR)
        input("Enter any key to continue. ")



    "Runs a single round of the game by asking the user a question."
    def playRound(self, num):

        question_word = self.answersByNumber[num][0]
        answer_word = self.answersByNumber[num][1]
        correct = False
        answer = ""

        # Ask user a question, get an answer and check it.
        while not correct:
            # Ask question and wait for answer
            correct = False
            os.system('clear')
            answer = str(input(f"For {question_word}, {self.__instruction}.\n Use ! for special characters such as" +
                               f" 'a!' for ä. Press * to return to the game menu: "))

            # Check answer
            if answer == "*":
                return answer
            elif (answer_word == answer):
                correct = True
                input("\n\nCorrect answer!! Enter any key to continue. ")
            else:
                input(f"\n\nWrong answer!!! {answer_word} is correct! Try again! Enter any key to continue. ")

        return answer
