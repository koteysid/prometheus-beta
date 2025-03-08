import pytest
from src.reverse_linked_list import ListNode, reverse_linked_list

def list_to_array(head):
    """
    Convert a linked list to an array for easy comparison.
    
    Args:
        head (ListNode): Head of the linked list.
    
    Returns:
        list: Array representation of the linked list values.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    """
    Convert an array to a linked list.
    
    Args:
        arr (list): Array of values.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def test_reverse_empty_list():
    """
    Test reversing an empty list.
    """
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """
    Test reversing a list with a single node.
    """
    head = ListNode(42)
    reversed_head = reverse_linked_list(head)
    assert reversed_head.val == 42
    assert reversed_head.next is None

def test_reverse_two_node_list():
    """
    Test reversing a list with two nodes.
    """
    head = ListNode(1, ListNode(2))
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [2, 1]

def test_reverse_multiple_node_list():
    """
    Test reversing a list with multiple nodes.
    """
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = array_to_list([1, 2, 3, 4, 5])
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Check if list is now 5 -> 4 -> 3 -> 2 -> 1
    assert list_to_array(reversed_head) == [5, 4, 3, 2, 1]

def test_list_integrity_after_reversal():
    """
    Ensure the list maintains integrity after multiple reversals.
    """
    # Create original list
    original = array_to_list([1, 2, 3, 4, 5])
    
    # Reverse once
    first_reversal = reverse_linked_list(original)
    assert list_to_array(first_reversal) == [5, 4, 3, 2, 1]
    
    # Reverse again (should return to original order)
    second_reversal = reverse_linked_list(first_reversal)
    assert list_to_array(second_reversal) == [1, 2, 3, 4, 5]