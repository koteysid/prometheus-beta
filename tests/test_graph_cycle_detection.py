import pytest
from src.graph_cycle_detection import has_cycle_undirected

def test_graph_with_cycle():
    """Test a graph that contains a cycle."""
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    assert has_cycle_undirected(graph) == True

def test_graph_without_cycle():
    """Test a graph without a cycle."""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: []
    }
    assert has_cycle_undirected(graph) == False

def test_disconnected_graph_with_multiple_cycles():
    """Test a disconnected graph with multiple cycles."""
    graph = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2],
        4: [5],
        5: [4]
    }
    print("Debugging graph:", graph)
    print("Nodes:", list(graph.keys()))
    print("Edges:", [(node, neighbors) for node, neighbors in graph.items()])
    result = has_cycle_undirected(graph)
    print("Cycle detection result:", result)
    assert result == True

def test_disconnected_graph_without_cycle():
    """Test a disconnected graph without a cycle."""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: []
    }
    assert has_cycle_undirected(graph) == False

def test_single_node_graph():
    """Test a graph with a single node."""
    graph = {0: []}
    assert has_cycle_undirected(graph) == False

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError):
        has_cycle_undirected({})

def test_none_graph_raises_error():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError):
        has_cycle_undirected(None)

def test_complex_graph_with_multiple_components():
    """Test a more complex graph with multiple components."""
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],  # First component with cycle
        3: [4],
        4: [5],
        5: [3]      # Second component with cycle
    }
    assert has_cycle_undirected(graph) == True

def test_large_graph_no_cycle():
    """Test a larger graph without a cycle."""
    graph = {
        0: [1],
        1: [0, 2, 3],
        2: [1, 4],
        3: [1, 5],
        4: [2],
        5: [3]
    }
    assert has_cycle_undirected(graph) == False