from menuItem import menuItem

"""A menu contains menuItems that allows the user to navigate the program."""
class menu:
    """Constructor to create an item."""

    def __init__(self, title: str):

        # Run validations to the received arguments
        assert title != "" or title is not None, f"{title} is a valid title."

        # Assign to self object
        self.__title = title
        self.__menuItems = dict()

    # Getters and Setters
    @property
    def title(self):
        return self.__title

    @property
    def menuItems(self):
        return self.__menuItems

    """Add a new item to the menu."""
    def addMenuItem(self, title: str, position: int):

        # Check that position or title aren't already used.
        assert title not in self.__menuItems.keys(), f"{title} already in the menu."
        assert position not in [self.__menuItems[key].position for key in self.__menuItems.keys()], \
            f"{position} already taken."

        # Add item to menu.
        newMenuItem = menuItem(title, position)
        self.__menuItems[newMenuItem.title] = newMenuItem

        return 0

