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
from os import listdir
from os.path import (
    isfile, 
    join
)
from random import randint

# My libraries

from variables.constants import *

def select_photo(directory=PHOTO_DIR):
    '''
    arguments: directory is the constant directory where the photos will live
    '''
    photos = [photo for photo in listdir(directory) if isfile(join(directory, photo))]
    photo_num = randint(0, (len(photos)) - 1)
    pic = photos[photo_num]
    return pic

def get_photo_directory(photo_filename):
    '''
    arguments: photo_filename is the name of the photo selected to posted
    returns: directory pointing to where photo to be posted lives
    description: get_photo_directory() gets the correct directory of a photo in order to accurately
    point to where picture to be posted lives
    '''
    return PHOTO_DIR + '/' + photo_filename

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