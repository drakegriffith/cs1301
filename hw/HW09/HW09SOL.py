
"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""

#########################################

"""
Function Name: pageNumbers()
Parameters: bookList (list)
Returns: total (int)
"""

def pageNumbers(bookList) :
    if len(bookList) == 0: 
        return 0
    else :
        return bookList[0] + pageNumbers(bookList[1:4]) 

#########################################

"""
Function Name: letterPyramid()
Parameters: letter (str), rows (int)
Returns: None (NoneType)
"""

def letterPyramid(letter, rows) :
    if rows == 1: 
        return {}
    else:
        if letter.lower() == letter and letter.isalpha():
            letterPyramid(letter, rows-1)
            print(letter *rows)
            
#########################################
        
"""
Function Name: specialChar()
Parameters: usernames (list)
Returns: aDict (dict)
"""

def specialChar(usernames) :
    if len(usernames) == 0 : 
        return {}
    else :
        speciCount = 0
        for i in usernames[0] :
            if i in ".~-_!#" :
                speciCount += 1

        rememberName = usernames[0]
        usernames.pop(0)
        aDict = specialChar(usernames)
        aDict[rememberName] = speciCount
    return aDict
  
        
#########################################

"""
Function Name: messageDecoder()
Parameters: hiddenMessage (str), characters (str)
Returns: decodedMessage (str)
"""

def messageDecoder(hiddenMessage, characters) :
    for i in hiddenMessage :
        if i in characters :
            hiddenMessage = hiddenMessage.replace(str(i), "")
            messageDecoder(hiddenMessage, characters)
        else :
            continue
        
    return hiddenMessage
            
#########################################

"""
Function Name: stringCombiner()
Parameters: stringList (list)
Returns: combinedString (str)
"""

def stringCombiner(stringList) :
    for i in range(len(stringList)) : #Base Case
        if len(stringList) == 0:
            return {}
        
        firstElement = stringList[0]
       
        if type(firstElement) == str: 
            stringList = stringList[1:len(stringList)]

            if len(stringList) == 1: #Evade Concatination str + Nonetype Error
                if type(stringList) == tuple or type(stringList) == list:
                    return firstElement + str(stringList[0][0])
                else :
                    return firstElement + str(stringList[0])

            return firstElement + stringCombiner(stringList)
    
        elif type(firstElement) == list or type(firstElement) == tuple: 
            firstElement = stringList[0][0]
            stringList = stringList[1:len(stringList)] 

            if len(stringList) == 1: #Evade Concatination str + Nonetype Error
                if type(stringList) == tuple or type(stringList) == list:
                    return firstElement + str(stringList[0][0])
                else :
                    return firstElement + str(stringList[0])
                
            return firstElement + stringCombiner(stringList)
        


        



    
        



        
    
        

    
    
    


