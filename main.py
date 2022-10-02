# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from mainMenu import mainMenu
from subMenu import subMenu
import os


def createMenus():

    menus = dict()

    # Create main menu
    GameMenu = mainMenu()
    GameMenu.addMenuItem("Learn German words", 1)
    GameMenu.addMenuItem("Past, present and future tense", 2)
    GameMenu.addMenuItem("Nominative, accusative, dative and genitive cases", 3)
    GameMenu.addMenuItem("Adjectives", 4)
    GameMenu.addMenuItem("About", 5)
    GameMenu.addMenuItem("Exit program", 6)
    menus[GameMenu.title] = GameMenu

    # Learn German words menu
    learnGermanWordsMenu = subMenu("Learn German Words")
    learnGermanWordsMenu.addMenuItem("Greetings", 1)
    learnGermanWordsMenu.addMenuItem("The workplace", 2)
    learnGermanWordsMenu.addMenuItem("Travelling", 3)
    learnGermanWordsMenu.addMenuItem("Food, eating and drinking", 4)
    learnGermanWordsMenu.addMenuItem("The home", 5)
    learnGermanWordsMenu.addMenuItem("Clothing", 6)
    learnGermanWordsMenu.addMenuItem("Return to main menu", 7)
    menus[learnGermanWordsMenu.title] = learnGermanWordsMenu

    # Past, present and future tense menu
    tensesMenu = subMenu("Past, present and future tense")
    tensesMenu.addMenuItem("Return to main menu", 1)
    menus[tensesMenu.title] = tensesMenu


    # Nominative, accusative, dative and genitive cases menu
    casesMenu = subMenu("Nominative, accusative, dative and genitive cases")
    casesMenu.addMenuItem("Return to main menu", 1)
    menus[casesMenu.title] = casesMenu

    # Adjectives menu
    adjectivesMenu = subMenu("Adjectives")
    adjectivesMenu.addMenuItem("Return to main menu", 1)
    menus[adjectivesMenu.title] = adjectivesMenu

    return menus

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    menus = createMenus()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
