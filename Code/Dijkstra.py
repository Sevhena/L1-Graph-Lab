from MetricExtractor import numNodes

from MinPQ import MinPQ


class Dijkstra:

    def __init__(self, graph, start):
        self.start = start
        num_Nodes = numNodes(graph)

        # Shortest based on line changes
        self.timeTo = [0] * (num_Nodes + 2)
        self.connectionsTo = [0] * (num_Nodes + 2)
        self.edgeTo = [0] * (num_Nodes + 2)

        self.pqueue = MinPQ(num_Nodes + 2)
        self.order_added = 0

        for i in range(len(self.timeTo)):
            self.timeTo[i] = float('inf')

        self.timeTo[start] = 0

        self.pqueue.push((0, 0, self.order_added, start))
        self.order_added += 1
        while self.pqueue.length() != 0:
            self.relax(graph, self.pqueue.pop()[3])

        # for edge in self.edgeTo:
        #     if edge != 0:
        #         print(edge.start.getId(),edge.to.getId())

    def relax(self, graph, node1):
        lastEdge = None
        for row in graph.getAdjList()[node1].values():
            for edge in row:
                node2 = edge.to.getId()

                newLine = lastEdge != None and edge.line.lineID != lastEdge.line.lineID

                # if self.connectionsTo[node2] > self.connectionsTo[node1] + newLine:
                #     self.updateEdges(node1, node2, edge, newLine)
                    
                #     self.order_added += 1
                #     lastEdge = edge

                if self.timeTo[node2] > self.timeTo[node1] + edge.time:
                    self.updateEdges(node1, node2, edge, newLine)
                    
                    self.order_added += 1
                    lastEdge = edge
                    #print(lastEdge)

    def updateEdges(self, node1, node2, edge, newLine):
        self.timeTo[node2] = self.timeTo[node1] + edge.time
        self.connectionsTo[node2] = self.connectionsTo[node1] + newLine
        self.edgeTo[node2] = edge
        #print(edge)

        # if self.pqueue.contains(node2):
        #     self.pqueue.replace((self.connectionsTo[node2], self.timeTo[node2], self.order_added, edge.to.getId()))
        # else:
        #     self.pqueue.push((self.connectionsTo[node2], self.timeTo[node2], self.order_added, edge.to.getId()))

        if self.pqueue.contains(node2):
            self.pqueue.replace((self.timeTo[node2], self.connectionsTo[node2], self.order_added, edge.to.getId()))
        else:
            self.pqueue.push((self.timeTo[node2], self.connectionsTo[node2], self.order_added, edge.to.getId()))
        

    def pathTo(self, destination):
        if not (self.timeTo[destination] < float('inf')):
            return None
        
        path = []
        edge = self.edgeTo[destination]
        while edge != 0:
            path.append(edge)
            edge = self.edgeTo[edge.start.getId()]

        path.reverse()
        
        return path
