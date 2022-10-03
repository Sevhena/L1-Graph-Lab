from AstarAlgo import AstarAlgo

from graph import Graph
from MetricExtractor import*
from LondonGraphBuilder import*

class UrbanPlanning:
    def __init__(self,graph):
        self.graph = graph

        self.stations = {}
        for dict in self.graph.getAdjList().values():
            for row in dict.values(): 
                for edge in row:
                    self.stations[edge.getStart().getId()] = edge.getStart()
                    break
                break

        self.cc = []

    def getZones(self,stations):
        #getZones is a function that initializes a dictionary with all the possible zones that we have
        zones = {}
        for station in stations:
            zones[station] = stations[station].getZone()
        return zones
        
    def buildZones(self):
        #buildZones is a function that goes trhough the stations and places them into the getZones dictionary
        # for example, 1 in the dictionary represents zone 1, and would return the list of all stations that are in that zone
        zoneContent = {}
        zones = self.getZones(self.stations)
        for station in zones:
            zoneContent[zones[station]] = []

        for station in zones:
            zoneContent[zones[station]] += [station]
        return zoneContent

    def getCC(self):
        #this function returns the connected components list
        return self.cc
     
    def DFS(self,temp, node, visited,zone):
        #this function performs depth first search
        # it finds the connected compoenents of the the zone you pass 
        # into it (finds the islands of a desired islands)
        zones = self.buildZones()
        zoneNeeded = zones[zone]
        
        visited[node] = True

        if(node in zoneNeeded):
            temp.append(node)

        for adjacentEdgeList in self.graph.getAdjList()[node].values():
            for adjacentEdge in adjacentEdgeList:
                adjacentNode = adjacentEdge.getTo().getId()
                if(visited[adjacentNode] == False):
                    if(adjacentNode in zoneNeeded):
                        temp = self.DFS(temp,adjacentNode,visited,zone)
        return temp

    def connectedComponents(self,zone):
        # this is a function that finds the connected components
        # works with the DFS function.
        visited = {}

        for station in self.stations:
            visited[station] = False
        for i in visited:
            if visited[i] == False:
                temp = []
                self.cc.append(self.DFS(temp,i,visited,zone))

        cc = self.getCC()
        cc = [x for x in cc if x]
        return cc

    def getIsland(self, zone, node):
        # given a zone we find all the islands in that zone, and given a node we get the island it belongs to
        islands = self.connectedComponents(zone)
        for island in islands:
            if(node in island):
                return island
        
    def islandPath(self,start,end):
        # this function finds a path between 2 islands
        # we check if the 2 stations we are looking at are in the same island, if so then we say that we are already on the island
        # if they are not on the same island then we run A* to achieve a path, then we run through that path checking if any nodes
        # before the final node are on the same isalnd as the final node, if so then we return a path from the beginning to that node 
        # if not then we just return the A* path.
        a = AstarAlgo(self.graph, start)
        startIsland = self.getIsland(self.stations[start].getZone(),start)
        endIsland = self.getIsland(self.stations[end].getZone(),end)
        if(end in startIsland):
            print("Already on the island")
            return
        else:
            Apath = a.pathTo(end)
            path = [Apath[0]]
            for i in range(1,len(Apath)):
                if(Apath[i] in endIsland):
                    path.append(Apath[i])
                    return path
                path.append(Apath[i])
            return path



