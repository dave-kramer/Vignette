import json

with open('json/top1000characters.json') as f:
    charlist = json.load(f)
    chardata = charlist['data']

with open('json/top500anime.json') as f:
    animelist = json.load(f)
    animedata = animelist['data']
