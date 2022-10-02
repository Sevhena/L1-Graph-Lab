class Edge:

    def __init__(self, start, to, line, time, reverse):
        self.start = start #Station object  
        self.to = to #Station object
        self.time = time
        self.line = line #Line object
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