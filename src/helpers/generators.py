'''
Author(s): Adam Forestier
Last Updated: April 2, 2020
Description: generators.py contains the functions to handle random number generation and to generate
hashtag lists
'''

# Libraries
from random import randint

# Import personal libraries and variables
from helpers.photos import select_photo
from variables.constants import *

def select_specific_hashtags():
    '''
    arguments: none
    returns: randomly generated number between 0 and 3
    description select_specific_hashtags() generates and returns a number between 0-3
    to select a hashtags from specific hashtag lists
    '''
    return randint(0, 3)

