from menu.mainMenu import mainMenu
from menu.subMenu import subMenu
from game.wordGame import wordGame
from global_constants import *

"""Creates all the menus and their selections."""
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

    return menus

def createGames():

    games = dict()

    # Learn German words game
    theWorkplace = wordGame(THE_WORKPLACE, LEARN_GERMAN_WORDS_MENU_INSTRUCTION, THE_WORKPLACE_GREETING)
    theWorkplace.readCSV("csv\\germanWords\\theWorkplace.csv", "english", "german")
    games[theWorkplace.title] = theWorkplace

    return games

"""Based on user's selection find the menu, section or game to go to."""
def findMenuOrGame(selection, menus, games):

    # Check for about page and program exit
    if selection == PROGRAM_EXIT:
        menus[MAIN_MENU].exitProgram()
    if selection == ABOUT_PAGE:
        mainMenuTemp = menus[MAIN_MENU]
        selectionTemp = mainMenuTemp.aboutPage()
        selectionTemp = mainMenuTemp.getSelectionName(selectionTemp)
        return findMenuOrGame(selectionTemp, menus)

    # Check menus first
    if selection == MAIN_MENU or selection == MAIN_MENU_RETURN:
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
    if selection == THE_WORKPLACE:
        games[THE_WORKPLACE].playGame()
        return menus[LEARN_GERMAN_WORDS_MENU]



"""Run the program by prompting the user for menu selection and processing requests."""
def runGame(menus, games):

    # Start at welcome message and head to main menu
    currentMenu = menus[MAIN_MENU]
    currentMenu.welcomeMessage()

    # Prompt user for menu selection and process request
    while True:
        selection = currentMenu.displayMenu()
        selection = currentMenu.getSelectionName(selection)
        currentMenu = findMenuOrGame(selection, menus, games)