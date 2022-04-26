
"""
Georgia Institute of Technology - CS1301
HW04 - Strings and Lists
"""
#########################################

"""
Function Name: messageDecoder()
Parameters: message (str)
Returns: decodedMessage (str)
"""

def messageDecoder(message):
    newmessage = str(message)[::-1]
    decodedMessage = ''
    count = 0
    for c in newmessage :
        if c.isalpha() :
            decodedMessage += str(c)
            count += 1
            continue
        if c == " " :
            decodedMessage += " "
            continue
        if count == 0 :
            return 'No message'
    return decodedMessage

#########################################

"""
Function Name: clubMembers()
Parameters: interested (list), recruits (list)
Returns: memberList (list)
"""

interested = []
recruits = ['Neville', 'Lee', 'Susan', 'Padma']
def clubMembers(interested, recruits) :
    memberList = []
    memberMe = []
    for c in range(len(interested)) :
        memberList.append(interested[c])
    interested.sort()
    if len(interested) == 0 :
        for c in range(len(recruits)):
            memberList.append(recruits[c])
        return memberList
    if len(interested) <= len(recruits) :
        for c in range(len(recruits)) :
            if recruits[c] not in interested :
                memberMe.append(recruits[c])
    if len(interested) > len(recruits) :
        for c in range(len(recruits)) :
            if recruits[c] not in interested :
                memberMe.append(recruits[c])
    memberList = memberList + memberMe
    return memberList

#########################################

"""
Function Name: checkCareer()
Parameters: students (list), career (str)
Returns: selectedStudents (list)
"""


students = [["Harry", "Auror"], ["Ron", "Auror"], ["Seamus", "Curse Breaker"]]

def checkCareer(students, career) :
    selectedStudents = []
    for c in range(len(students)) :
        if career in students[c] :
            del students[c][1]
            selectedStudents += students[c]
    return selectedStudents

#########################################

"""
Function Name: highGrades()
Parameters: students (list), gpas (list)
Returns: honorsStudents (list)
"""

students = ["Hermione", "Ron", "Ginny", "Fred", "Neville", "Draco"] 
gpas = [4.0, 2.8, 3.8, 2.3, 3.6, 3.4] 
def highGrades(students, gpas) :
    honorStudents = []
    for c in range(len(students)):
        if gpas [c] >= 3.5:
            honorStudents.append(students[c])
    return honorStudents

#########################################

"""
Function Name: quidditchPlay()
Parameters: playOrder (list), partners (list)
Returns: isApproved (bool)
"""
playerOrder = ['George', 'Fred', 'George', 'Fred', 'George']
partners = ['Ron', 'George']
def quidditchPlay(playerOrder, partners) :
    for c in range(len(playerOrder)) :
        if c<len(playerOrder)-1:
            if playerOrder[c] in partners and playerOrder[c+1] in partners:
                return True
            else :
                pass
        elif c>=1 :
            if playerOrder[c] in partners and playerOrder[c-1] in partners:
                return True
            else :
                pass
    return False
   

        
        
        

  



    
