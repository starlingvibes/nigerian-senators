#! usr/bin/python

# Written by starlingvibe <chidexy67@gmail.com>
# Github: https://github.com/starlingvibes
# Data from: https://ngleadersdb.herokuapp.com/
# #EndSARS #EndPoliceBrutality

import requests
import json


# present json data in readable format
def visuals(objects):
    text = json.dumps(objects, sort_keys=True, indent=4)
    print(text)


response = requests.get("https://ngleadersdb.herokuapp.com/api/senator/all")
visuals(response.json())
