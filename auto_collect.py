import time

from __init__ import *
from collect_creator import *

import random

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
characters = random.sample(alphabet, 5)


def auto(nation):
    for _ in range(10):
        try:
            auto_collect(nation, random.sample(alphabet, 3))
        except Exception as e:
            print(e)
            time.sleep(3)
