'''
Author(s): Adam Forestier
Last Updated: April 3, 2020
Description: bot.py contains the driver code for an Instagram bot
'''

# Import methods and variables from other files
from helpers.base import (
    post_photo
)
test_photo = 'D:/coding/Python/projects/insta-manager/src/photos/CirqueOfTowers_Mountain.JPG'

test_caption = 'The Cirque of Towers in the Wind River Range is one of the most amazing and wild alpine climbing and backcountry locations in the lower 48! Photo taken August 2019'

test_hashtags = [
    'Wyoming',
    'alpine',
    'alpineclimbing',
    'august',
    'climbing',
    'tradisrad',
    'backcountry',
    'backpacking',
    'hiking',
    'mountains',
    'windriverrange',
    'west',
    'unitedstates',
    'rockclimbing',
    'tradclimbing',
    'multipitchclimbing',
    'camping',
    'wilderness'
]

post_photo(test_photo, test_caption, test_hashtags)

