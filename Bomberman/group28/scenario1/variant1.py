# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game

#from testcharacter_niko import TestCharacter
from testcharacter_astar import TestCharacter

# TODO This is your code!
sys.path.insert(1, '../groupNN')


# Create the game
g = Game.fromfile('map.txt')

# TODO Add your character
g.add_character(TestCharacter("me", # name
                              "C",  # avatar
                              0, 0  # position
))

# Run!
g.go()
