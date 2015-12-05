__author__ = 'Leria'

import re
import sys

data = 'PART I IT WAS A PLEASURE TO BURN IT was a special pleasure to see things eaten, to see things blackened and changed. With the brass nozzle in his fists, with this great python spitting its venomous kerosene upon the world, the blood pounded in his head, and his hands were the hands of some amazing conductor playing all the symphonies of blazing and burning to bring down the tatters and charcoal ruins of history. With his symbolic helmet numbered 451 on his stolid head, and his eyes all orange fl'

def telegram(text):
    # pattern = "\W"
    # res = re.sub(pattern, ' ', text)
    # res_norm = re.sub('\s{2}', ' ', res)
    pattern = "[^a-zA-Z0-9]+"
    res = re.sub(pattern, ' ', data)
    return res

print(telegram(data))