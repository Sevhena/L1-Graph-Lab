from IShortestPath import ShortestPath

import random
from Dijkstra import Dijkstra

class Itinerary:

    def __init__(self, graph, numNodes):
        self.graph = graph
        self.numNodes = numNodes
        #self.aStar = AStar()

    def shortestPath(self, pathFinder, destination):
        return pathFinder.pathTo(destination)

    def shortestCycle(self, nodes):
        path = []
        travelled = {}
        startNode = random.choice(nodes)
        travelled[startNode] = True

        while all(node in travelled for node in nodes):
            dijkstra = Dijkstra(self.graph, startNode,self.numNodes)

            minDistNode = float('inf')
            for node in nodes:
                if travelled.get(node) == None:
                    if dijkstra.timeTo[node] < dijkstra.timeTo[minDistNode]:
                        minDistNode = node

            travelled[minDistNode] = True
            path += self.shortestPath(dijkstra, minDistNode)

            if all(node in travelled for node in nodes):
                path += self.shortestPath(Dijkstra(self.graph, minDistNode, self.numNodes), startNode)

        



## NOT DONE

