from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
from math import radians,sin,cos,asin,sqrt

class AstarAlgo:

    geoLocations = {}

    def __init__(self,graph):
        self.graph = graph
        self.stations = LondonGraphBuilder().read_London_Station()
        self.getGeoLocations(self.stations)

    def getGeoLocations(self,stations):
        # this function adds the gepLocatoions dictionary each station, and its value is a list
        # of the latitide and longitude of that station
        for station in stations:
            self.geoLocations[station] = [stations[station].getLatitude(),stations[station].getLongitude()]

    def getH(self,node,goalNode):
        # the A* algorithm chooses which node to go to base on a g value and and h value
        # the g value is the weight so far of the travel, and the H is the distance from that node to the final node
        # this function caluates that distance
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

    def aStarAlgo(self,startNode,goalNode):
        openList = set([startNode])
        closedList = set([])

        gValues = {}
        gValues[startNode] = 0

        adjacentMapping = {}
        adjacentMapping[startNode] = startNode

        while len(openList) > 0:
            # let the current node be nothing
            n = None

            # Check the openList for the node with the lowest value of f
            for node in openList:
                if n == None or gValues[node]+ self.getH(node, goalNode) < gValues[n]+ self.getH(n,goalNode):
                    # set the current node to the node with the lowest value of f
                    n = node
            # If after lookest for the lowest f value we find that there is nothing
            # then a path does not exist
            if n == None:
                return None
            # If the node with the lowest f value we found is the goalNode then retrace our steps
            if n == goalNode:
                pathTaken = []
                while adjacentMapping[n] != n:
                    pathTaken.append(n)
                    n = adjacentMapping[n]
                pathTaken.append(startNode)
                pathTaken.reverse()
                return pathTaken

            # Iterate through the children of the current node  
            for adjacentEdge in self.graph.getAdjList()[n]:
                print("Hello ", adjacentEdge)
                # Here we get ready to get the weight
                adjacentNode = adjacentEdge.getTo().getId()
                weight = adjacentEdge.getTime()
                #check if the child is in the open and the closed list
                if(adjacentNode not in openList and adjacentNode not in closedList):
                        #Add the child to the open list
                    openList.add(adjacentNode)
                    adjacentMapping[adjacentNode] = n
                        #Assign the g value of the child in the g values list (Weight of the path so far + the weight of the current child)
                    gValues[adjacentNode] = gValues[n] + weight
                else:
                        # Here we see if it is faster to first visit the current node than the child
                        # if so we update the values
                    if(gValues[adjacentNode] > gValues[n] + weight):
                        gValues[adjacentNode] = gValues[n] + weight
                        adjacentMapping[adjacentNode] = n

                            #if the child is in the closed list move it to the open list
                        if(adjacentNode in closedList):
                            closedList.remove(adjacentNode)
                            openList.add(adjacentNode)

            #remove the current node from the openList
            #add the current node to the closed list as we are finsihed with it
            openList.remove(n)
            closedList.add(n)
        # after checking all paths if there is still no path
        return None