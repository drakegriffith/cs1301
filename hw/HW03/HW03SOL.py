"""
Georgia Institute of Technology - CS1301
HW03 - Iterations
"""

#########################################

"""
Function Name: avgTotal()
Parameters: numString(str)
Returns: average(float)
"""

def avgTotal(numstring):
    singleNum = str(numstring)
    total = 0 #Using a Counter like Total is FANTASTIC
    if numstring != "" :
        for c in singleNum :
            c = int(c)
            total += c
        total = total / int(len(singleNum))       
    else :
        total = float(0)
    return total

#########################################

"""
Function Name: safeDecoder()
Parameters: characterString(str)
Returns: passcodeString(str)
"""

def safeDecoder(characterString):
    safe = str(characterString)
    total = -1 #EX2 of Total Counter
    stringMe = str("")
    for c in safe :
        total += 1
        if c.isdigit() :
            stringMe += str(total) #A Loop of Pure Concatenation of Strings
    return stringMe
    
#########################################

"""
Function Name: testScore()
Parameters: test1(str), test2(str)
Returns: maxPercentage(float)
"""

def testScore(test1, test2):
#Variable Define
    maxscore = 25
    totalone = 0 
    totaltwo = 0 #More Total Counters
    testOne = str(test1)
    testTwo = str(test2)

#Find Test Scores
    for c in testOne :
        if c != "_" :
            c = int(c)
            totalone += c
    finalScoreT1 = (totalone / maxscore) * 100

    for c in testTwo :
        if c != "_" :
            c = int(c)
            totaltwo += c
    finalScoreT2 = (totaltwo / maxscore) * 100

#Compare
    if finalScoreT1 > finalScoreT2 :
        return float(finalScoreT1)
    elif finalScoreT1 < finalScoreT2 :
        return float(finalScoreT2)
    else :
        return 'Same Percentage'
        
#########################################

"""
Function Name: trip()
Parameters: tripTotalCost(float), bankBalance(float), interestRate(float)
Returns: months(int)
"""

def trip(tripTotalCost, bankBalance, interestRate) :
    monthlyGrow = float(bankBalance) * float((interestRate / 100) + 1)
    month = 1 #Counter
    while tripTotalCost != monthlyGrow :
        monthlyGrow *= float((interestRate / 100) + 1)
        month += 1
        if tripTotalCost <= monthlyGrow :
            break
    return month


#########################################      

"""
Function Name: rightTriangles()
Parameters: numRows(int), character(str)
Returns: None
"""

def rightTriangles (numRows, character) :
    total = 1 #Counter
  
    if character == '':
        print("No Triangle")
    elif numRows == 0 or numRows == 1 :
        print("No Triangle")
     
    else :
        for c in range(numRows) :
            totalCharacter = (character * total)
            print(totalCharacter)
            total += 1

        

    



    
            
    


       

