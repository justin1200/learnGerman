"""A menuItem is an item in a menu selection. Each menuItem has a title and points towards another area of the
program such as another menu, about page or one of the practice games."""
class menuItem:

    """Constructor to create an item."""
    def __init__(self, title: str, position: int):
        # Run validations to the received arguments
        assert title != "" or title is not None, f"{title} is a valid title."
        assert position >= 0, f"{position} must not be negative."

        # Assign to self object
        self.__title = title
        self.__position = position

    # Getters and Setters
    @property
    def title(self):
        return self.__title

    @property
    def position(self):
        return self.__position