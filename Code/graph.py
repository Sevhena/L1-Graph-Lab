from IGraphBuilder import BuildGraph

class Graph:

    def __init__(self, graph):
        self.adjacency_list = BuildGraph(graph)

    def display(self):
        print(self.adjacency_list)

    def getAdjList(self):
        return self.adjacency_list
