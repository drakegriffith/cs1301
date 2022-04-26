# import and use the following function for your HW05!
# please do not turn this file in when submitting!

def counterPick(fighter):
    counter = {
            'mario':['luigi','link'],
            'luigi':['bowser','ness'],
            'bowser':['mario','link'],
            'captain falcon':['fox','marth'],
            'fox':['samus','mewtwo'],
            'ness':['bowser','samus'],
            'kirby':['mario','captain falcon'],
            'samus':['pikachu','marth'],
            'link':['fox','ness'],
            'pikachu':['captain falcon','kirby'],
            'marth':['luigi','mewtwo'],
            'mewtwo':['kirby','pikachu']
    }
    return counter.get(fighter)
