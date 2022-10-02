#MAIN Module
from LondonGraphBuilder import LondonGraphBuilder
from UrbanPlanning import UrbanPlanning
from graph import Graph
from Dijkstra import Dijkstra
from AstarAlgo import AstarAlgo

graph = Graph(LondonGraphBuilder())
stations = LondonGraphBuilder().read_London_Station()
up = UrbanPlanning(graph,stations)
a =AstarAlgo(graph)

print(a.aStarAlgo(4,70))



