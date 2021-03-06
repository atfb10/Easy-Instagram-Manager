'''
Author(s): Adam Forestier
Last Updated: April 3, 2020
Description: base.py contains the functions to assist driver code
'''

# Libraries
from instabot import Bot
from subprocess import call

# Import project functions and models
from variables.constants import (
    SCRIPT_SCHEDULE_DIR
)

from variables.PII import (
    username,
    password
)

def task(terminal_cmd='python', scriptname=SCRIPT_SCHEDULE_DIR):
    '''
    argument: terminal_cmd is argument to run on terminal when subprocess is called
    scriptname is the name of the scheduler script to run
    returns: nothing
    description: task() calls the schedule.py script
    '''
    call([terminal_cmd, scriptname])

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
    print('Photo Successfully Uploaded')
    return

def unfollow_unfollowers():
    '''
    arguments: none
    returns: nothing
    description: the function unfollow_unfollowers() unfollows every one we follow
    that does not follow us
    '''
    bot = sign_in()
    bot.unfollow_non_followers()
    return