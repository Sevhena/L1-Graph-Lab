import pytest

from LondonGraphBuilder import LondonGraphBuilder
from graph import Graph
from UrbanPlanning import UrbanPlanning

graph = Graph(LondonGraphBuilder())

def urbanPlanning(island1, island2):
    up = UrbanPlanning(graph)
    return up.islandPath(island1,island2)

def test_urbanPlanning_Same_Island():
    assert urbanPlanning(11,11) == [11]

def urbanPlanning_Missing_Stations():
    with pytest.raises(TypeError):
        urbanPlanning()
        urbanPlanning(1)

def urbanPlanning_Missing_Stations():
    with pytest.raises(KeyError):
        urbanPlanning(0,-1)
        urbanPlanning(400,450)

def test_urbanPlanning_Different_Islands():
    assert urbanPlanning(4,200) == [4,70]