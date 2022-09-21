import csv

from Line import Line
from Station import Station
from Edge import Edge

class LondonGraphBuilder:

    def __init__(self):
        self.stationsList = self.read_London_Station()
        self.lines_list = self.read_London_Lines()
        self.connectionsList = self.read_London_Connections()
        self.adj_list = {}

    def read_London_Station(self):
        stations_list = {}
        with open('_dataset\london.stations.csv')as file:
            csvFile = csv.reader(file)

            next(csvFile)
            
            for lines in csvFile:
                station = Station(int(lines[0]),float(lines[1]),float(lines[2]),lines[3],lines[4],float(lines[5]),int(lines[6]),int(lines[7]))
                stations_list[station.getId()] = station

        return stations_list


    def read_London_Lines(self):
        L_Lines = {}
        with open('_dataset\london.lines.csv')as file:
            csvFile = csv.reader(file)

            next(csvFile)
            
            for lines in csvFile:
                listA, listB = list(map(int,lines[:1])), lines[1:]
                line_list = listA + listB
                line = Line(line_list[0], line_list[1], line_list[2], line_list[3])
                L_Lines[line.getLineID()] = line

        return L_Lines

    def read_London_Connections(self):
        connections = [] #
        with open('_dataset/london.connections.csv')as file:
            csvFile = csv.reader(file)

            next(csvFile)
            for lines in csvFile:
                connections.append(list(map(int,lines)))

        return connections

    def getAdjacenyList(self):
        for row in self.connectionsList:
            if self.adj_list.get(row[0]) == None:
                self.adj_list[row[0]] = [Edge(self.stationsList[row[0]], self.stationsList[row[1]], self.lines_list[row[2]], row[3], False)]
            elif self.adj_list.get(row[0]) != None:
                self.adj_list[row[0]] += [Edge(self.stationsList[row[0]], self.stationsList[row[1]], self.lines_list[row[2]], row[3], False)]
            if self.adj_list.get(row[1]) == None:
                self.adj_list[row[1]] = [Edge(self.stationsList[row[1]], self.stationsList[row[0]], self.lines_list[row[2]], row[3], True)]
            elif self.adj_list.get(row[1]) != None:
                self.adj_list[row[1]] += [Edge(self.stationsList[row[1]], self.stationsList[row[0]], self.lines_list[row[2]], row[3], True)]

                

        return self.adj_list

def main():
    graph = LondonGraphBuilder()
    print(graph.getAdjacenyList()[11][0].getTo().getId())
    #print(graph.lines_list[6].getLineID())
    #print(len(graph.stationsList))
    #read_London_Station()

if __name__ == "__main__":
    main()



