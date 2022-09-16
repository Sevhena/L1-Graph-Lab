class LondonGraphBuilder:

    def __init__(self):
        # self.num_of_vertices = 0
        # self.num_of_edges = 0
        self.adj_list = {}

    # def csvStations(self):
    #     colNames, rows = self.importCSV(self.stations_file)

    #     rowCounter = 0
    #     for row in rows:
    #         colCounter = 0
    #         for value in row:
    #             self.stationsList[rowCounter+1] = {colNames[colCounter]:row}
    #             colCounter += 1
    #         rowCounter += 1

    def adjList(self, station_file):
        for row in station_file:
            if self.adj_list.get(row[0]) == None:
                self.adj_list[row[0]] = {row[1]:[row[2],row[3]]} 
            else:
                self.adj_list[row[0]][row[1]] = [row[2],row[3]]
        return self.adj_list



