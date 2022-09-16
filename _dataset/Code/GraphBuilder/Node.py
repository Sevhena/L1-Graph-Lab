class StationNode:

    def __init__(self, id, latitude, longitude, name, zone):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.zone = zone

    def getId(self):
        return self.id

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def getName(self):
        return self.name

    def getZone(self):
        return self.zone    