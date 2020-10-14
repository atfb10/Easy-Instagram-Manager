'''
Author(s): Adam Forestier
Last Updated: April 14, 2020
Description: schedule.py contains the code to schedule performing tasks
'''

# To be able to import personal libraries and variables from higher directory
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# Libraries
import schedule
import time

# Import project functions and models
from base import (
    post_photo,
    unfollow_unfollowers
)
from helpers.generators import (
    generate_caption,
    generate_hashtags,
)
from helpers.photos import (
    get_photo_directory,
    select_photo
)

schedule.every().wednesday.at('00:00').do(unfollow_unfollowers)

# Run indefinitely (until we manually shut down)
while(True):
    schedule.run_pending()
    time.sleep(1)
 