"""
Function Name: currencyFinder()
Parameters: regionalBloc(str),currency(str)
Returns: how many countries use the given currency(str)
"""

#### SOLUTION CODE:

def currencyFinder(regionalBloc,currency):
    url = "https://restcountries.com/v2/regionalbloc/{}".format(regionalBloc)
    r = requests.get(url)
    data = r.json()
    num = 0
    aDict = {}
    for each in data:
        for i in each["currencies"]:
            if i["name"] == currency:
                num += 1
                aDict[currency] = num
    if aDict == {}:
        return "No countries in this region use the {}!".format(currency)
    elif aDict[currency] == 1:
        return "{} country uses the {}!".format(aDict[currency],currency)
    else:
        return "{} countries use the {}!".format(aDict[currency],currency)
        
        
#### TEST CASE(S):
currencyFinder("eu","Euro")
# '21 countries use the Euro!'
currencyFinder("NAFTA","United States dollar")
# '1 country uses the United States dollar!'
currencyFinder("eu","Mexican peso")
# 'No countries in this region use the Mexican peso!'

