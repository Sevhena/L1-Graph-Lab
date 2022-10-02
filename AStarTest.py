import pytest
from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
from AstarAlgo import AstarAlgo

graph = Graph(LondonGraphBuilder())
astar = AstarAlgo(graph)

def AStarAlgo(start, end):
    return astar.aStarAlgo(start,end)

def testAStarAlgo_Same_Station():
    assert AStarAlgo(11,11) == [11]

def testAStarAlgo_Missing_Stations():
    with pytest.raises(TypeError):
        AStarAlgo()
        AStarAlgo(1)

def testAStarAlgo_Missing_Stations():
    with pytest.raises(KeyError):
        AStarAlgo(0,-1)
        AStarAlgo(400,450)

def testAStarAlgo_Adjacent_Stations():
    assert AStarAlgo(4,70) == [4,70]
