"""
Function Name: rainCheck()
Parameters: days (int)
Returns: whether rain has occured in x days with (1/x)% per day. (str)
"""

import random

#### SOLUTION CODE

def rainCheck (days) :
    total = 0
    for i in range(days) :
        randRain = random.randint(1,days)
        total += 1
        if randRain == 1 :
            return "Rain is here on day {}!".format(total)
    return "No rain for now."

#### TEST CASE(S):
rainCheck(10)
# 1/10 % for rain per day for 10 days
rainCheck(88)
# 1/88 % for rain per day for 88 days.
# Either returns "Rain is here on day {}" or "No rain for now." Return day # if True.
