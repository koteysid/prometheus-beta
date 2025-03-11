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
    
    def dfs(node: int, visited: Set[int], parent: int) -> bool:
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
        
        # Check all adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor hasn't been visited, recursively check its connections
            if neighbor not in visited:
                if dfs(neighbor, visited, node):
                    return True
            # If neighbor has been visited and is not the parent, a cycle exists
            elif neighbor != parent:
                return True
        
        return False
    
    # Track visited nodes across the entire graph
    visited_nodes = set()
    
    # Check for cycles starting from each unvisited node
    for node in graph:
        if node not in visited_nodes:
            if dfs(node, visited_nodes, -1):
                return True
    
    return False