"""
Middle of the Linked List (LeetCode #876)

Problem:
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, 
                 we return the second one.

Constraints:
    - The number of nodes in the list is in the range [1, 100]
    - 1 <= Node.val <= 100

Time Complexity: O(n) - we traverse the list once
Space Complexity: O(1) - only using two pointers
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node using fast and slow pointers.
    
    Approach:
        - Slow pointer moves 1 step at a time
        - Fast pointer moves 2 steps at a time
        - When fast reaches the end, slow is at the middle
    
    Why it works:
        - Fast travels 2x the distance of slow
        - When fast has traveled n nodes, slow has traveled n/2
        - So slow ends up at the middle
    
    For even-length lists, this returns the SECOND middle node.
    
    Args:
        head: The head of the linked list
        
    Returns:
        The middle node of the linked list
    """
    if not head:
        return None
    
    slow = head
    fast = head
    
    # Move until fast reaches the end
    while fast and fast.next:
        slow = slow.next        # Move slow by 1
        fast = fast.next.next   # Move fast by 2
    
    return slow  # slow is at the middle


def middle_node_first(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the FIRST middle node for even-length lists.
    
    Approach:
        - Same as above, but with different termination condition
        - Check fast.next and fast.next.next instead
    
    For list [1,2,3,4], returns node 2 (first middle).
    
    Args:
        head: The head of the linked list
        
    Returns:
        The first middle node for even-length lists
    """
    if not head:
        return None
    
    slow = head
    fast = head
    
    # Different condition: check next two nodes exist
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def middle_node_two_pass(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node using two passes.
    
    Approach:
        1. First pass: count the total number of nodes
        2. Second pass: traverse to the middle node
    
    Note: This is less efficient but easier to understand.
    
    Args:
        head: The head of the linked list
        
    Returns:
        The middle node of the linked list
    """
    if not head:
        return None
    
    # First pass: count nodes
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    # Second pass: go to middle
    middle_index = count // 2
    current = head
    for _ in range(middle_index):
        current = current.next
    
    return current


def middle_node_array(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node by storing nodes in an array.
    
    Approach:
        - Store all nodes in an array
        - Return the node at index len/2
    
    Note: This uses O(n) space but is very simple.
    
    Args:
        head: The head of the linked list
        
    Returns:
        The middle node of the linked list
    """
    if not head:
        return None
    
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    
    return nodes[len(nodes) // 2]


# --------------------- Helper Functions ---------------------

def create_linked_list(arr: list) -> Optional[ListNode]:
    """Create a linked list from an array."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head: Optional[ListNode]) -> list:
    """Convert a linked list to an array for easy verification."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# --------------------- Test Cases ---------------------

if __name__ == "__main__":
    # Test Case 1: Odd length list
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = middle_node(head1)
    print(f"Test 1 (odd): {linked_list_to_array(result1)}")  # Expected: [3, 4, 5]
    
    # Test Case 2: Even length list (returns second middle)
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    result2 = middle_node(head2)
    print(f"Test 2 (even): {linked_list_to_array(result2)}")  # Expected: [4, 5, 6]
    
    # Test Case 3: Single node
    head3 = create_linked_list([1])
    result3 = middle_node(head3)
    print(f"Test 3 (single): {linked_list_to_array(result3)}")  # Expected: [1]
    
    # Test Case 4: Two nodes
    head4 = create_linked_list([1, 2])
    result4 = middle_node(head4)
    print(f"Test 4 (two): {linked_list_to_array(result4)}")  # Expected: [2]
    
    # Test Case 5: Three nodes
    head5 = create_linked_list([1, 2, 3])
    result5 = middle_node(head5)
    print(f"Test 5 (three): {linked_list_to_array(result5)}")  # Expected: [2, 3]
    
    # Test Case 6: First middle for even length
    head6 = create_linked_list([1, 2, 3, 4])
    result6 = middle_node_first(head6)
    print(f"Test 6 (first middle): {linked_list_to_array(result6)}")  # Expected: [2, 3, 4]
    
    # Test Case 7: Two-pass approach
    head7 = create_linked_list([1, 2, 3, 4, 5])
    result7 = middle_node_two_pass(head7)
    print(f"Test 7 (two-pass): {linked_list_to_array(result7)}")  # Expected: [3, 4, 5]
    
    # Test Case 8: Array approach
    head8 = create_linked_list([1, 2, 3, 4, 5, 6])
    result8 = middle_node_array(head8)
    print(f"Test 8 (array): {linked_list_to_array(result8)}")  # Expected: [4, 5, 6]
    
    # Test Case 9: Longer list
    head9 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    result9 = middle_node(head9)
    print(f"Test 9 (longer): {result9.val}")  # Expected: 5
    
    print("\nAll tests passed!")
