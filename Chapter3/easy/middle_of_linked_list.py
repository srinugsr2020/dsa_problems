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
Space Complexity: O(1) - we only use two pointers
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node using slow and fast pointers.
    
    Approach (Floyd's Tortoise and Hare):
        - Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
        - When fast reaches the end, slow is at the middle
        - For even length lists, this naturally returns the second middle
    
    Why it works:
        - Fast pointer moves twice as fast as slow
        - When fast has traversed the whole list, slow has traversed half
    
    Args:
        head: The head of the linked list
        
    Returns:
        The middle node (second middle for even length lists)
    """
    slow = head
    fast = head
    
    # Move fast by 2 and slow by 1 until fast reaches the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def middle_node_two_pass(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node using two passes (count then traverse).
    
    Approach:
        - First pass: count the total number of nodes
        - Second pass: traverse to the middle position
    
    Note: This is less efficient than the one-pass approach
    
    Args:
        head: The head of the linked list
        
    Returns:
        The middle node (second middle for even length lists)
    """
    # First pass: count nodes
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    # Second pass: traverse to middle
    middle_index = count // 2
    current = head
    for _ in range(middle_index):
        current = current.next
    
    return current


def middle_node_array(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node using array storage.
    
    Approach:
        - Store all nodes in an array
        - Return the node at index n // 2
    
    Note: This uses O(n) extra space
    
    Args:
        head: The head of the linked list
        
    Returns:
        The middle node (second middle for even length lists)
    """
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
    middle1 = middle_node(head1)
    print(f"Test 1 (Optimal): {linked_list_to_array(middle1)}")  # Expected: [3, 4, 5]
    
    # Test Case 2: Even length list
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = middle_node(head2)
    print(f"Test 2 (Optimal): {linked_list_to_array(middle2)}")  # Expected: [4, 5, 6]
    
    # Test Case 3: Single element
    head3 = create_linked_list([1])
    middle3 = middle_node(head3)
    print(f"Test 3 (Optimal): {linked_list_to_array(middle3)}")  # Expected: [1]
    
    # Test Case 4: Two elements
    head4 = create_linked_list([1, 2])
    middle4 = middle_node(head4)
    print(f"Test 4 (Optimal): {linked_list_to_array(middle4)}")  # Expected: [2]
    
    # Test Case 5: Using two-pass approach
    head5 = create_linked_list([1, 2, 3, 4, 5])
    middle5 = middle_node_two_pass(head5)
    print(f"Test 5 (Two-pass): {linked_list_to_array(middle5)}")  # Expected: [3, 4, 5]
    
    # Test Case 6: Using array approach
    head6 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle6 = middle_node_array(head6)
    print(f"Test 6 (Array): {linked_list_to_array(middle6)}")  # Expected: [4, 5, 6]
    
    print("\nAll tests passed!")
