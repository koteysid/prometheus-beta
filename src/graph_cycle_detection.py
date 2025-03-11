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
        True
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
            # Unvisited neighbor
            if neighbor not in visited:
                # Recursively explore the neighbor
                if dfs(neighbor, visited, node):
                    return True
            # Visited neighbor that is not the parent (indicates a cycle)
            elif neighbor != parent:
                return True
        
        return False
    
    # Track visited nodes
    visited = set()
    
    # Check each node as a potential starting point
    for node in graph:
        if node not in visited:
            component_visited = set()
            if dfs(node, component_visited):
                return True
            visited.update(component_visited)
    
    return False