import random
import time
import tracemalloc
from PathFactory import PathFactory
from graph import Graph
from LondonGraphBuilder import LondonGraphBuilder

graph = Graph(LondonGraphBuilder())


def main():
    startNode = random.randint(1,304)
    destinationNode = random.randint(1,304)
    algorithms = ['astar','dijkstra']
    do_bench(algorithms,startNode,destinationNode)

def do_bench(algorithms, startNode, destinationNode):
    print(startNode)
    print(destinationNode)

    for an_algorithm in algorithms:
        start_time = time.time()
        algo = PathFactory.build(an_algorithm,graph, startNode, destinationNode)
        end_time = time.time()
        print(an_algorithm,(end_time-start_time)*1000)
        
        # Tracing the memory used to run the algorithms
        # # this gets the current size and peak size of memory blocks traced in bytes
        # # current being how much memory th code is currently using
        # # peak being the maximum space the program used while executing
        tracemalloc.start()
        algo = PathFactory.build(an_algorithm,graph, startNode, destinationNode)
        print(tracemalloc.get_traced_memory())
        tracemalloc.stop()


if __name__ == "__main__":
    main()