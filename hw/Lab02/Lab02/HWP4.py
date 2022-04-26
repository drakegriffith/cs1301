"""
Function Name: asciiTech()
Parameters: gt (str)
Returns: BOO or GOO TECH! 
"""

#SOLUTION CODE

def asciiTech (gt) :
    f = open("/Users/drakegriffith/Desktop/Lab02/ascii-artgt.txt", 'r')
    lineList = f.readlines()
    f.close()
    if gt == "georgia tech" or gt == "gt" :
        for i in lineList :
            print(i)
        return "GOO TECH!"
    elif gt == "uga" :
        f = open("/Users/drakegriffith/Desktop/Lab02/ascii-artuga.txt")
        lineList = f.readlines()
        f.close()
        for i in lineList :
            print(i)
        return "BOOO!"

#TEST CASE(S)
asciiTech("gt")
#*GT Logo Ascii Art + returns "GOO TECH!"
asciiTech("uga")
#*UGA Logo Ascii Art + returns "BOOO!"
