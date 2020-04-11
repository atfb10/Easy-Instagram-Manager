'''
Author(s): Adam Forestier
Last Updated: April 2, 2020
Description: generators.py contains the functions to handle random number generation
'''

# Libraries
from random import randint

def select_specific_hashtags():
    '''
    arguments: none
    returns: randomly generated number between 0 and 3
    description select_specific_hashtags() generates and returns a number between 0-3
    to select a hashtags from specific hashtag lists
    '''
    return randint(0, 3)