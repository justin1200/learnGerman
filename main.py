# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from mainMenu import mainMenu
from subMenu import subMenu
import os

# Menus
MAINMENU = "Main Menu"
LEARNGERMANWORDSMENU = "Learn German Words"
TENSESMENU = "Past, present and future tense"
CASESMENU = "Nominative, accusative, dative and genitive cases"
ADJECTIVESMENU = "Adjectives"
ABOUTPAGE = "About"
PROGRAMEXIT = "Exit Program"

def createMenus():

    menus = dict()

    # Create main menu
    GameMenu = mainMenu()
    GameMenu.addMenuItem(LEARNGERMANWORDSMENU, 1)
    GameMenu.addMenuItem(TENSESMENU, 2)
    GameMenu.addMenuItem(CASESMENU, 3)
    GameMenu.addMenuItem(ADJECTIVESMENU, 4)
    GameMenu.addMenuItem(ABOUTPAGE, 5)
    GameMenu.addMenuItem(PROGRAMEXIT, 6)
    menus[GameMenu.title] = GameMenu

    # Learn German words menu
    learnGermanWordsMenu = subMenu(LEARNGERMANWORDSMENU)
    learnGermanWordsMenu.addMenuItem("Greetings", 1)
    learnGermanWordsMenu.addMenuItem("The workplace", 2)
    learnGermanWordsMenu.addMenuItem("Travelling", 3)
    learnGermanWordsMenu.addMenuItem("Food, eating and drinking", 4)
    learnGermanWordsMenu.addMenuItem("The home", 5)
    learnGermanWordsMenu.addMenuItem("Clothing", 6)
    learnGermanWordsMenu.addMenuItem("Return to main menu", 7)
    menus[learnGermanWordsMenu.title] = learnGermanWordsMenu

    # Past, present and future tense menu
    tensesMenu = subMenu(TENSESMENU)
    tensesMenu.addMenuItem("Return to main menu", 1)
    menus[tensesMenu.title] = tensesMenu


    # Nominative, accusative, dative and genitive cases menu
    casesMenu = subMenu(CASESMENU)
    casesMenu.addMenuItem("Return to main menu", 1)
    menus[casesMenu.title] = casesMenu

    # Adjectives menu
    adjectivesMenu = subMenu(ADJECTIVESMENU)
    adjectivesMenu.addMenuItem("Return to main menu", 1)
    menus[adjectivesMenu.title] = adjectivesMenu

    #print(GameMenu.displayMenu())
    #x = GameMenu.displayMenu()
    #print(x)
    #print(GameMenu.getSelectionName(x))
    #print(GameMenu.itemsByPosition[1])

    return menus

def findMenuOrGame(selection, menus):

    # Check for about page and program exit
    if selection == PROGRAMEXIT:
        menus[MAINMENU].exitProgram()
    if selection == ABOUTPAGE:
        mainMenuTemp = menus[MAINMENU]
        selectionTemp = mainMenuTemp.aboutPage()
        selectionTemp = mainMenuTemp.getSelectionName(selectionTemp)
        return findMenuOrGame(selectionTemp, menus)

    # Check menus first
    if selection == MAINMENU:
        return menus[MAINMENU]
    elif selection == LEARNGERMANWORDSMENU:
        return menus[LEARNGERMANWORDSMENU]
    elif selection == TENSESMENU:
        return menus[TENSESMENU]
    elif selection == CASESMENU:
        return menus[CASESMENU]
    elif selection == ADJECTIVESMENU:
        return menus[ADJECTIVESMENU]

    # Next check games and run them

def runGame(menus):

    currentMenu = menus[MAINMENU]
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
