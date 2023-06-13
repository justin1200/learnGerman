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
    learnGermanWordsMenu.addMenuItem(BODY, 7)
    learnGermanWordsMenu.addMenuItem(MAIN_MENU_RETURN, 8)
    menus[learnGermanWordsMenu.title] = learnGermanWordsMenu

    # Past, present and future tense menu
    tensesMenu = subMenu(TENSES_MENU)
    tensesMenu.addMenuItem(PERFECT_PAST, 1)
    tensesMenu.addMenuItem(PRESENT_TENSE_ER_SIE_ES, 2)
    tensesMenu.addMenuItem(SIMPLE_PAST, 3)
    tensesMenu.addMenuItem(MAIN_MENU_RETURN, 4)
    menus[tensesMenu.title] = tensesMenu


    # Nominative, accusative, dative and genitive cases menu
    casesMenu = subMenu(CASES_MENU)
    casesMenu.addMenuItem(PREPOSITIONS, 1)
    casesMenu.addMenuItem(VERBS, 2)
    casesMenu.addMenuItem(MAIN_MENU_RETURN, 3)
    menus[casesMenu.title] = casesMenu

    # Adjectives menu
    adjectivesMenu = subMenu(ADJECTIVES_MENU)
    adjectivesMenu.addMenuItem(SUPERLATIVE, 1)
    adjectivesMenu.addMenuItem(COMPARATIVE, 2)
    adjectivesMenu.addMenuItem(MAIN_MENU_RETURN, 3)
    menus[adjectivesMenu.title] = adjectivesMenu

    return menus



