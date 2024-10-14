import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##PlayerSETUP##

class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []


myPlayer = player()


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('######################################')
    print('######   Your journey Awaits!  #######')
    print('######################################')
    print('               -PLAY-                 ')
    print('               -HELP-                 ')
    print('               -QUIT-                 ')
    print('######################################')
    title_screen_selections()

def help_menu():
    print('######################################')
    print('#  Tips To Aid You On Your Quest!    #')
    print('######################################')
    print('   -Use UP, DOWN, LEFT, RIGHT to move-')
    print('   -Type Your Commands To Execute-    ')
    print('   -Use Look To Inspect-              ')
    print('###   Good Luck On Your Journey    ###')
    print('######################################')

    