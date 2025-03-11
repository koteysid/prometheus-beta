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
    
    def dfs(node: int) -> bool:
        """
        Depth-first search to detect cycles in an undirected graph.
        
        Args:
            node (int): Starting node to begin DFS
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Initialize visited set and stack for DFS
        visited = set()
        stack = [(node, -1)]  # (current_node, parent_node)
        
        while stack:
            current, parent = stack.pop()
            
            # If node is already visited and not the parent, a cycle exists
            if current in visited:
                return True
            
            # Mark current node as visited
            visited.add(current)
            
            # Explore neighbors
            for neighbor in graph.get(current, []):
                if neighbor != parent:
                    stack.append((neighbor, current))
        
        return False
    
    # Check each node as a potential starting point
    for node in graph:
        if dfs(node):
            return True
    
    return False