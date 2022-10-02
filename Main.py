#MAIN Module
import time
import tracemalloc
from Code.LondonGraphBuilder import LondonGraphBuilder
from UrbanPlanning import UrbanPlanning
from Code.graph import Graph
from Code.Dijkstra import Dijkstra
from Code.AstarAlgo import AstarAlgo

graph = Graph(LondonGraphBuilder())
stations = LondonGraphBuilder().read_London_Station()
up = UrbanPlanning(graph,stations)
a = AstarAlgo(graph,4)





