

"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries adn Try/Except Blocks
"""

#########################################
"""
Function Name: findTicket()
Parameters: ticketDictionary (dict)
Returns: cheapestTicket (tuple)
"""

def findTicket(ticketDictionary):
    if len(ticketDictionary) == 0:
        return "No tickets available!"
    
    for key, value in ticketDictionary.items() :
        name = ""
        cheapestPrice = value
        for i in ticketDictionary.values() :
            if i < cheapestPrice :
                cheapestPrice = i
        if value == cheapestPrice:
            name = str(key)
            cheapestTicket = (name,cheapestPrice)

    return cheapestTicket
       
#########################################
"""
Function Name: findHotel()
Parameters: hotelDictionary (dict)
Returns: preferredHotel (dict)
"""

def findHotel(hotelDictionary):
    newList = list(hotelDictionary.values())
    finalDict = {}
    numDict = {}
    for hotel in newList :
        numDict[hotel] = newList.count(hotel)
        print(newList.count(hotel))
        return numDict
    if numDict == {} :
        return "No hotels available!"

#########################################
"""
Function Name: findEvent()
Parameters: myInterests (list), schedule (dict)
Returns: match (list)
"""

def findEvent(myInterest, schedule) :
    li = []
    for key, events in schedule.items() :
        for i in myInterest :
            if i in events :
                li.append(key)
                break
    li.sort()
    return li

#########################################

"""
Function Name: figureSkating()
Parameters: technicalScores (list), componentScores (list)
Returns: finalScores (list)
"""


def figureSkating(technicalScores, componentScores) :
    li = []
    for i in range(len(technicalScores)) :
        try:
            totali = technicalScores[i] + componentScores[i]
            li.append(totali)
            continue
        except TypeError :
            continue
    return li



#########################################
"""
Function Name: sportManagement()
Parameters: countryDict (dict)
Returns: sportDict (dict)
"""

countryDict = {"Belarus": ["Ice Hockey", "Skiing"], 
                            "Lebanon": ["Skiing", "Snowboard"], 
                            "Denmark":["Skiing", "Luge"]} 
def sportManagement(countryDict) :
    sportDict = {}
    
    for key, events in countryDict.items() :
        for i in events :
            if i in sportDict :
                sportDict[i].append(key)
                
                continue
            sportDict[i] = [key]
            print(sportDict)
    sportDict = {i: sorted(j) for i, j in sportDict.items()}
    return sportDict


print(sportManagement(countryDict))
           
            
            
            

            



        
