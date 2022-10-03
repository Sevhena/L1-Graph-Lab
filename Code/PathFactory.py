from AstarAlgo import AstarAlgo
from Dijkstra import Dijkstra

class PathFactory:

    def build(name: str, graph,startNode, destinationNode):
        selected = None
        match name:
            case 'dijkstra':
                d = Dijkstra(graph,startNode)
                selected = d.pathTo(destinationNode)
            case 'astar':
                a = AstarAlgo(graph,startNode)
                selected = a.pathTo(destinationNode)
        return selected