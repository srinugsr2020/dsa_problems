"""
Merge Two Sorted Lists (LeetCode #21)

Problem:
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by 
    splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    - The number of nodes in both lists is in the range [0, 50]
    - -100 <= Node.val <= 100
    - Both list1 and list2 are sorted in non-decreasing order

Time Complexity: O(n + m) - where n and m are lengths of the two lists
Space Complexity: O(1) - we only use a few pointers (iterative approach)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def merge_two_lists_iterative(
    list1: Optional[ListNode], 
    list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Merge two sorted linked lists iteratively.
    
    Approach:
        - Use a dummy node to simplify edge cases
        - Compare values from both lists
        - Attach the smaller node to the result
        - Move the pointer in the list we took from
        - Attach remaining nodes at the end
    
    Args:
        list1: Head of the first sorted linked list
        list2: Head of the second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Dummy node simplifies handling the head
    dummy = ListNode(0)
    current = dummy
    
    # Compare and merge while both lists have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining nodes (one list might still have nodes)
    current.next = list1 if list1 else list2
    
    return dummy.next


def merge_two_lists_recursive(
    list1: Optional[ListNode], 
    list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Merge two sorted linked lists recursively.
    
    Approach:
        - Base case: if one list is empty, return the other
        - Compare the heads of both lists
        - The smaller one becomes part of the result
        - Recursively merge the rest
    
    Note: This uses O(n + m) space due to recursion stack
    
    Args:
        list1: Head of the first sorted linked list
        list2: Head of the second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Base cases: if one list is empty, return the other
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Compare heads and recursively merge
    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2


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
    # Test Case 1: Two normal sorted lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = merge_two_lists_iterative(list1, list2)
    print(f"Test 1: {linked_list_to_array(merged)}")  # Expected: [1, 1, 2, 3, 4, 4]
    
    # Test Case 2: Both empty
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = merge_two_lists_iterative(list1, list2)
    print(f"Test 2: {linked_list_to_array(merged)}")  # Expected: []
    
    # Test Case 3: One empty, one with element
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = merge_two_lists_iterative(list1, list2)
    print(f"Test 3: {linked_list_to_array(merged)}")  # Expected: [0]
    
    # Test Case 4: Using recursive approach
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])
    merged = merge_two_lists_recursive(list1, list2)
    print(f"Test 4 (Recursive): {linked_list_to_array(merged)}")  # Expected: [1, 2, 3, 4, 5, 6]
    
    # Test Case 5: Different lengths
    list1 = create_linked_list([1, 2])
    list2 = create_linked_list([3, 4, 5, 6, 7])
    merged = merge_two_lists_iterative(list1, list2)
    print(f"Test 5: {linked_list_to_array(merged)}")  # Expected: [1, 2, 3, 4, 5, 6, 7]
    
    print("\nAll tests passed!")
