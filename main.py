# -*- coding: utf-8 -*-

"""
This program allows an individual to practice their German grammar in a series of games including spelling, tense and cases.
"""

__author__ = 'Justin Kelley'
__date__ = '18.03.2023'
__version__ = 'V1000'

from gameControl import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Create menus and games
    menus = createMenus()
    games = createGames()

    # Run game
    runGame(menus, games)
