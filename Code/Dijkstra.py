from graph import Graph

from MinPQ import MinPQ


class Dijkstra:

    def __init__(self, graph, start):
        self.edge = {} 
        self.time = {} 
        self.pqueue = MinPQ(303) #MUST CHANGE!!!!
        self.order_added = 0

        for i in range(len(self.time)):
            self.time[i] = float('inf')

        self.time[start.getId()] = 0

        self.pqueue.push(0, self.order_added, start)
        self.order_added += 1
        while self.pqueue.length() != 0:
            self.relax(graph, self.pqueue.pop()[2])

    def relax(self, graph, node1):
        for edge in graph.getAdjList().values():
            node2 = edge.to.getId()

            if self.time[node2] > self.time[node1] + edge.time:
                self.time[node2] = self.time[node1] + edge.time
                self.edge[node2] = edge

                if self.pqueue.contains(node2):
                    self.pqueue.replace(self.time[node2], self.order_added, edge.to)
                else:
                    self.pqueue.push(self.time[node2], self.order_added, edge.to)
                
                self.order_added += 1
