#MAIN Module
from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
from Dijkstra import Dijkstra
from MetricExtractor import *
from Itinerary import Itinerary

import random

graph = Graph(LondonGraphBuilder())

start = 11
end = 44


itinerary = Itinerary(graph,numNodes(graph))

dijkstra = Dijkstra(graph, start, numNodes(graph))

path = itinerary.shortestPath(dijkstra,end)

#circle = random.sample(range(1,303),10)
# circle = [250,48,126,60,151,49,87,44,13]
# #print(circle)
# circlePath = itinerary.shortestCycle(circle)


# path = dijkstra.pathTo(end)

stationCount = 0
for edge in path:
    stationCount += 1
    print("<" + edge.start.name + "(", edge.start.id, ")" + ">\t\t","to\t", "<" + edge.to.name + "(", edge.to.id, ")" + ">")

#print(circlePath)
# for edge in circlePath:
#     stationCount += 1
#     # if edge.start.id in circle:
#     #     print("\nCheckpoint")
#     #     circle.remove(edge.start.id)
#     print("<" + edge.start.name + "(", edge.start.id, ")" + ">\t\t","to\t", "<" + edge.to.name + "(", edge.to.id, ")" + ">")

print("Edges:", len(path), "Station Count:", stationCount, "Travel Time:", dijkstra.timeTo[end], "Line Changes:", dijkstra.connectionsTo[end])
#print(graph.getAdjList().keys())

