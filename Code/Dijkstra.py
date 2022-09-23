from graph import Graph

from MinPQ import MinPQ


class Dijkstra:

    def __init__(self, graph, start, numNodes):
        self.start = start

        #Shortest based of time taken
        self.edge = [0] * (numNodes + 2)
        self.timeTo = [0] * (numNodes + 2)

        #Shortest based on line changes
        self.timeToC = [0] * (numNodes + 2)
        self.connectionsTo = [0] * (numNodes + 2) 
        self.edgeC = [0] * (numNodes + 2)

        self.pqueue = MinPQ(numNodes + 2)
        self.order_added = 0

        for i in range(len(self.timeTo)):
            self.timeTo[i] = float('inf')

        #print(len(self.time))
        self.timeTo[start] = 0

        self.pqueue.push((0, self.order_added, start))
        self.order_added += 1
        while self.pqueue.length() != 0:
            self.relaxT(graph, self.pqueue.pop()[2])

        for i in range(len(self.timeToC)):
            self.timeToC[i] = float('inf')

        self.order_added = 0
        self.timeToC[start] = 0

        self.pqueue.push((0, 0, self.order_added, start))
        self.order_added += 1
        while self.pqueue.length() != 0:
            self.relaxC(graph, self.pqueue.pop()[3])

        # for edge in self.edgeC:
        #     if edge != 0:
        #         print(edge.start.getId(),edge.to.getId())



    def relaxT(self, graph, node1):
        for row in graph.getAdjList()[node1].values():
            for edge in row:
                node2 = edge.to.getId()
                #print(node2,node1)

                if self.timeTo[node2] > self.timeTo[node1] + edge.time:
                    self.timeTo[node2] = self.timeTo[node1] + edge.time
                    self.edge[node2] = edge

                    if self.pqueue.contains(node2):
                        self.pqueue.replace((self.timeTo[node2], self.order_added, edge.to.getId()))
                    else:
                        self.pqueue.push((self.timeTo[node2], self.order_added, edge.to.getId()))
                    
                    self.order_added += 1

    def relaxC(self, graph, node1):
        lastEdge = None
        #print(graph.getAdjList().keys())
        for row in graph.getAdjList()[node1].values():
            for edge in row:
                node2 = edge.to.getId()
                #print(node2,node1)

                newLine = lastEdge != None and edge.line.lineID != lastEdge.line.lineID
                #print(int(newLine))
                if self.timeToC[node2] > self.timeToC[node1] + edge.time:
                    self.timeToC[node2] = self.timeToC[node1] + edge.time
                    self.connectionsTo[node2] = self.connectionsTo[node1] + newLine
                    self.edgeC[node2] = edge
                    #print(edge)

                    if self.pqueue.contains(node2):
                        self.pqueue.replace((self.connectionsTo[node2], self.timeToC[node2], self.order_added, edge.to.getId()))
                    else:
                        self.pqueue.push((self.connectionsTo[node2], self.timeToC[node2], self.order_added, edge.to.getId()))
                    
                    self.order_added += 1
                    lastEdge = edge
                    #print(lastEdge)
        

    def pathTo(self, destination):
        if not (self.timeTo[destination] < float('inf')):
            return None
        
        if not (self.connectionsTo[destination] < float('inf')):
            return None

        pathT = []
        edge = self.edge[destination]
        while edge != 0:
            pathT.append(edge)
            edge = self.edge[edge.start.getId()]

        pathC = []
        edge = self.edgeC[destination]
        while edge != 0:
            pathC.append(edge)
            edge = self.edgeC[edge.start.getId()]
        
        return pathT, pathC


