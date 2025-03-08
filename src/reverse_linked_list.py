class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (any): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. 
                                   Defaults to None.
    """
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.
        
        Args:
            val (any, optional): Value to be stored in the node. Defaults to 0.
            next (ListNode, optional): Reference to the next node. Defaults to None.
        """
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list in-place.
    
    This function reverses the links of a singly linked list, effectively 
    reversing the order of the nodes. It handles the following cases:
    - Empty list (None)
    - List with a single node
    - List with multiple nodes
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as reversal is done in-place
    
    Args:
        head (ListNode): The head of the linked list to be reversed.
    
    Returns:
        ListNode: The new head of the reversed list.
    
    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> reversed_head = reverse_linked_list(head)
        >>> # List is now 3 -> 2 -> 1
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None
    current = head
    
    # Iterate through the list and reverse links
    while current:
        # Store the next node before changing links
        next_node = current.next
        
        # Reverse the current node's pointer
        current.next = prev
        
        # Move pointers one step forward
        prev = current
        current = next_node
    
    # prev is now the new head of the reversed list
    return prev