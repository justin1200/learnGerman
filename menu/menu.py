import os
from global_constants import *

"""A menu contains items that allows the user to navigate the program."""
class menu:

    """Constructor to create an item."""
    def __init__(self, title: str):

        # Run validations to the received arguments.
        assert title != "" or title is not None, f"{title} is a valid title."

        # Assign to self object.
        self.__title = title
        self.__itemsByName = dict()
        self.__itemsByPosition = dict()



    # Getters and Setters.
    @property
    def title(self):
        return self.__title

    @property
    def itemsByName(self):
        return self.__itemsByName

    @property
    def itemsByPosition(self):
        return self.__itemsByPosition



    """Add a new item to the menu."""
    def addMenuItem(self, title: str, position: int):

        # Check that title and position are valid values.
        assert title != "" or title is not None, f"{title} is a valid title."
        assert position >= 0, f"{position} must not be negative."

        # Check that position or title aren't already used.
        assert title not in self.__itemsByName.keys(), f"{title} already in the menu."
        assert position not in self.__itemsByPosition.keys(),  f"{position} already taken."

        # Position is equal to size of new size of menu.
        assert position - 1 == len(self.__itemsByPosition.keys()), f"{position} too large."

        # Add item
        self.__itemsByName[title] = position
        self.__itemsByPosition[position] = title

        return 0



    """Display the menu."""
    def displayMenu(self):

        os.system('clear')
        print(SEPERATOR)
        print(str.upper(self.__title))
        print(SEPERATOR)

        # List out menu options.
        for i in range(1, len(self.__itemsByPosition.keys()) + 1):
            print(f"{i}: {self.__itemsByPosition[i]}")
        print(SEPERATOR)

        return input("Select an option from the above menu: ")



    """Get the name of the selected option."""
    def getSelectionName(self, selection):

        return self.itemsByPosition[int(selection)]
