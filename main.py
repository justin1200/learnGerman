# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from mainMenu import mainMenu
from subMenu import subMenu
from global_constants import *
import os

def createMenus():

    menus = dict()

    # Create main menu
    GameMenu = mainMenu()
    GameMenu.addMenuItem(LEARN_GERMAN_WORDS_MENU, 1)
    GameMenu.addMenuItem(TENSES_MENU, 2)
    GameMenu.addMenuItem(CASES_MENU, 3)
    GameMenu.addMenuItem(ADJECTIVES_MENU, 4)
    GameMenu.addMenuItem(ABOUT_PAGE, 5)
    GameMenu.addMenuItem(PROGRAM_EXIT, 6)
    menus[GameMenu.title] = GameMenu

    # Learn German words menu
    learnGermanWordsMenu = subMenu(LEARN_GERMAN_WORDS_MENU)
    learnGermanWordsMenu.addMenuItem(GREETINGS, 1)
    learnGermanWordsMenu.addMenuItem(THE_WORKPLACE, 2)
    learnGermanWordsMenu.addMenuItem(TRAVELLING, 3)
    learnGermanWordsMenu.addMenuItem(FOOD_EATING_AND_DRINKING, 4)
    learnGermanWordsMenu.addMenuItem(THE_HOME, 5)
    learnGermanWordsMenu.addMenuItem(CLOTHING, 6)
    learnGermanWordsMenu.addMenuItem(MAIN_MENU_RETURN, 7)
    menus[learnGermanWordsMenu.title] = learnGermanWordsMenu

    # Past, present and future tense menu
    tensesMenu = subMenu(TENSES_MENU)
    tensesMenu.addMenuItem(MAIN_MENU_RETURN, 1)
    menus[tensesMenu.title] = tensesMenu


    # Nominative, accusative, dative and genitive cases menu
    casesMenu = subMenu(CASES_MENU)
    casesMenu.addMenuItem(MAIN_MENU_RETURN, 1)
    menus[casesMenu.title] = casesMenu

    # Adjectives menu
    adjectivesMenu = subMenu(ADJECTIVES_MENU)
    adjectivesMenu.addMenuItem(MAIN_MENU_RETURN, 1)
    menus[adjectivesMenu.title] = adjectivesMenu

    #print(GameMenu.displayMenu())
    #x = GameMenu.displayMenu()
    #print(x)
    #print(GameMenu.getSelectionName(x))
    #print(GameMenu.itemsByPosition[1])

    return menus

def findMenuOrGame(selection, menus):

    # Check for about page and program exit
    if selection == PROGRAM_EXIT:
        menus[MAIN_MENU].exitProgram()
    if selection == ABOUT_PAGE:
        mainMenuTemp = menus[MAIN_MENU]
        selectionTemp = mainMenuTemp.aboutPage()
        selectionTemp = mainMenuTemp.getSelectionName(selectionTemp)
        return findMenuOrGame(selectionTemp, menus)

    # Check menus first
    if selection == MAIN_MENU:
        return menus[MAIN_MENU]
    elif selection == LEARN_GERMAN_WORDS_MENU:
        return menus[LEARN_GERMAN_WORDS_MENU]
    elif selection == TENSES_MENU:
        return menus[TENSES_MENU]
    elif selection == CASES_MENU:
        return menus[CASES_MENU]
    elif selection == ADJECTIVES_MENU:
        return menus[ADJECTIVES_MENU]

    # Next check games and run them

def runGame(menus):

    currentMenu = menus[MAIN_MENU]
    currentMenu.welcomeMessage()

    selection = currentMenu.displayMenu()
    selection = currentMenu.getSelectionName(selection)
    currentMenu = findMenuOrGame(selection, menus)
    print(currentMenu.title)
    #while True:
    #    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    menus = createMenus()

    runGame(menus)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
