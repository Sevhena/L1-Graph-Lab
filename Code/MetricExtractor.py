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
    degreeDist = degreeDistribution(graph)
    sum_of_degrees = 0

    for degree in degreeDist.keys():
        sum_of_degrees += degree * degreeDist[degree]
        
    return sum_of_degrees/ numNodes(graph)

def degreeDistribution(graph):
    degreeDist = {}
    
    for dict in graph.getAdjList().values():
        degree = 0
        for row in dict.values(): 
            degree += len(row)

        if degreeDist.get(degree) == None:
            degreeDist[degree] = 1
        else:
            degreeDist[degree] += 1

    return degreeDist