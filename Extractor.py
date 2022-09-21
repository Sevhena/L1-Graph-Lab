import csv
class MetricExtractor:

    stations = []
    L_Lines = []
    connections = []
    
    def read_London_Station(self, input):
        with open(input)as file:
            csvFile = csv.reader(file)

            for lines in csvFile:
                self.stations.append(lines)
        self.stations.pop(0)
        return self.toFloat(self.stations)

    def read_London_Lines(self,input):
        with open(input)as file:
            csvFile = csv.reader(file)

            for lines in csvFile:
                self.L_Lines.append(lines)

        self.L_Lines.pop(0)
        return self.toInteger(self.L_Lines)

    def read_London_Connections(self,input):
        with open(input)as file:
            csvFile = csv.reader(file)

            for lines in csvFile:
                self.connections.append(lines)

        self.connections.pop(0)
        return self.toInteger(self.connections)

    def toInteger(self, list):
        for i in list:
            for j in range(0,len(i)):
                try:
                    i[j] = int(i[j])
                except ValueError:
                    continue
        return list

    def toFloat(self, list):
        for i in list:
            for j in range(0,len(i)):
                try:
                    i[j] = float(i[j])
                except ValueError:
                    continue
        return list