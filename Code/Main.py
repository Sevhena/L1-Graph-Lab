#MAIN Module
from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
from Dijkstra import Dijkstra

graph = Graph(LondonGraphBuilder())

print(graph.getAdjList())