from math import radians,sin,cos,asin,sqrt

class Graph:

    graphAdjList = {} 
    geoLocations = {} 

    def __init__(self,edges,locations):

        self.visited = []

        self.getLocations(locations)

        for edge in edges:
            
            station1 = edge[0]

            station2 = edge[1]

            line = edge[2]

            time = edge[3]

            self.addEdge(station1,station2,[line,time])

    def addEdge(self,node1,node2,lt):
        if node1 not in self.graphAdjList:
            self.graphAdjList[node1] = {}
        if node2 not in self.graphAdjList[node1]:
            self.graphAdjList[node1][node2] = []

        if node2 not in self.graphAdjList:
            self.graphAdjList[node2] = {}
        if node1 not in self.graphAdjList[node2]:
            self.graphAdjList[node2][node1] = []

        #if we are undirected then we should add the same code above
        #but reverse it so it applies backwards
        self.graphAdjList[node1][node2].append(lt)
        self.graphAdjList[node2][node1].append(lt)

    def getLocations(self,stations):
        for station in stations:
            self.geoLocations[station[0]] = [float(station[1]),float(station[2])]
    
    def getH(self,node,goalNode):
        long1 = radians(self.geoLocations[node][0])
        long2 = radians(self.geoLocations[goalNode][0])
        lat1 = radians(self.geoLocations[node][1])
        lat2 = radians(self.geoLocations[goalNode][1])
        
        dlon = long2 - long1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        
        c = 2 * asin(sqrt(a))

        r = 6371

        return (c*r)

    def aStarAlgo(self,startVertex,goalVertex):
        openList = set([startVertex])
        closedList = set([])

        gValues = {}
        gValues[startVertex] = 0

        adjacentMapping = {}
        adjacentMapping[startVertex] = startVertex

        while len(openList) > 0:
            # let the current node be nothing
            n = None

            # Check the openList for the node with the lowest value of f
            for node in openList:
                if n == None or gValues[node]+ self.getH(node, goalVertex) < gValues[n]+ self.getH(n,goalVertex):
                    # set the current node to the node with the lowest value of f
                    n = node
            # If after lookest for the lowest f value we find that there is nothing
            # then a path does not exist
            if n == None:
                return None
            # If the node with the lowest f value we found is the goalNode then retrace our steps
            if n == goalVertex:
                pathTaken = []
                while adjacentMapping[n] != n:
                    pathTaken.append(n)
                    n = adjacentMapping[n]
                pathTaken.append(startVertex)
                pathTaken.reverse()
                return pathTaken

            # Iterate through the children of the current node  
            for neighbor in self.graphAdjList[n]:
                # Here we get ready to get the weight
                for neighborW in self.graphAdjList[n][neighbor]:
                    #check if the child is in the open and the closed list
                    if(neighbor not in openList and neighbor not in closedList):
                        #Add the child to the open list
                        openList.add(neighbor)
                        adjacentMapping[neighbor] = n
                        #Assign the g value of the child in the g values list (Weight of the path so far + the weight of the current child)
                        gValues[neighbor] = gValues[n] + neighborW[1]
                    else:
                        # Here we see if it is faster to first visit the current node than the child
                        # if so we update the values
                        if(gValues[neighbor] > gValues[n] + neighborW[1]):
                            gValues[neighbor] = gValues[n] + neighborW[1]
                            adjacentMapping[neighbor] = n

                            #if the child is in the closed list move it to the open list
                            if(neighbor in closedList):
                                closedList.remove(neighbor)
                                openList.add(neighbor)

            #remove the current node from the openList
            #add the current node to the closed list as we are finsihed with it
            openList.remove(n)
            closedList.add(n)
        # after checking all paths if there is still no path
        return None










