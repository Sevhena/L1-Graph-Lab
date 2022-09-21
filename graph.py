from GraphBuilder import*
from Extractor import*

connections = MetricExtractor().read_London_Connections('_dataset\london.connections.csv')
locations = MetricExtractor().read_London_Station('_dataset\london.stations.csv')

graph = Graph(connections,locations)


ShortestPath = graph.aStarAlgo(11,13)
print(ShortestPath)
