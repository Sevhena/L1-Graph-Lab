class Station:

    def __init__(self, id, latitude, longitude, name, display_name, zone, total_lines, rail):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.display_name = display_name
        self.zone = zone
        self.total_lines = total_lines
        self.rail = rail

    def getId(self):
        return self.id

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def getName(self):
        return self.name

    def getDisplayName(self):
        return self.display_name

    def getZone(self):
        return self.zone

    def getTotalLines(self):
        return self.total_lines

    def getRail(self):
        return self.rail    