from AstarAlgo import AstarAlgo
from Dijkstra import Dijkstra
from graph import Graph
from LondonGraphBuilder import LondonGraphBuilder


class Astar:

    graph = Graph(LondonGraphBuilder())
    def algo(self):
        return AstarAlgo(self.graph)
        

class Djikstra:
    graph = Graph(LondonGraphBuilder())
    def algo(self):
        return Dijkstra(self.graph)