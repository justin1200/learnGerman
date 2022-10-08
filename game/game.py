import csv
from global_constants import *

"""This class acts for handling the common functionality for any game."""
class game():


    """Constructor to create a game."""
    def __init__(self, title: str):
        # Run validations to the received arguments.
        assert title != "" or title is not None, f"{title} is a valid title."

        # Assign to self object.
        self.__title = title
        self.__answersByColumnOne = dict()
        self.__answersByColumnTwo = dict()
        self.__answersByNumber = dict()



    # Getters and Setters.
    @property
    def title(self):
        return self.__title

    @property
    def answersByAnswer(self):
        return self.__answersByColumnOne

    @property
    def answersByAnswer(self):
        return self.__answersByColumnTwo

    @property
    def answersByNumber(self):
        return self.__answersByNumber



    """Reads the information from the csv to generate the questions and correct answers for the game."""
    def readCSV(self, file):

        print(file)
        # Read data from the file.
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Create items from the file.
        n = 0
        for row in rows:
            self.__answersByColumnOne[row["german"]] = row["english"]
            self.__answersByColumnTwo[row["english"]] = row["german"]
            self.__answersByNumber[n] = [row["german"], row["english"]]
            n = n + 1



    """Displays the information gathered from the CSV file."""
    def printCSVInfo(self):

        for key in self.__answersByColumnOne.keys():
            print(f"{key}: {self.__answersByColumnOne[key]}")


