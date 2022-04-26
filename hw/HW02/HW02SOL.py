
"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################


"""
Function Name: workout()
Parameters: exerciseName (str), interestedFriends (int), totalFriends (int)
Returns: None (NoneType)
"""

def workout(exerciseName, interestedFriends, totalFriends) :
    if int(interestedFriends) / int(totalFriends) < .20 :
        print("Let's try a different workout.")
    elif (int(interestedFriends) / int(totalFriends) >= .20) and (int(interestedFriends) / int(totalFriends) < .70) :
        print("We will try to {} for 30 minutes.".format(str(exerciseName)))
    elif (int(interestedFriends) / int(totalFriends) >= .70) and (int(interestedFriends) / int(totalFriends) <= 1) :
        print("We are so excited to {}!".format(str(exerciseName)))
    


#########################################
        
"""
Function Name: iceCream()
Parameters: rating (float), distance (float)
Returns: choice (str)
"""

def iceCream(rating, distance) :
    if rating == 4.5 and distance == 7.5:
        return("Jeni's")
    elif rating == 4.5 and distance == 3.6:
        return("Cold Stone")
    elif rating == 4.5 and distance == 4.2:
        return("Morelli's")
    elif rating == 4.0 and distance == 1.3 :
        return("Bruster's")
    elif rating == 4.0 and distance == 6.4 :
        return("Sweet Stack")
    elif rating == 3.5 and distance == 2.8 :
        return("Baskin Robbins")
    else :
        return("Try again tomorrow.")



#########################################

"""
Function Name: restaurantDecider()
Parameters: veganFriendly (bool), yelpStars (int), milesAway (int)
Returns: decisionStr (str)
"""

def restaurantDecider(veganFriendly, yelpStars, milesAway) :
    if veganFriendly == False :
        return("Not tonight.")
    if veganFriendly == True and yelpStars < 3:
        return("Not good enough food.")
    if veganFriendly == True and yelpStars >= 3 and milesAway > 5 :
        return("Too far!")
    if veganFriendly == True and yelpStars >= 3 and milesAway <= 5 :
        return("Perfect restaurant!")

#########################################

"""
Function Name: dinnerTip()
Parameters: numFriends (int), dinnerCost (float)
Returns: tipAmount (float)
"""
def dinnerTip(numFriends, dinnerCost) :
    if numFriends <= 3 and numFriends > 0:
        newtip = float(dinnerCost) * .15
        roundvar = round(newtip, 2)
        return roundvar
    elif numFriends > 3 and numFriends <= 7:
        newtip = float(dinnerCost) * .20
        roundvar = round(newtip, 2)
        return roundvar
    elif numFriends > 7:
        newtip = float(dinnerCost) * .25
        roundvar = round(newtip, 2)
        return roundvar
    else :
        return 0
    

#########################################

"""
Function Name: planMaker()
Parameters: timeA (float), costA (int), timeB (float), costB (int)
Returns: planDecision (str)
"""

def planMaker(timeA, costA, timeB, costB) :
    if costA < costB :
        return("planA")
    elif costB < costA :
        return("planB")
    elif costA == costB :
        if timeA < timeB :
            return("planA")
        if timeB < timeA :
            return("planB")
        if timeA == timeB :
            return("No plans this weekend.")


