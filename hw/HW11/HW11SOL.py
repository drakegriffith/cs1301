"""
Georgia Institute of Technology - CS1301
HW11
"""

#########################################

"""
Function Name: puppyFinder()
Parameters: puppyCityDict (dict), cityDistanceDict (dict)
Returns: representation of puppy name, city and distance (str)
"""

#########################################

def puppyFinder(puppyCityDict, cityDistanceDict) :
    minVal = 1000
    cityFinder = ""
    for k, v in cityDistanceDict.items() :
        if v < minVal :
            minVal = v
            cityFinder = k
    for k, v in puppyCityDict.items() :
        if v == cityFinder :
            return "Your new puppy, {}, is in {} {} miles away.".format(k,v,minVal)

#########################################
        
"""
Function Name: doubleOddhalfEven()
Parameters: numberList (list)
Returns: changedList (list)
"""

def doubleOddhalfEven(numberList) :
    if len(numberList) == 0 :
        return []
    else :
        num = numberList[0]
        if num % 2 == 0 :
            numberList[0] = int(num / 2)
        else :
            numberList[0] = int(num * 2)
    newLi = [numberList[0]] + doubleOddhalfEven(numberList[1:])
    return sorted(newLi)

#########################################

"""
Function Name: datingApp()
Parameters: profile1 (list), profile2 (list)
Returns: compatibility (float)
"""

def datingApp(profile1, profile2) :
    newLi = []
    datingGap = False
    count = 0
    #P1
    if profile1[1] >= profile2[1] :
        if profile1[1] - profile2[1] <= 5 :
            datingGap = True
    elif profile2[1] > profile1[1] :
        if profile2[1] - profile1[1] <= 5 :
            datingGap = True
    #P2
    if datingGap == True :
        for i in profile1[2] :
            newLi.append(i)
        for i in profile2[2] :
            if i in newLi :
                count += 1
            else :
                newLi.append(i)
        if count >= 3 :
            ratio = (count / len(newLi)) * 100
            ratio = round(ratio,1)
            return "You're {}% compatible!".format(str(ratio))

    return "Sorry, you're incompatible."

#########################################
    
"""
Function Name: simplestDirections()
Parameters: directions(str)
Returns: simple direction (str)
"""

def simplestDirections(directions) :
    #Setup
    leftrightCount = 0
    updownCount = 0
    moveOut = ""
    moveOutDU = ""
    #P1
    for i in directions :
        if i == "<" :
            leftrightCount -= 1
        elif i == ">" :
            leftrightCount += 1
        elif i == "U" :
            updownCount += 1
        elif i == "D" :
            updownCount -= 1
    #P2
    if updownCount > 0 :
        moveOutDU = "up"
    if leftrightCount > 0 :
        moveOut = "right"
    if updownCount < 0 :
        print(updownCount)
        updownCount *= -1
        moveOutDU = "down"
    if leftrightCount < 0 :
        leftrightCount *= -1
        moveOut = "left"
    if updownCount == 0 and leftrightCount == 0 :
        return "No movement."

    return "You have moved {} blocks {} and {} blocks {}.".format(updownCount,moveOutDU,leftrightCount,moveOut)

#########################################

"""
Function Name: songMystery()
Parameters: codedSong (str), songNames (list)
Returns: newSong (str)
"""

def songMystery(codedSong, songNames) :
    newSong = ""
    for i in songNames :
        if len(i) == len(codedSong) :
            return i.lower()
    return "I need more clues :("
    


    
            






            
        
