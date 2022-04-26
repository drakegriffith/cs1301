
"""
Georgia Institute of Technology - CS1301
HW01 - Functions & Expressions
"""

#########################################


"""
Function Name: dinnerTime()
Parameters: N/A
Returns: None
"""

def dinnerTime():
    # number of entrees and drinks ordered
    entrees = input("How many entrees will you be ordering? ")
    drinks = input("How many drinks will you be ordering? ")

    #convert entrees and drinks into money
    eprice = float(entrees) * 12
    dprice = float(drinks) * 4.5

    #combine and print
    total = float(dprice) + float(eprice)
    print("The total cost of all the meals and drinks is $" + str(total) + ".")

#########################################

"""
Function Name: bottleBonanza()
Parameters: N/A
Returns: None
"""

def bottleBonanza() :

    #define pi, radius, and height
    pi = 3.14
    r = input("What is the radius of the water bottle? ")
    h = input("What is the height of the water? ")

    #define radius squared and volume
    rr = float(r)*float(r)
    V = float(pi)*(rr)*float(h)

    #round volume to two decimals and print
    rounded_V = round(V,2)
    print("The volume of the water bottle is " + str(rounded_V) + ".")

#########################################

"""
Function Name: winterBreak()
Parameters: N/A
Returns: None
"""
              
def winterBreak() :
    #p1 how many neflix and youtube watched
    netflix = input("How many episodes did you watch? ")
    youtube = input("How many YouTube videos did you watch? ")

    #scale to 40 min for netflix & 10 for youtube
    minflix = int(netflix) * 40
    mintube = int(youtube) * 10

    #combine and split into hours and minutes and print
    total = mintube + minflix
    hour = int(total) // 60
    minute = int(total) % 60
   
    print("You spent " + str(hour) + " hours and " + str(minute) + " minutes watching Netflix and YouTube over winter break.")

#########################################

"""
Function Name: skateboardMoney()
Parameters: N/A
Returns: None
"""

def skateboardMoney() :
    #create allowance and finds allowance after percentage saved
    allowance = input("How much is your monthly allowance? ")
    percentallow = input("What percentage of your allowance do you want to save? ")
    percentdecimal = float(percentallow) * .01
    newallowance = float(allowance) * (1-percentdecimal)
    rounded_allow = round(newallowance,1)
    
    #how much money left over for skateboard
    newestallowance = float(newallowance) - 311.7
    rounded_newest = round(newestallowance,1)
    print("You'll have $" + str(rounded_newest) + " left to spend on your skateboard after savings and fees.")



