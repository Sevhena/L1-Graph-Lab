import ThingsToTest as algo

class BenchFactory:

    def build(name: str):
        selected = None
        match name:
            case 'Astar':
                selected = algo.Astar
            case 'Dijkstra':
                selected = algo.Djikstra
            case _:
                raise ValueError(name)
        return selected

