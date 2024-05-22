import time

from __init__ import *
from collect_creator import *

import random

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ'
characters = random.sample(alphabet, 5)


def auto(nation, prefix_len:int, max_cnt:int):
    for _ in range(max_cnt):
        try:
            auto_collect(nation, random.sample(alphabet, prefix_len))
        except Exception as e:
            print(e)
            time.sleep(3)
