from Dijkstra import Dijkstra

from MetricExtractor import numNodes
import random


class Itinerary:

    def __init__(self, graph):
        self.graph = graph
        self.numNodes = numNodes(graph)
        #self.aStar = AStar()

    def shortestPath(self, pathFinder, destination):
        return pathFinder.pathTo(destination)

    def shortestCycle(self, nodes):
        path = []
        travelled = {}
        startNode = random.choice(nodes)
        firstNode = startNode
        #print(startNode)
        travelled[startNode] = True
        

        while not all(node in travelled.keys() for node in nodes):
            dijkstra = Dijkstra(self.graph, startNode)

            #print("check 1")

            minDistNode = 0
            for node in nodes:
                if travelled.get(node) == None:
                    if dijkstra.timeTo[node] < dijkstra.timeTo[minDistNode]:
                        #print("check 2")
                        minDistNode = node

            print(minDistNode)
            travelled[minDistNode] = True
            path += self.shortestPath(dijkstra, minDistNode)
            startNode = minDistNode

            if all(node in travelled.keys() for node in nodes):
                path += self.shortestPath(Dijkstra(self.graph, minDistNode), firstNode)
                #print("check 3")

        print(len(path))
        return path
