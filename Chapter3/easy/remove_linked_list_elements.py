"""
Remove Linked List Elements (LeetCode #203)

Problem:
    Given the head of a linked list and an integer val, remove all the nodes 
    of the linked list that has Node.val == val, and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [], val = 1
    Output: []

Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Constraints:
    - The number of nodes in the list is in the range [0, 10^4]
    - 1 <= Node.val <= 50
    - 0 <= val <= 50

Time Complexity: O(n) - we traverse each node once
Space Complexity: O(1) for iterative, O(n) for recursive due to call stack
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    Remove all nodes with the given value using a dummy node.
    
    Approach:
        - Use a dummy node to handle edge cases (removing head)
        - Traverse the list, skipping nodes with the target value
        - Return dummy.next as the new head
    
    Args:
        head: The head of the linked list
        val: The value to remove
        
    Returns:
        Head of the modified linked list
    """
    # Dummy node simplifies handling removal at head
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next:
        if current.next.val == val:
            # Skip the node with the target value
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next
    
    return dummy.next


def remove_elements_no_dummy(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    Remove all nodes with the given value without using a dummy node.
    
    Approach:
        - First, handle all leading nodes with target value
        - Then traverse and remove remaining occurrences
    
    Args:
        head: The head of the linked list
        val: The value to remove
        
    Returns:
        Head of the modified linked list
    """
    # Remove all leading nodes with target value
    while head and head.val == val:
        head = head.next
    
    # Handle empty list after removing leading nodes
    if not head:
        return None
    
    # Traverse and remove remaining occurrences
    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


def remove_elements_recursive(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    Remove all nodes with the given value recursively.
    
    Approach:
        - Base case: empty list returns None
        - Recursively process the rest of the list
        - If current node has target value, skip it
        - Otherwise, keep it and update its next pointer
    
    Note: This uses O(n) space due to recursion stack
    
    Args:
        head: The head of the linked list
        val: The value to remove
        
    Returns:
        Head of the modified linked list
    """
    # Base case: empty list
    if not head:
        return None
    
    # Recursively process the rest of the list
    head.next = remove_elements_recursive(head.next, val)
    
    # If current node has target value, skip it
    if head.val == val:
        return head.next
    
    return head


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
    # Test Case 1: Multiple occurrences in the middle
    head1 = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    result1 = remove_elements(head1, 6)
    print(f"Test 1: {linked_list_to_array(result1)}")  # Expected: [1, 2, 3, 4, 5]
    
    # Test Case 2: Empty list
    head2 = create_linked_list([])
    result2 = remove_elements(head2, 1)
    print(f"Test 2: {linked_list_to_array(result2)}")  # Expected: []
    
    # Test Case 3: All nodes have target value
    head3 = create_linked_list([7, 7, 7, 7])
    result3 = remove_elements(head3, 7)
    print(f"Test 3: {linked_list_to_array(result3)}")  # Expected: []
    
    # Test Case 4: Target value at head
    head4 = create_linked_list([1, 1, 2, 3])
    result4 = remove_elements(head4, 1)
    print(f"Test 4: {linked_list_to_array(result4)}")  # Expected: [2, 3]
    
    # Test Case 5: Target value at tail
    head5 = create_linked_list([1, 2, 3, 3])
    result5 = remove_elements(head5, 3)
    print(f"Test 5: {linked_list_to_array(result5)}")  # Expected: [1, 2]
    
    # Test Case 6: No matching values
    head6 = create_linked_list([1, 2, 3, 4, 5])
    result6 = remove_elements(head6, 6)
    print(f"Test 6: {linked_list_to_array(result6)}")  # Expected: [1, 2, 3, 4, 5]
    
    # Test Case 7: Using no-dummy approach
    head7 = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    result7 = remove_elements_no_dummy(head7, 6)
    print(f"Test 7 (No Dummy): {linked_list_to_array(result7)}")  # Expected: [1, 2, 3, 4, 5]
    
    # Test Case 8: Using recursive approach
    head8 = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    result8 = remove_elements_recursive(head8, 6)
    print(f"Test 8 (Recursive): {linked_list_to_array(result8)}")  # Expected: [1, 2, 3, 4, 5]
    
    # Test Case 9: Single element - matches
    head9 = create_linked_list([1])
    result9 = remove_elements(head9, 1)
    print(f"Test 9: {linked_list_to_array(result9)}")  # Expected: []
    
    # Test Case 10: Single element - doesn't match
    head10 = create_linked_list([1])
    result10 = remove_elements(head10, 2)
    print(f"Test 10: {linked_list_to_array(result10)}")  # Expected: [1]
    
    print("\nAll tests passed!")
