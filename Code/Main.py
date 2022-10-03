#MAIN Module
import time
from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
from Dijkstra import Dijkstra
from AstarAlgo import AstarAlgo
from MetricExtractor import *
from Itinerary import Itinerary

import random

graph = Graph(LondonGraphBuilder())
len(graph.getAdjList())

start = 4
end = 11


dijkstra = Dijkstra(graph, start)
astar = AstarAlgo(graph, start)

start_time = time.time()

dijkstra.pathTo(end)

end_time = time.time()

print("Dijkstra : ",(end_time-start_time)*1000)

start_time = time.time()

astar.pathTo(end)

end_time = time.time()

print("A star : ",(end_time-start_time)*1000)




print("Dijkstra : ",(end_time-start_time)*1000)

# path = itinerary.shortestPath(dijkstra,end)

# #circle = random.sample(range(1,303),10)
# # circle = [250,48,126,60,151,49,87,44,13]
# # #print(circle)
# # circlePath = itinerary.shortestCycle(circle)


# # path = dijkstra.pathTo(end)

# stationCount = 0
# for edge in path:
#     stationCount += 1
#     print("<" + edge.start.name + "(", edge.start.id, ")" + ">\t\t","to\t", "<" + edge.to.name + "(", edge.to.id, ")" + ">")

# #print(circlePath)
# # for edge in circlePath:
# #     stationCount += 1
# #     # if edge.start.id in circle:
# #     #     print("\nCheckpoint")
# #     #     circle.remove(edge.start.id)
# #     print("<" + edge.start.name + "(", edge.start.id, ")" + ">\t\t","to\t", "<" + edge.to.name + "(", edge.to.id, ")" + ">")

# print("Edges:", len(path), "Station Count:", stationCount, "Travel Time:", dijkstra.timeTo[end], "Line Changes:", dijkstra.connectionsTo[end])
# #print(graph.getAdjList().keys())

