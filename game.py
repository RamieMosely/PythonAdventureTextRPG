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
        self.location = 'start'
        self.gameOver = False
        self.job = ""


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





    


#### MAP ####
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right','east'

solvedPlaces = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

zoneMap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'up', 'north',
        DOWN = 'down', 'south',
        LEFT = 'left', 'west',
        RIGHT = 'right','east'
        },

    'a2': {
        ZONENAME: "",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'up', 'north',
        DOWN = 'down', 'south',
        LEFT = 'left', 'west',
        RIGHT = 'right','east'
    },

    'a3': {
        ZONENAME: "",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'up', 'north',
        DOWN = 'down', 'south',
        LEFT = 'left', 'west',
        RIGHT = 'right','east'
    },

    'b1': {
        ZONENAME: "",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'up', 'north',
        DOWN = 'down', 'south',
        LEFT = 'left', 'west',
        RIGHT = 'right','east'
    },

    'b2': {
        ZONENAME: "",
        DESCRIPTION = 'This is your home!',
        EXAMINATION = 'Yes it really is a nice place!',
        SOLVED = False,
        UP = 'a2',
        DOWN = 'c2',
        LEFT = 'b1',
        RIGHT = 'b3',
    },

    'b3': {
        ZONENAME: "",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'up', 'north',
        DOWN = 'down', 'south',
        LEFT = 'left', 'west',
        RIGHT = 'right','east'
    },
}




##Game Interactivity###
def printLocation():
    print('\n' + ('#' * (4 + len[myPlayer.location])))
    print('#' + myPlayer.location.upper() + '#')
    print('#' + zoneMap[myPlayer.position][DESCRIPTION] + '#')
    print('\n' + ('#' * (4 + len[myPlayer.location])))

def prompt():
    print('\n' + "###########")
    print("What would you like to do?")
    action = input("> ")
    acceptableActions = ['move', 'walk', 'travel', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptableActions:
        print('Unknow Action, Try Again\n')
        action = input("> ")
    if action.lower == 'quit':
        sys.exit()

    elif action.lower == ['move', 'walk', 'travel']:
        playerMove(action.lower())

    elif action.lower == ['examine', 'inspect', 'interact', 'look']:
        playerExamine(action.lower())

def playerMove(myaction):
    ask = "Where would you like to go?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destiantion = zonemap[myPlayer.location][UP]
        movementHandler(destination)

    elif dest in ['left', 'west']:
        destiantion = zonemap[myPlayer.location][LEFT]
        movementHandler(destination)
    elif dest in ['right', 'east']:
        destiantion = zonemap[myPlayer.location][RIGHT]
        movementHandler(destination)
    elif dest in ['down', 'south']:
        destiantion = zonemap[myPlayer.location][DOWN]
        movementHandler(destination)


def movementHandler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    printLocation()

def playerExamine(action):
    if zoneMap[myPlayer.location][SOLVED] == True:
        print('You have already been there')
    else:
        print("")


###GameFunctionality
def start_game():
    return



def mainGameLoop():
    while myPlayer.gameOver == False:
        prompt()
        #Handle if puzzles solved, etc, etc

def setupGame():
    os.system('clear')
    question1 = "Greetings! What is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input("> ")
    myPlayer.name = playerName


    ##JOB HANDLING##
    question2 = "What is your job?\n"
    question2Added = "You can play as a warrior, priest or mage!\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2Added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    playerJob = input("> ")
    validJobs = ['warrior', 'priest', 'mage']
    if playerJob.lower in validJobs:
        myPlayer.job = playerJob
        print('You are now a ' + playerJob + '!\n')
    
    while playerJob.lower() not in validJobs:
        playerJob = input('> ')

        if playerJob.lower in validJobs:
            myPlayer.job = playerJob
            print('You are now a ' + playerJob + '!\n')

    if myPlayer.job == "warrior":
        myPlayer.hp = 200
        myPlayer.mp = 20
    elif myPlayer.job == "priest":
        myPlayer.hp = 100
        myPlayer.mp = 100
    elif myPlayer.job == "mage":
        myPlayer.hp = 100
        myPlayer.mp = 200


    ##Introduction##
    question3 = "Welcome" + playerName +  "the" + playerJob + ".\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input("> ")
    myPlayer.name = playerName

    speech1 = "Welcome to this world of discovery"
    speech2 = "Good luck on your journey"
    speech3 = "Youll need it"
    speech4 = "Hehehehehe...!"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('clear')
    print('#############################')
    print('#####   It begins...   ######')
    print('#############################')
    mainGameLoop()








title_screen()


