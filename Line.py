class Line:

    def __init__(self, lineID, name, colour, stripe):
        self.lineID = lineID
        self.name = name
        self.colour = colour
        self.stripe = stripe
    
    def getLineID(self):
        return self.lineID

    def getName(self):
        return self.name

    def getColour(self):
        return self.colour

    def getStripe(self):
        return self.stripe
        