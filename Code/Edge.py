class Edge:

    def __init__(self, start, to, line, time, reverse):
        self.start = start
        self.to = to
        self.time = time
        self.line = line
        self.reverse = reverse

    def getStart(self):
        return self.start

    def getTo(self):
        return self.to
    
    def getTime(self):
        return self.time

    def getLine(self):
        return self.line

    def __lt__(self, other):
        return self.time < other.time