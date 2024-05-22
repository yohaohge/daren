import json
from collections import defaultdict
import pickle
import os

ph_creators = defaultdict(dict)
if os.path.exists("ph_creator.pickle"):
    with open("ph_creator.pickle", "rb") as f:
        ph_creators = pickle.load(f)
print(ph_creators)

with open("ph_creator.json", "w", encoding="utf-8") as f:
    json.dump(ph_creators, f)