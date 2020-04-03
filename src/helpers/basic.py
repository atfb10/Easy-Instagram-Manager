'''
Author(s): Adam Forestier
Last Updated: April 2, 2020
Description: helpers.py contains the functions to assist driver code
'''

# Libraries
from instabot import Bot

# Import project functions and models
from helpers.PII import (
    username,
    password
)

def sign_in():
    '''
    arguments: none
    returns: nothing
    description: the function sign_in() utilizes the instabot library to sign into the specified instagram account
    '''
    insta_bot = Bot()
    insta_bot.login(username=username, password=password)
    return

def generate_caption():
    '''
    TODO: 
    '''

def upload_photo(photo):
    '''
    arguments: photo file
    returns: nothing
    description: the function upload_photo() signs in takes in a photo argument and posts said photo
    '''


