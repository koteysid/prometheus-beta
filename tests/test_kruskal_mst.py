import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_basic():
    """Test basic DisjointSet operations."""
    ds = DisjointSet(5)
    
    # Initial state: each vertex in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union vertices
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Verify union prevents duplicate edges
    assert not ds.union(0, 1)

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph."""
    # Graph edges: (weight, u, v)
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 0, 2)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected result: minimum spanning tree with minimum total weight
    assert len(mst) == 2
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 3

def test_kruskal_mst_complex_graph():
    """Test Kruskal's algorithm on a more complex graph."""
    graph = [
        (4, 0, 1),
        (8, 0, 7),
        (11, 1, 7),
        (8, 1, 2),
        (7, 7, 8),
        (2, 7, 6),
        (6, 8, 6),
        (2, 2, 8),
        (4, 2, 3),
        (7, 2, 5),
        (9, 3, 5),
        (10, 3, 4),
        (14, 5, 4),
        (10, 6, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected total weight 
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 37
    assert len(mst) == 7  # Number of edges in MST should be vertices-1

def test_kruskal_mst_single_edge():
    """Test Kruskal's algorithm with a single edge."""
    graph = [(5, 0, 1)]
    
    mst = kruskal_mst(graph)
    assert mst == [(5, 0, 1)]

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with an empty graph."""
    graph = []
    
    mst = kruskal_mst(graph)
    assert mst == []

def test_kruskal_mst_error_handling():
    """Test error handling for invalid inputs."""
    # Test None input
    with pytest.raises(ValueError, match="Graph cannot be None"):
        kruskal_mst(None)
    
    # Test invalid graph format
    with pytest.raises(TypeError):
        kruskal_mst([(1, 2), (3, 4)])  # Incorrect tuple format
    
    with pytest.raises(TypeError):
        kruskal_mst("not a list")  # Wrong input type

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph."""
    graph = [
        (1, 0, 1),
        (2, 2, 3),
        (3, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Should include edges that do not connect
    assert len(mst) == 3