'''
Author(s): Adam Forestier
Last Updated: April 3, 2020
Description: base.py contains the functions to assist driver code
'''

# Libraries
from instabot import Bot

# Import project functions and models
from variables.PII import (
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
    return insta_bot

def post_photo(photo, caption, hashtags):
    '''
    arguments: photo file, string of comments, list of hashtags
    returns: nothing
    description: the function upload_photo() signs in takes in a photo argument and posts photo with caption
    '''
    bot = sign_in()
    hashtag_str = '#' + hashtags[0]
    for tag in hashtags:
        if tag != hashtags[0]:
            hashtag_str += ' #' + tag
    full_caption = caption + '\n\n' + hashtag_str
    bot.upload_photo(photo=photo, caption=full_caption)
    return


