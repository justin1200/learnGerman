from menu import menu
import os

"""This is the class that handles navigating the main menu of the program."""
class mainMenu(menu):

    VERSION = "1.0"
    DATE = "25-SEP-2022"
    AUTHOR = "Justin Kelley"

    """Constructor to create the main menu."""
    def __init__(self):
        # Call to super function to have access to all attributes / methods
        super().__init__("Main Menu")


    """Welcome message and nagivation to main menu upon start up of program."""
    def welcomeMessage(self):

        print(self.SEPERATOR)
        print("Welcome to LEARN GERMAN!!!! This program allows you to practice your German.")
        input("Enter any key and press enter to continue: ")
        print(self.SEPERATOR)

        return self.displayMenu()


    """Handles the showing of the about page of the program."""
    def aboutPage(self):

        os.system('cls')
        print(self.SEPERATOR)
        print("Learn German")
        print(f"Author: {self.AUTHOR}, Version: {self.VERSION}, Date: {self.DATE}")
        print("This is a Python program that allows the user to practice their German.")
        print("The user can learn varies things including words, tense and cases.")
        print(self.SEPERATOR)
        input("Enter any key and press enter to return to the main menu: ")

        return self.displayMenu()


    """Handles the closing of the program."""
    def exitProgram(self):
        print(self.SEPERATOR)
        print("Goodbye!!! Hope you learnt something!")
        input("Enter any key and press enter to exit program: ")
        print(self.SEPERATOR)

        exit(0)

