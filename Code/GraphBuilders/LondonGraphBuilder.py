import csv

from Line import Line

class LondonGraphBuilder:

    def __init__(self):
        self.stationsList = self.read_London_Station()
        self.lines_list = self.read_London_Lines()
        self.connectionsList = self.read_London_Connections()
        self.adj_list = {}

    def read_London_Station(self):
        stations_list = []
        with open('_dataset\london.stations.csv')as file:
            csvFile = csv.reader(file)

            next(csvFile)
            for lines in csvFile:
                listA = list(map(int, lines[:1]))
                listB = list(map(float, lines[1:3]))
                listC = list(map(float,lines[5:6]))
                listD = list(map(int, lines[6:]))
                stations_list.append(listA + listB + lines[3:5] + listC + listD)

        return stations_list


    def read_London_Lines(self):
        L_Lines = [] #
        with open('_dataset\london.lines.csv')as file:
            csvFile = csv.reader(file)

            next(csvFile)
            
            for lines in csvFile:
                listA, listB = list(map(int,lines[:1])), lines[1:]
                line_list = listA + listB
                line = Line(line_list[0], line_list[1], line_list[2], line_list[3])
                L_Lines.append(line)

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
                self.adj_list[row[0]] = {row[1]:[[self.lines_list[row[2]-1],row[3]]]} 
            else:
                if self.adj_list[row[0]].get(row[1]) == None:
                    self.adj_list[row[0]][row[1]] = [[self.lines_list[row[2]-1],row[3]]]
                else:
                    self.adj_list[row[0]][row[1]] += [[self.lines_list[row[2]-1],row[3]]]

        return self.adj_list

def main():
    graph = LondonGraphBuilder()
    print(graph.getAdjacenyList()[11][163][0][0].getLineID())
    #read_London_Station()

if __name__ == "__main__":
    main()



