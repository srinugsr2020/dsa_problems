"""
Remove Duplicates from Sorted List (LeetCode #83)

Problem:
    Given the head of a sorted linked list, delete all duplicates such that 
    each element appears only once. Return the linked list sorted as well.

Example 1:
    Input: head = [1,1,2]
    Output: [1,2]

Example 2:
    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

Constraints:
    - The number of nodes in the list is in the range [0, 300]
    - -100 <= Node.val <= 100
    - The list is guaranteed to be sorted in ascending order

Time Complexity: O(n) - we traverse each node once
Space Complexity: O(1) - we only modify pointers in place
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicates from a sorted linked list.
    
    Approach:
        - Since the list is sorted, duplicates are adjacent
        - Compare current node with next node
        - If they're equal, skip the next node
        - If they're different, move to next node
    
    Args:
        head: The head of the sorted linked list
        
    Returns:
        Head of the list with duplicates removed
    """
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            # Skip the duplicate node by updating the pointer
            current.next = current.next.next
        else:
            # Move to the next distinct node
            current = current.next
    
    return head


def delete_duplicates_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicates from a sorted linked list recursively.
    
    Approach:
        - Base case: empty list or single node
        - Recursively process the rest of the list
        - If current value equals next value, skip current
    
    Note: This uses O(n) space due to recursion stack
    
    Args:
        head: The head of the sorted linked list
        
    Returns:
        Head of the list with duplicates removed
    """
    # Base case: empty or single node
    if not head or not head.next:
        return head
    
    # Recursively process the rest
    head.next = delete_duplicates_recursive(head.next)
    
    # If current equals next, return next (skip current duplicate)
    if head.val == head.next.val:
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
    # Test Case 1: Simple duplicates
    head1 = create_linked_list([1, 1, 2])
    result1 = delete_duplicates(head1)
    print(f"Test 1: {linked_list_to_array(result1)}")  # Expected: [1, 2]
    
    # Test Case 2: Multiple duplicates
    head2 = create_linked_list([1, 1, 2, 3, 3])
    result2 = delete_duplicates(head2)
    print(f"Test 2: {linked_list_to_array(result2)}")  # Expected: [1, 2, 3]
    
    # Test Case 3: Empty list
    head3 = create_linked_list([])
    result3 = delete_duplicates(head3)
    print(f"Test 3: {linked_list_to_array(result3)}")  # Expected: []
    
    # Test Case 4: Single element
    head4 = create_linked_list([1])
    result4 = delete_duplicates(head4)
    print(f"Test 4: {linked_list_to_array(result4)}")  # Expected: [1]
    
    # Test Case 5: All duplicates
    head5 = create_linked_list([1, 1, 1, 1, 1])
    result5 = delete_duplicates(head5)
    print(f"Test 5: {linked_list_to_array(result5)}")  # Expected: [1]
    
    # Test Case 6: No duplicates
    head6 = create_linked_list([1, 2, 3, 4, 5])
    result6 = delete_duplicates(head6)
    print(f"Test 6: {linked_list_to_array(result6)}")  # Expected: [1, 2, 3, 4, 5]
    
    # Test Case 7: Recursive approach
    head7 = create_linked_list([1, 1, 2, 2, 3, 3, 4])
    result7 = delete_duplicates_recursive(head7)
    print(f"Test 7 (Recursive): {linked_list_to_array(result7)}")  # Expected: [1, 2, 3, 4]
    
    print("\nAll tests passed!")
