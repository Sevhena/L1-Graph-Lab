# import the graphbuilder

#use extracor to aquire the stations

#use extractor to obtain the connections

#build the graph
from GraphBuilders.LondonGraphBuilder import LondonGraphBuilder
from IGraphBuilder import BuildGraph



class Graph:

    def __init__(self):
        self.adjacency_list = BuildGraph(LondonGraphBuilder())

    def display(self):
        print(self.adjacency_list)

    def getAdjList(self):
        return self.adjacency_list

#print(BuildGraph(LondonGraphBuilder()))
Graph().display()
# connections = {

#     11: {163:[[1,1]], 83:[[3,3],[6,3]] },
#     49: {87:[[1,1]]}
# }

# print(connections[11][83][0])