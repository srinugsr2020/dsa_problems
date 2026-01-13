"""
Palindrome Linked List (LeetCode #234)

Problem:
    Given the head of a singly linked list, return true if it is a palindrome
    or false otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    - The number of nodes in the list is in the range [1, 10^5]
    - 0 <= Node.val <= 9

Time Complexity: O(n) - we traverse the list multiple times but still O(n)
Space Complexity: O(1) for optimal approach, O(n) for array approach
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def is_palindrome_optimal(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is palindrome using O(1) extra space.
    
    Approach:
        1. Find the middle of the linked list using slow/fast pointers
        2. Reverse the second half of the list
        3. Compare the first half with the reversed second half
        4. (Optional) Restore the list to original state
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if the list is a palindrome, False otherwise
    """
    if not head or not head.next:
        return True
    
    # Step 1: Find the middle using slow/fast pointers
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    second_half_start = reverse_list(slow.next)
    
    # Step 3: Compare the first half with reversed second half
    first_half = head
    second_half = second_half_start
    is_palindrome = True
    
    while second_half:
        if first_half.val != second_half.val:
            is_palindrome = False
            break
        first_half = first_half.next
        second_half = second_half.next
    
    # Step 4 (Optional): Restore the list by reversing the second half back
    slow.next = reverse_list(second_half_start)
    
    return is_palindrome


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Helper function to reverse a linked list."""
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev


def is_palindrome_array(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is palindrome using array conversion.
    
    Approach:
        - Convert linked list to array
        - Use two pointers to check palindrome
    
    Note: This uses O(n) extra space
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if the list is a palindrome, False otherwise
    """
    # Convert to array
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Check palindrome using two pointers
    left, right = 0, len(values) - 1
    while left < right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1
    
    return True


def is_palindrome_recursive(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is palindrome using recursion.
    
    Approach:
        - Use recursion to reach the end of the list
        - Compare nodes from outside-in during recursion unwinding
        - Use a reference to track the front node
    
    Note: This uses O(n) space due to recursion stack
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if the list is a palindrome, False otherwise
    """
    # Use a list to hold reference to front node (allows modification in nested function)
    front = [head]
    
    def check_palindrome(current: Optional[ListNode]) -> bool:
        if not current:
            return True
        
        # Recurse to end of list first
        if not check_palindrome(current.next):
            return False
        
        # Compare front and current (from back)
        if front[0].val != current.val:
            return False
        
        # Move front pointer forward
        front[0] = front[0].next
        return True
    
    return check_palindrome(head)


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
    # Test Case 1: Even length palindrome
    head1 = create_linked_list([1, 2, 2, 1])
    print(f"Test 1 (Optimal): {is_palindrome_optimal(head1)}")  # Expected: True
    
    # Test Case 2: Not a palindrome
    head2 = create_linked_list([1, 2])
    print(f"Test 2 (Optimal): {is_palindrome_optimal(head2)}")  # Expected: False
    
    # Test Case 3: Single element (always palindrome)
    head3 = create_linked_list([1])
    print(f"Test 3 (Optimal): {is_palindrome_optimal(head3)}")  # Expected: True
    
    # Test Case 4: Odd length palindrome
    head4 = create_linked_list([1, 2, 3, 2, 1])
    print(f"Test 4 (Array): {is_palindrome_array(head4)}")  # Expected: True
    
    # Test Case 5: All same values
    head5 = create_linked_list([1, 1, 1, 1])
    print(f"Test 5 (Array): {is_palindrome_array(head5)}")  # Expected: True
    
    # Test Case 6: Three elements, not palindrome
    head6 = create_linked_list([1, 2, 3])
    print(f"Test 6 (Recursive): {is_palindrome_recursive(head6)}")  # Expected: False
    
    # Test Case 7: Three elements, palindrome
    head7 = create_linked_list([1, 2, 1])
    print(f"Test 7 (Recursive): {is_palindrome_recursive(head7)}")  # Expected: True
    
    print("\nAll tests passed!")
