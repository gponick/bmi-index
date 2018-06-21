#!/usr/bin/env python3

import logging
import requests
import os
import pickle
import time
import json

allfiles = os.listdir('.')
mods = []
for fil in allfiles:
    if fil == ".git":
        continue
    if os.path.isdir(os.path.join(os.path.abspath('.'), fil)):
        with open(os.path.join(os.path.abspath('.'),fil,'mod.json'),'r') as modfile:
            modjson = modfile.read()
            mod = json.loads(modjson)
            mod['Name'] = fil
            mods.append(mod)

modlistdict = {}

for mod in mods:
    print(mod['Name'])
    modlistdict[mod['Name']] = { 'Name': mod['Name'], 'Author': mod['Author'], 'Website': mod['Website'], 'Category': mod['Category'] if 'Category' in mod else 'Unknown', 'Description': mod['Description'] }

os.remove(os.path.join(os.path.abspath('.'),'modlist.json'))
with open(os.path.join(os.path.abspath('.'),'modlist.json'),'w') as modlistfile:
    modlistfile.write(json.dumps(modlistdict, indent=4))
        
print(json.dumps(modlistdict, indent=4))