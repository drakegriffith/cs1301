"""
Function Name: bagCheck()
Parameters: amount (str)
Returns: whether user has sufficient amount to purchase bag dict (boolean)
"""

#### SOLUTION CODE:

def bagCheck(amount) :
    fruit = ["banana","apple","peaches"]
    vegetable = ["broccoli", "spinach", "cabbage"]
    total = 0
    for k, v in bag.items() :
        for i in fruit :
            if i == k.lower() :
                total += (v * 1.20)
        for i in vegetable :
            if i == k.lower() :
                total += (v * .7)
    if amount >= total :
        return True
    else :
        return False

#### TEST CASE(S)
bag = {"Banana" : 3, "Peaches": 4, "Broccoli" : 7 }
bagCheck(15)
# True
bag = {"Spinach" : 4, "Apple": 4, "Cabbage" : 7 }
bagCheck(10)
# False
