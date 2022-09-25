# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from menu import menu
from mainMenu import mainMenu
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    mainMenu = mainMenu()
    mainMenu.addMenuItem("one", 1)
    mainMenu.addMenuItem("two", 2)
    mainMenu.welcomeMessage()
    mainMenu.aboutPage()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
