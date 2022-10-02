import pyperf
import random
from PathFactory import PathFactory
from Code.graph import Graph
from Code.LondonGraphBuilder import LondonGraphBuilder

def main():
    random.seed(1659644754)
    startNode = random.randint(1,304)
    destinationNode = random.randint(1,304)
    algorithms = ['astar','dijkstra']
    do_bench(algorithms,startNode,destinationNode)

def do_bench(algorithms, startNode, destinationNode):
    graph = Graph(LondonGraphBuilder())
    runner = pyperf.Runner()

    for an_algorithm in algorithms:
        algo = PathFactory.build(an_algorithm,graph,startNode, destinationNode)
        runner.bench_func(an_algorithm,algo,startNode,destinationNode)

if __name__ == "__main__":
    main()