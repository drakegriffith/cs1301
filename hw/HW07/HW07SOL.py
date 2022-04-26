
#File I/O
def featureActor(fileName, actorName) :
    #Setup
    movieList = []
    file = open(fileName, 'r')
    firstLine = file.readline()
    lineList = file.readlines()
    file.close()

    #Execute
    index = 0
    for item in lineList:
        index += 1
        if actorName in item:
            celebName = lineList[index - 2]
            celebName = celebName.replace('\n',"")
            movieList.append(celebName)
          
    if len(movieList) == 0:
        return "Actor not found"
   
    return movieList

def alphabetSearch(filename, letter) :
    #Setup
    file = open(filename, "r")
    firstLine = file.readline()
    lineList = file.readlines()`    `
    file.close()
    aDict = {}
    titleNum = 1 #Titles Appear Every 4 Turns >
    
    #Execute
    for item in lineList :
        if (titleNum + 4) < len(lineList) :
            titleNum += 4
            letterFi = lineList[titleNum]
            if letter == letterFi[0].lower() :
                movieName = lineList[titleNum]
                celebName = lineList[titleNum + 1]
                movieName = str(movieName)
                movieName = movieName.replace('\n',"")
                celebName = celebName.replace('\n',"")
                if celebName != "" :
                    aDict[movieName] = celebName
    if len(aDict) == 0:
        return "No movie tonight"

    return aDict

def favFilms(filename, movieList) :
    #Setup
    fileMe = open("favMovies.txt", "w")
    fileC = open(filename, "r")
    firstLine = fileC.readline()
    lineList = fileC.readlines()
    fileC.close()
    
    #Execute
    fileMe.write("Movie Data")
    index = 0
    tally = 0
    for item in lineList :
        index += 1
        for i in movieList :
            if i in item :
                fileMe.write("\n")
                fileMe.write("\n")
                movieData = (lineList[index - 1 : index + 1])
                #Strip \n from Genre Category
                genre = str(lineList[index + 1])
                genre = genre.replace('\n',"")
                movieData.append(genre)
                for data in movieData :
                    fileMe.write(data)
                
    return None

#CSV

def movieNight(filename, timeLimit) :
    #Setup
    movieA = (),
    file = open(filename, "r")
    firstLine = file.readline()
    lineList = file.readlines()
    hiRating = 0
    hiMovie = ""
    file.close()
    
    #Execute
    for item in lineList :
        line = item.strip()
        line = item.split(",")
   
        if int(line[3]) <= int(timeLimit) :
            aveRating = (int(line[1]) + int(line[2])) / 2
            if aveRating > hiRating :
                hiRating = aveRating
                hiMovie = line[0]
        elif timeLimit < 95 :
            return "Can't do movie night on Friday"
            
        movieA = (hiMovie, hiRating )
    return (movieA)


def movieRecs(filename, interestedList, expectedRatio) :
    file = open(filename, "r")
    firstLine = file.readline()
    lineList = file.readlines()
    aDict = {}
    file.close()
    for item in lineList :
        line = item.strip()
        line = item.split(",")
        aRating = (int(line[1]) + int(line[2])) / 2
        if (aRating / float(line[3])) >= expectedRatio :
            for i in range(len(interestedList)) :
               
                
                if interestedList[i] in item:
                    point = line[3]
                    point = point.replace('\n',"")
                    point = int(point)
                    aDict[line[0]] = point

    if len(aDict) == 0:
        return "Too many expectations"

    return aDict



            

                



