form AstarAlgo import AstarAlgo
from Dijkstra import Dijkstra

class PathFactory:

    @static.method
    def build(name: str):
        selected = None
        match name:
            case 'dijkstra':
                selected = Dijkstra()
            case 'astar':
                selected = AstarAlgo()

        return selected