def createGames():

    games = dict()

    # Learn German words games
    theWorkplace = wordGame(THE_WORKPLACE, LEARN_GERMAN_WORDS_MENU_INSTRUCTION, THE_WORKPLACE_GREETING)
    theWorkplace.readCSV("csv/germanWords/theWorkplace.csv", "english", "german")
    games[theWorkplace.title] = theWorkplace
    
    travelling = wordGame(TRAVELLING, LEARN_GERMAN_WORDS_MENU_INSTRUCTION, TRAVELLING_GREETING)
    travelling.readCSV("csv/germanWords/travelling.csv", "english", "german")
    games[travelling.title] = travelling

    food = wordGame(FOOD_EATING_AND_DRINKING, LEARN_GERMAN_WORDS_MENU_INSTRUCTION, FOOD_EATING_AND_DRINKING_GREETING)
    food.readCSV("csv/germanWords/food.csv", "english", "german")
    games[food.title] = food

    clothing = wordGame(CLOTHING, LEARN_GERMAN_WORDS_MENU_INSTRUCTION, CLOTHING_GREETING)
    clothing.readCSV("csv/germanWords/clothing.csv", "english", "german")
    games[clothing.title] = clothing

    greetings = wordGame(GREETINGS, LEARN_GERMAN_WORDS_MENU_INSTRUCTION, GREETINGS_GREETING)
    greetings.readCSV("csv/germanWords/greetings.csv", "english", "german")
    games[greetings.title] = greetings

    theHome = wordGame(THE_HOME, LEARN_GERMAN_WORDS_MENU_INSTRUCTION, THE_HOME_GREETING)
    theHome.readCSV("csv/germanWords/theHome.csv", "english", "german")
    games[theHome.title] = theHome

    body = wordGame(BODY, LEARN_GERMAN_WORDS_MENU_INSTRUCTION, BODY_GREETING)
    body.readCSV("csv/germanWords/body.csv", "english", "german")
    games[body.title] = body


    # Tenses games
    perfect_past = wordGame(PERFECT_PAST, PERFECT_PAST_INSTRUCTION, PERFECT_PAST_GREETING)
    perfect_past.readCSV("csv/tense/perfectPast.csv", "word", "prefectPast")
    games[perfect_past.title] = perfect_past

    presentTenseErSieEs = wordGame(PRESENT_TENSE_ER_SIE_ES, PRESENT_TENSE_ER_SIE_ES_INSTRUCTION,
                                   PRESENT_TENSE_ER_SIE_ES_GREETING)
    presentTenseErSieEs.readCSV("csv/tense/presentTenseErSieEs.csv", "word", "presentTenseErSieEs")
    games[presentTenseErSieEs.title] = presentTenseErSieEs

    simeplePast = wordGame(SIMPLE_PAST, SIMPLE_PAST_INSTRUCTION, SIMPLE_PAST_GREETING)
    simeplePast.readCSV("csv/tense/simplePast.csv", "word", "simplePast")
    games[simeplePast.title] = simeplePast


    # Cases games
    prepositions = wordGame(PREPOSITIONS, PREPOSITIONS_INSTRUCTION, PREPOSITIONS_GREETING)
    prepositions.readCSV("csv/cases/prepositions.csv", "preposition", "case")
    games[prepositions.title] = prepositions

    verbs = wordGame(VERBS, VERBS_INSTRUCTION, VERBS_GREETING)
    verbs.readCSV("csv/cases/words.csv", "word", "case")
    games[verbs.title] = verbs


    # Adjectives games
    superlative = wordGame(SUPERLATIVE, SUPERLATIVE_INSTRUCTION, SUPERLATIVE_GREETING)
    superlative.readCSV("csv/adjectives/superlative.csv", "word", "superlative")
    games[superlative.title] = superlative

    comparative = wordGame(COMPARATIVE, COMPARATIVE_INSTRUCTION, COMPARATIVE_GREETING)
    comparative.readCSV("csv/adjectives/comparative.csv", "word", "comparative")
    games[comparative.title] = comparative

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
        return findMenuOrGame(selectionTemp, menus, games)


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


    # Next check games and run them for learnGermanWords
    if selection == THE_WORKPLACE:
        games[THE_WORKPLACE].playGame()
        return menus[LEARN_GERMAN_WORDS_MENU]
    elif selection == GREETINGS:
        games[GREETINGS].playGame()
        return menus[LEARN_GERMAN_WORDS_MENU]
    elif selection == TRAVELLING:
        games[TRAVELLING].playGame()
        return menus[LEARN_GERMAN_WORDS_MENU]
    elif selection == FOOD_EATING_AND_DRINKING:
        games[FOOD_EATING_AND_DRINKING].playGame()
        return menus[LEARN_GERMAN_WORDS_MENU]
    elif selection == THE_HOME:
        games[THE_HOME].playGame()
        return menus[LEARN_GERMAN_WORDS_MENU]
    elif selection == CLOTHING:
        games[CLOTHING].playGame()
        return menus[LEARN_GERMAN_WORDS_MENU]
    elif selection == BODY:
        games[BODY].playGame()
        return menus[LEARN_GERMAN_WORDS_MENU]


    # Next check games and run them for tense
    if selection == PERFECT_PAST:
        games[PERFECT_PAST].playGame()
        return menus[TENSES_MENU]
    elif selection == PRESENT_TENSE_ER_SIE_ES:
        games[PRESENT_TENSE_ER_SIE_ES].playGame()
        return menus[TENSES_MENU]
    elif selection == SIMPLE_PAST:
        games[SIMPLE_PAST].playGame()
        return menus[TENSES_MENU]


    # Next check games and run them for cases
    if selection == PREPOSITIONS:
        games[PREPOSITIONS].playGame()
        return menus[CASES_MENU]
    elif selection == VERBS:
        games[VERBS].playGame()
        return menus[CASES_MENU]


    # Next check games and run them for adjectives
    if selection == SUPERLATIVE:
        games[SUPERLATIVE].playGame()
        return menus[ADJECTIVES_MENU]
    elif selection == COMPARATIVE:
        games[COMPARATIVE].playGame()
        return menus[ADJECTIVES_MENU]


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
