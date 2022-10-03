import pytest

from ..MainModules.LondonGraphBuilder import LondonGraphBuilder
from ..MainModules.graph import Graph
from ..PathFinders.AstarAlgo import AstarAlgo

graph = Graph(LondonGraphBuilder())
astar = AstarAlgo(graph)

def AStarAlgo(start, end):
    return astar.aStarAlgo(start,end)

def test_AStarAlgo_Same_Station():
    assert AStarAlgo(11,11) == [11]

def AStarAlgo_Missing_Stations():
    with pytest.raises(TypeError):
        AStarAlgo()
        AStarAlgo(1)

def AStarAlgo_Missing_Stations():
    with pytest.raises(KeyError):
        AStarAlgo(0,-1)
        AStarAlgo(400,450)

def test_AStarAlgo_Adjacent_Stations():
    assert AStarAlgo(4,70) == [4,70]
