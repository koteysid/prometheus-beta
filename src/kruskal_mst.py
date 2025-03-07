class DisjointSet:
    """
    A data structure to perform union-find operations for Kruskal's algorithm.
    
    This class implements the disjoint-set data structure with path compression 
    and union by rank for efficient minimum spanning tree computation.
    """
    
    def __init__(self, vertices):
        """
        Initialize the disjoint set for a given number of vertices.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item):
        """
        Find the root of a vertex with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Union of two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(graph):
    """
    Implement Kruskal's algorithm to find the minimum spanning tree.
    
    :param graph: A list of edges, where each edge is (weight, u, v)
    :return: A list of edges in the minimum spanning tree
    
    Raises:
    - ValueError: If the graph is empty or None
    - TypeError: If the graph is not in the correct format
    """
    # Input validation
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    if not graph:
        return []
    
    # Validate graph edge format and ensure correct tuple structure
    try:
        # Sort edges by weight in ascending order
        sorted_edges = sorted([(edge[0], edge[1], edge[2]) for edge in graph], key=lambda x: x[0])
    except (TypeError, IndexError):
        raise TypeError("Graph must be a list of (weight, u, v) tuples")
    
    # Get number of vertices 
    max_vertex = max(max(edge[1], edge[2]) for edge in sorted_edges)
    vertices = max_vertex + 1
    
    # Initialize disjoint set
    disjoint_set = DisjointSet(vertices)
    
    # Store minimum spanning tree edges
    mst = []
    
    # Add edges to MST if they don't create a cycle
    for weight, u, v in sorted_edges:
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))
            
            # Stop when we have V-1 edges (a complete spanning tree)
            if len(mst) == vertices - 1:
                break
    
    return mst