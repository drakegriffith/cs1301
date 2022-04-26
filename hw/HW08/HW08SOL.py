import requests

"""
Georgia Institute of Technology - CS1301
HW08 - API
"""

#########################################

"""
Function Name: highestPopulation()
Parameters: regionalBloc (str)
Returns: country with highest population (str)
"""

def highestPopulation(regionalBloc) :
    url = "https://restcountries.com/v2/regionalbloc/{}".format(regionalBloc)
    request = requests.get(url)
    data = request.json()
    index = 0
    maxv = 0
    liPop = []
    liName = []

    for c in range(len(data)) :
        index += 1
        din = data[c]
        pop = din["population"]
        name = din["name"]
        liName.append(name)
        liPop.append(pop)

    maxPop = max(liPop)
    for c in range(len(liPop)) :
        if liPop[c] == maxPop :
            return liName[c]

#########################################
        
"""
Function Name: commonTimeZones()
Parameters: code1(str) , code2(str)
Returns: list of common time zones (list)
"""

def commonTimeZones(code1, code2) :
    #Sep
    urlX = "https://restcountries.com/v2/alpha?codes={}".format(code1)
    urlY = "https://restcountries.com/v2/alpha?codes={}".format(code2)
    requestX = requests.get(urlX)
    requestY = requests.get(urlY)
    dataX = requestX.json()
    dataY = requestY.json()
    similarTZ = []
    listX = []
    listY = []
    
    for c in range(len(dataX)) :
        dinX = dataX[c]
        zoneX = dinX["timezones"]
        listX.append(zoneX)
        
    for c in range(len(dataY)) :
        dinY = dataY[c]
        zoneY = dinY["timezones"]
        listY.append(zoneY)

    uplistX = listX[0]
    uplistY = listY[0]
   
    #Find Common 
    if len(uplistX) > len(uplistY) :
        for c in range(len(uplistX)) :
            if uplistX[c] in uplistY :
                similarTZ.append(uplistX[c])
            
    elif len(uplistY) >= len(uplistX) :
        for c in range(len(uplistY)) :
            if uplistY[c] in uplistX :
                similarTZ.append(uplistY[c])

    if len(similarTZ) == 0 :
        return 'No Common Time Zones'
    return similarTZ

#########################################

"""
Function Name: registerDomains()
Parameters: companyName (str), countryList (list)
Returns: list of domain names (list)
"""

def registerDomains(companyName, countryList) :
    li = []
    for c in range(len(countryList)) :
        url = "https://restcountries.com/v2/name/{}?fullText=true".format(countryList[c])
        request = requests.get(url)
        data = request.json()
                     
        try :
            for dataloop in range(len(data)) :
                din = data[dataloop]    
            
            domainCode = din["topLevelDomain"]
            domainCode = domainCode[0]
            full = str(companyName.lower()) + str(domainCode)
            li.append(full)
        except :
            continue
    return li

#########################################

"""
Function Name: findCountry()
Parameters: capitalList (list)
Returns: Dictionary mapping each capital to its country(dict)
"""

def findCountry(capitalList) :
    dic = {}
    for c in range(len(capitalList)) :
        url = "https://restcountries.com/v2/capital/{}".format(capitalList[c])
        request = requests.get(url)
        data = request.json()

        for dataloop in range(len(data)) :
            din = data[dataloop]

        name = din["name"]
        dic[capitalList[c]] = name

    return dic

#########################################

"""
Function Name: commonLanguages()
Parameters: regionalBloc (str)
Returns: most common language (str) or languages (list)
"""

def commonLanguages(regionalBloc) :
    li = []
    url = "https://restcountries.com/v2/regionalbloc/{}".format(regionalBloc)
    request = requests.get(url)
    data = request.json()
    for c in range(len(data)) :
        din = data[c]
        
        for x in range(len(din["languages"])) :
            lanCount = din["languages"][x]["name"]
            li.append(lanCount)
             
    counterLi = []
    nameCount = []
    newLi = []
    finalLi = []
    for c in range(len(li)) :
        if li[c] in nameCount :
            continue
        else :
            counter = li.count(li[c])
            counterLi.append(counter)
            nameCount.append(li[c])

    maxLi = max(counterLi)
    for c in range(len(counterLi)) :
        if counterLi[c] == maxLi :
            newLi.append(c)
    for c in range(len(newLi)) :
        countries = (nameCount[newLi[c]])
        
        finalLi.append(countries)
    finalLi.sort()

    if len(finalLi) == 1 :
        return finalLi[0]
    return finalLi


    


    
    
