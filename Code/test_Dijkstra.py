import pytest

from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
from Dijkstra import Dijkstra

graph = Graph(LondonGraphBuilder())

def initialize(graph, start):
    return Dijkstra(graph, start)

def test_start_is_end():
    assert initialize(graph, 5).pathTo(5) == []

def test_multi_edge_pair():
    assert len(initialize(graph, 11).pathTo(83)) == 1

# @pytest.fixture
# def random():
#     return random.randint(1,304), random.randint(1,304)

# def all_cases(start_is_end, multi_edge_pair, random):

