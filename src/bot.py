'''
Author(s): Adam Forestier
Last Updated: April 3, 2020
Description: bot.py contains the driver code for an Instagram bot
'''

# Import methods and variables from other files
from helpers.base import (
    post_photo
)
from helpers.generators import (
    generate_caption,
    generate_hashtags,
)
from helpers.photos import (
    select_photo
)

photo = select_photo()

post_photo(photo, generate_caption(photo), generate_hashtags(photo))

