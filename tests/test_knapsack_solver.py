import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a simple knapsack scenario"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_full_capacity_knapsack():
    """Test when items exactly fill the knapsack"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_cannot_fill_knapsack():
    """Test when no items can be included"""
    weights = [30, 40, 50]
    values = [60, 100, 120]
    capacity = 20
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 0
    assert selected_items == []

def test_single_item_fits():
    """Test when only a single item fits"""
    weights = [10, 30, 50]
    values = [60, 100, 120]
    capacity = 20
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 60
    assert selected_items == [0]

def test_zero_capacity():
    """Test knapsack with zero capacity"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 0
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 0
    assert selected_items == []

def test_invalid_input_different_lengths():
    """Test error handling for lists of different lengths"""
    weights = [10, 20]
    values = [60, 100, 120]
    capacity = 50
    
    with pytest.raises(ValueError, match="Weights and values lists must be non-empty and of equal length"):
        solve_knapsack(weights, values, capacity)

def test_invalid_input_empty_lists():
    """Test error handling for empty lists"""
    weights = []
    values = []
    capacity = 50
    
    with pytest.raises(ValueError, match="Weights and values lists must be non-empty and of equal length"):
        solve_knapsack(weights, values, capacity)

def test_negative_capacity():
    """Test error handling for negative capacity"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = -10
    
    with pytest.raises(ValueError, match="Knapsack capacity must be non-negative"):
        solve_knapsack(weights, values, capacity)