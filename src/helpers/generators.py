'''
Author(s): Adam Forestier
Last Updated: April 2, 2020
Description: contains the functions to handle random number generation and to generate
photo caption and hashtag lists 
'''

# Libraries
from random import randint

# Import personal libraries and variables
from helpers.photos import select_photo
from variables.constants import *

def select_special_hashtags():
    '''
    arguments: none
    returns: randomly generated number between 0 and 3
    description select_specific_hashtags() generates and returns a number between 0-3
    to select a hashtag from special hashtag lists based on naming of photo file
    '''
    return randint(0, 3)

def generate_caption():
    '''
    TODO: I will create captions using functions in the generators file
    '''

def generate_hashtags():
    '''
    TODO: I will create hashtags using functions in the generators file
    '''

