#MAIN Module
from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
from Dijkstra import Dijkstra
from MetricExtractor import *

graph = Graph(LondonGraphBuilder())

start = 46
end = 4

Dijkstra(graph, start, numNodes(graph))

dijkstra = Dijkstra(graph, start, numNodes(graph))


path1,path2 = dijkstra.pathTo(end)

print("Path 1")
for edge in path1:
    print(edge.start.name,"to", edge.to.name)

print("Path 2")
for edge in path2:
    print(edge.start.name,"to", edge.to.name)

print(dijkstra.timeTo[end])
print(dijkstra.timeToC[end], dijkstra.connectionsTo[end])
#print(graph.getAdjList().keys())