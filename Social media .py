


# get the dimension of the query location i.e. latitude and logitude
# raise an exception of the given query Id not found in the input file
def getDimensionsofQueryLoc(inputFile, queryLocId):
    with open(inputFile) as infile:
        header = infile.readline().strip()
        headerIndex={ headerName.lower():index for index,headerName in enumerate(header.split(","))}
        for line in infile:
            values = line.strip().split(",")
            if values[headerIndex["locid"]].lower()==queryLocId:
                return float(values[headerIndex["latitude"]]),float(values[headerIndex["longitude"]]),values[headerIndex["category"]]
    return None,None,None
    
# Calculate the euclidean distance between 2 points
def calculateDistance(x1, y1, x2, y2):
    distance =((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**0.5
    return distance

# Calculate the standard deviation 
def getStandardDeviation(distSorted, avg):
    std = 0
    for distance in distSorted:
        std += (avg - distance)*(avg - distance)
    std/=len(distSorted)
    std=std**0.5
    return std

# All the distances are round off to 4 decimal place at the end
def main(inputFile,queryLocId,d1,d2):
    queryLocId=queryLocId.lower()

    #get the dimensions of the given query location id
    X1, Y1, category = getDimensionsofQueryLoc(inputFile, queryLocId)
    category=category.lower()

    if not X1:
        print("Invalid location ID")
        return [],[],[],[]

    # calculate the cordinates of top right and bottom left corner of the rectangle formed
    topRightX, topRightY = X1+d1, Y1+d2
    bottomLeftX, bottomLeftY = X1-d1, Y1-d2

    locList=[]    # list of location falls inside the rectangle
    simLocList=[] # list of locations with same category as given query location category
    distSorted=[] # list containing distance of locations in ascending order with same location category
    sumDistance=0 # sum of distances in distSorted list
    
    with open(inputFile) as infile:
        # next(infile) # skip the header row
        header = infile.readline().strip()
        headerIndex={ headerName.lower():index for index,headerName in enumerate(header.split(","))}
        for line in infile:
            values = line.strip().split(",")
            
            if not (values[headerIndex["latitude"]] and values[headerIndex["longitude"]]):
                continue
            
            # get dimensions of the iterated location
            X2, Y2 = float(values[headerIndex["latitude"]]), float(values[headerIndex["longitude"]])

            #check if the iterated location is not same as query location and it falls under the defined rectangle
            if values[headerIndex["locid"]].lower()!=queryLocId and X2<=topRightX and X2>=bottomLeftX and Y2<=topRightY and Y2>=bottomLeftY:
                #add the location to loclist
                locList.append(values[headerIndex["locid"]])
                #if location category is same then
                # 1. Add it to simList
                # 2. Calculate its distance with query location and add it to distSorted list
                # 3. Add its value to sumDistance (it will help in calculating the average distance)
                if values[headerIndex["category"]].lower() == category:
                    simLocList.append(values[headerIndex["locid"]])
                    distance=calculateDistance(X1, Y1 ,X2, Y2)
                    distSorted.append(distance)
                    sumDistance += distance

    if not distSorted:
        return simLocList,[],[],[]

    # calculate the average distance and the standard deviation of all the distances
    avg = sumDistance/len(distSorted);
    std = getStandardDeviation(distSorted, avg)
    # sort the distance list and return the result

    for i, dist in enumerate(distSorted):
        distSorted[i] = round(dist,4)

    return locList, simLocList, sorted(distSorted), [round(avg,4), round(std,4)]


