'''
Author(s): Adam Forestier
Last Updated: April 3, 2020
Description: photos.py contains the functions to perform photo related functions
'''

# To be able to import personal libraries and variables from higher directory
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# Libraries

# My libraries
from variables.constants import *

def select_photo(directory=PHOTO_DIR):
    '''
    TODO: I will randomly select a photo from a specified library
    '''

    return photo
    

def date_photo():
    '''
    TODO: I will grab the date from the picture metadata nd include it in the post if desired by subsciber
    '''

def geotag_photo():
    '''
    TODO: I will grab the geotag from a photo and include it in the caption or hashtag.

    OPINION: We may want to make this a script that runs outside the app. Fastest way to rename photos.
    Create caption and bookened with !
    '''