from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
# from GraphBuilders.Line import Line
# from GraphBuilders.Station import Station
# from GraphBuilders.Edge import Edge

def numNodes(graph):
    return len(graph.getAdjList())

def numEdges(graph):
    numEdges = 0
    for dict in graph.getAdjList().values():
        for row in dict.values(): 
            for edge in row:
                if edge.reverse == False:
                    numEdges += 1

    return numEdges

def avgDegree(graph):
    return numEdges(graph) / numNodes(graph)



def main():
    graph = Graph(LondonGraphBuilder())

    print(numEdges(graph))
    #print(graph.adjList(read_London_Connections()))

if __name__ == "__main__":
    main()