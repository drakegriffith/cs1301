#### HOMEWORK PROBLEM 2

"""
Function Name: moveCharacter()
Parameters: keystrokes (str)
Returns: whether character is in same place (boolean)
"""

#### SOLUTION:
def moveCharacter(keystrokes): 
    for key in keystrokes:
        if key == '>':
            movement += 1
        elif key == '<':
            movement -= 1
            
    if movement == 0: 
        return True
    else: 
        return False
    
#### TEST CASE(S):
moveCharacter("<><<><<<<<>><<")
# False
moveCharacter("<<<<<<>>>>>>")
# True
