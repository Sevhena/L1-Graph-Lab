import heapq

class MinPQ:

    #tuple format (comparator, comparator, ..., value)

    def __init__(self, length):
        self.queue = [] 

    def push(self, weight, order, node):
        heapq.heappush(self.queue, (weight, order, node)) 

    def pop(self):
        return heapq.heappop(self.queue)

    def contains(self, node):
        for tuple in self.queue:
            if tuple[len(tuple)-1] == node:
                return True

    def replace(self, tuple):
        for i in range(self.length()):
            if self.queue[i][len(self.queue[i])-1] == tuple[len(tuple)-1]:
                self.queue.remove(self.queue[i])
                self.push(tuple)


    def length(self):
        return len(self.queue)

