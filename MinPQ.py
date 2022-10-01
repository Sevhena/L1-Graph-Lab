import heapq

class MinPQ:

    def __init__(self, length):
        self.queue = [None] * length

    def push(self, weight, order, node):
        heapq.heappush(self.queue, (weight, order, node)) 

    def pop(self):
        return heapq.heappop(self.queue)

    def contains(self, node):
        for tuple in self.queue:
            if tuple[2] is node:
                return True

    def replace(self, weight, order, node):
        for i in range(self.length()):
            if self.queue[i][2] is node:
                self.queue.remove(i)
                self.queue.push(weight, order, node)


    def length(self):
        return len(self.queue)

