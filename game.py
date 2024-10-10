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

    while option.lower() not in ['play', 'hlep', 'quit']:
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