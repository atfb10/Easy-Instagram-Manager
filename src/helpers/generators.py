'''
Author(s): Adam Forestier
Last Updated: April 2, 2020
Description: contains the functions to handle random number generation, randomly generates
photo caption and hashtag lists, and randomly follow users 
'''

# To be able to import personal libraries and variables from higher directory
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# Libraries

# Import personal libraries and variables
from photos import select_photo
from variables.constants import *

def generate_caption(picture_name):
    '''
    arguments: picture_name is the name of the picture to be captioned and posted
    returns: caption for post
    description: generate_caption() takes in a picture, and as long as naming convention is followed as outlined
    in strategy.txt; will accurately caption it
    '''
    tmp = picture_name.split('$')
    tmp = tmp[1]
    tmp = tmp.split('!')
    tmp = tmp[0]
    caption_list = tmp.split('-')
    caption = caption_list[0]
    for word in caption_list:
        if word != caption_list[0] and word != ',':
            caption += ' ' + word
        if word == ',':
            caption += word
    return caption

def generate_hashtags(picture_name):
    '''
    TODO: I will create hashtags using functions in the generators file
    '''


hi = generate_caption(PHOTO_DIR + 'The-Stuart-Enchantments-,-Washington!mountainswashington')
print(hi)