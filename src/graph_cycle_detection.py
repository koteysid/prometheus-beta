from typing import Dict, List, Set

def has_cycle_undirected(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if an undirected graph contains a cycle.
    
    Args:
        graph (Dict[int, List[int]]): An undirected graph represented as an adjacency list.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        bool: True if the graph contains a cycle, False otherwise.
    
    Raises:
        ValueError: If the input graph is empty or None.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    Space Complexity: O(V) for the recursion stack and visited set
    
    Examples:
        >>> has_cycle_undirected({0: [1, 2], 1: [0, 2], 2: [0, 1]})
        True
        >>> has_cycle_undirected({0: [1], 1: [0], 2: [3], 3: [2]})
        False
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs(node: int, visited: Set[int], parent: int = -1) -> bool:
        """
        Depth-first search to detect cycles in an undirected graph.
        
        Args:
            node (int): Current node being visited
            visited (Set[int]): Set of nodes already visited
            parent (int): Parent node of the current node
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Mark the current node as visited
        visited.add(node)
        
        # Explore neighbors
        for neighbor in graph.get(node, []):
            # Skip the parent node
            if neighbor == parent:
                continue
            
            # If neighbor is visited, a cycle exists
            if neighbor in visited:
                return True
            
            # Recursively explore neighbor 
            if dfs(neighbor, visited, node):
                return True
        
        return False
    
    # Track visited nodes
    visited = set()
    
    # Track nodes with cycles
    cycle_nodes = set()
    
    # Check each node as a potential starting point
    for node in graph:
        # Only process unvisited nodes
        if node not in visited:
            component_visited = set()
            
            # If a cycle is found in this component
            if dfs(node, component_visited):
                # Add all nodes in this component to cycle_nodes
                cycle_nodes.update(component_visited)
            
            # Update overall visited nodes
            visited.update(component_visited)
    
    # If there are any nodes in cycle_nodes, the graph has a cycle
    return len(cycle_nodes) > 0