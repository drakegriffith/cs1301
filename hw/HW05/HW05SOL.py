
import calendar

"""
Georgia Institute of Technology - CS1301
HW05 - Lists, Tuples, and Modules
"""

#########################################

"""
Function Name: showToWatch()
Parameters: friendsFavShows (list) and favoriteShow (str)
Returns: list of friends (list)
"""

def showToWatch(friendsFavShows, favoriteShow) :
    listofFriends = []
    for tup in range(len(friendsFavShows)) :
        if favoriteShow in friendsFavShows[tup][1] :
            listofFriends.append(friendsFavShows[tup][0])
    if len(listofFriends) == 0:
        return "Lonely night :("
    
    listofFriends.sort()
    return listofFriends

#########################################

"""
Function Name: fixLabels()
Parameters: labelList (list)
Returns: list of correct labels (list)
"""

def fixLabels(labelList) :
    digitList = []
    alphaList = []
    fixedLabelList = []

    for tup in range(len(labelList)) :
        if "a" in str(labelList[tup]) or "e" in str(labelList[tup]) or "i" in str(labelList[tup]) or "o" in str(labelList[tup]) or "u" in str(labelList[tup]) :
            alphaList.append(labelList[tup]) #^ I know it's lengthy, but all other ways failed.
        else :
            digitList.append(labelList[tup])
            
    for i in range(len(alphaList)):
        if len(alphaList) != len(digitList) :
            return 'Missing labels'
        else :
            tup1 = (alphaList[i], digitList[i])
            fixedLabelList.append(tup1)

    def tuplesorter(fixedLabelList):  
        fixedLabelList.sort(key = lambda x: x[0])
        return fixedLabelList
    tuplesorter(fixedLabelList)
        
    return fixedLabelList


#########################################

"""
Function Name: newPlaylist()
Parameters: playlist (list)
Returns: list of songs (list)
"""

def newPlaylist(playlist) :
    finalList = []
    newSong = []
    totalTimeMinute = 0
    totalTimeSecond = 0
    for tup in range(len(playlist)):
        newSong.append(playlist[tup][0])
        
        if len(playlist[tup][1]) > 4:
            totalTimeSecond += int(playlist[tup][1][3:])
            totalTimeMinute += int(playlist[tup][1][0:2])
        elif len(playlist[tup][1]) <= 4:
            totalTimeMinute += int(playlist[tup][1][0])
            totalTimeSecond += int(playlist[tup][1][2:])
        
            
    totalTimeSecond = totalTimeSecond / 60
    totalTime = float(totalTimeMinute) + float(totalTimeSecond)
    totalTime = round(totalTime,2)
    newSong.sort()
    newSong = tuple(newSong)
    finalList.append(newSong)
    finalList.append(totalTime)
    return finalList

#########################################

"""
Function Name: birthdays()
Parameters: friends (list) and birthdates (list)
Returns: list of names (list)
"""

def birthdays(friends,birthdates) :
    icanGo = []
    for tup in range(len(friends)) :
        if calendar.weekday(2022,birthdates[tup][0],birthdates[tup][1]) >= 5:
            icanGo.append(friends[tup])
        else:
            continue
    icanGo.sort()
    return icanGo

#########################################

"""
Function Name: smashBros()
Parameters: fighterList (list), opponent (str)
Returns: list of good picks (list)
"""

def smashBros(fighterList, opponent) :
    counterPicks = []
    def counterPick(fighter) :
        opponent = fighter
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
        
    if counterPick(opponent) == None :
        return None
    else :
    
        for i in range(len(fighterList)) :
            if len(counterPicks) <= 2 :
                if fighterList[i] in counterPick(opponent) :
                    if len(counterPicks) == 0 :
                        counterPicks.append(counterPick(opponent)[0])
                    elif len(counterPicks) == 1:
                        counterPicks.append(counterPick(opponent)[1])
                        
                else :
                    continue
    if len(counterPicks) == 0 :
        return 'No counters!'
    
    return counterPicks
            

        
        
               
   
    


      

    
              

