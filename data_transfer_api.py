# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:37:37 2017

@author: ravitiwari
"""

import json
from pprint import pprint

f = open('pets.txt')
text = f.read()
f.close()

pets = json.loads(text)
pprint pets

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)
parsed_json.keys()
parsed_json.values()

d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}

json.dumps(d)

f = open("user_data.txt")
text = f.read()
f.close()
user_data = json.loads(text)