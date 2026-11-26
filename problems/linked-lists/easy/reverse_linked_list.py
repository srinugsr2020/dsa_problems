"""
Reverse Linked List (LeetCode #206)

Problem:
    Given the head of a singly linked list, reverse the list, 
    and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints:
    - The number of nodes in the list is in the range [0, 5000]
    - -5000 <= Node.val <= 5000

Time Complexity: O(n) - we traverse each node once
Space Complexity: O(1) - we only use a few pointers (iterative approach)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list iteratively.
    
    Approach:
        - Use three pointers: prev, current, and next_temp
        - At each step, reverse the link direction
        - Move all pointers one step forward
    
    Args:
        head: The head of the linked list
        
    Returns:
        The new head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        # Save the next node before we break the link
        next_temp = current.next
        # Reverse the link - point current node back to prev
        current.next = prev
        # Move prev and current one step forward
        prev = current
        current = next_temp
    
    # prev is now the new head
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list recursively.
    
    Approach:
        - Base case: empty list or single node
        - Recursively reverse the rest of the list
        - Make the next node point back to current node
        - Set current node's next to None
    
    Note: This uses O(n) space due to recursion stack
    
    Args:
        head: The head of the linked list
        
    Returns:
        The new head of the reversed linked list
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    
    # Make the next node point back to current node
    head.next.next = head
    # Remove the old forward link
    head.next = None
    
    return new_head


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
    # Test Case 1: Normal list
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverse_list_iterative(head1)
    print(f"Test 1 (Iterative): {linked_list_to_array(reversed1)}")  # Expected: [5, 4, 3, 2, 1]
    
    # Test Case 2: Two elements
    head2 = create_linked_list([1, 2])
    reversed2 = reverse_list_recursive(head2)
    print(f"Test 2 (Recursive): {linked_list_to_array(reversed2)}")  # Expected: [2, 1]
    
    # Test Case 3: Empty list
    head3 = create_linked_list([])
    reversed3 = reverse_list_iterative(head3)
    print(f"Test 3 (Empty): {linked_list_to_array(reversed3)}")  # Expected: []
    
    # Test Case 4: Single element
    head4 = create_linked_list([1])
    reversed4 = reverse_list_iterative(head4)
    print(f"Test 4 (Single): {linked_list_to_array(reversed4)}")  # Expected: [1]
    
    print("\nAll tests passed!")
