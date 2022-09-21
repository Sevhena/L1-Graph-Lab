from GraphBuilders import *
from IShortestPath import ShortestPath
from SPAlgorithms import Dijkstra

class Itinerary:

    def __init__(self, start, destination):
        self.start = start
        self.destination = destination

    def shortestPath(self):
        shortest_path = ShortestPath(Dijkstra())
        pass



