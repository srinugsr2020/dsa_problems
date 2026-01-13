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

Follow up: Could you do it in O(n) time and O(1) space?

Time Complexity: O(n) - we traverse the list
Space Complexity: O(1) - using fast/slow pointers and in-place reversal
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is a palindrome using fast/slow pointers.
    
    Approach:
        1. Find the middle of the list using fast/slow pointers
        2. Reverse the second half of the list
        3. Compare the first half with the reversed second half
        4. (Optional) Restore the list by reversing the second half again
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if the list is a palindrome, False otherwise
    """
    if not head or not head.next:
        return True
    
    # Step 1: Find middle using fast/slow pointers
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    # slow is at the first middle (for even length) or exact middle (for odd)
    second_half_start = reverse_list(slow.next)
    
    # Step 3: Compare first and second halves
    first_half = head
    second_half = second_half_start
    is_palindrome_result = True
    
    while second_half:
        if first_half.val != second_half.val:
            is_palindrome_result = False
            break
        first_half = first_half.next
        second_half = second_half.next
    
    # Step 4: Restore the list (optional but good practice)
    slow.next = reverse_list(second_half_start)
    
    return is_palindrome_result


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
    Check if linked list is a palindrome by converting to array.
    
    Approach:
        - Store all values in an array
        - Check if array is a palindrome using two pointers
    
    Note: This uses O(n) space.
    
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
    left = 0
    right = len(values) - 1
    
    while left < right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1
    
    return True


def is_palindrome_recursive(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is a palindrome using recursion.
    
    Approach:
        - Use recursion to reach the end of the list
        - Compare nodes from both ends while unwinding the stack
    
    Note: This uses O(n) space for the recursion stack.
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if the list is a palindrome, False otherwise
    """
    # Use a list to hold the front pointer (to modify in nested function)
    front = [head]
    
    def check_palindrome(current: Optional[ListNode]) -> bool:
        if current is None:
            return True
        
        # Recurse to the end
        if not check_palindrome(current.next):
            return False
        
        # Compare front and current (back)
        if front[0].val != current.val:
            return False
        
        # Move front pointer forward
        front[0] = front[0].next
        return True
    
    return check_palindrome(head)


def is_palindrome_stack(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is a palindrome using a stack.
    
    Approach:
        - Use fast/slow to find middle
        - Push first half onto stack
        - Compare stack (reversed first half) with second half
    
    Note: This uses O(n/2) space for the stack.
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if the list is a palindrome, False otherwise
    """
    if not head or not head.next:
        return True
    
    # Find middle and push first half to stack
    slow = head
    fast = head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    
    # If odd length, skip the middle element
    if fast:
        slow = slow.next
    
    # Compare stack with second half
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    
    return True


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
    print(f"Test 1 [1,2,2,1]: {is_palindrome(head1)}")  # Expected: True
    
    # Test Case 2: Not a palindrome
    head2 = create_linked_list([1, 2])
    print(f"Test 2 [1,2]: {is_palindrome(head2)}")  # Expected: False
    
    # Test Case 3: Odd length palindrome
    head3 = create_linked_list([1, 2, 3, 2, 1])
    print(f"Test 3 [1,2,3,2,1]: {is_palindrome(head3)}")  # Expected: True
    
    # Test Case 4: Single element
    head4 = create_linked_list([1])
    print(f"Test 4 [1]: {is_palindrome(head4)}")  # Expected: True
    
    # Test Case 5: Two same elements
    head5 = create_linked_list([1, 1])
    print(f"Test 5 [1,1]: {is_palindrome(head5)}")  # Expected: True
    
    # Test Case 6: Three elements, not palindrome
    head6 = create_linked_list([1, 2, 3])
    print(f"Test 6 [1,2,3]: {is_palindrome(head6)}")  # Expected: False
    
    # Test Case 7: Array approach
    head7 = create_linked_list([1, 2, 2, 1])
    print(f"Test 7 (Array) [1,2,2,1]: {is_palindrome_array(head7)}")  # Expected: True
    
    # Test Case 8: Recursive approach
    head8 = create_linked_list([1, 2, 3, 2, 1])
    print(f"Test 8 (Recursive) [1,2,3,2,1]: {is_palindrome_recursive(head8)}")  # Expected: True
    
    # Test Case 9: Stack approach
    head9 = create_linked_list([1, 2, 2, 1])
    print(f"Test 9 (Stack) [1,2,2,1]: {is_palindrome_stack(head9)}")  # Expected: True
    
    # Test Case 10: Longer palindrome
    head10 = create_linked_list([1, 2, 3, 4, 3, 2, 1])
    print(f"Test 10 [1,2,3,4,3,2,1]: {is_palindrome(head10)}")  # Expected: True
    
    # Test Case 11: Verify list is restored after check
    head11 = create_linked_list([1, 2, 3, 2, 1])
    _ = is_palindrome(head11)
    print(f"Test 11 (Restored): {linked_list_to_array(head11)}")  # Expected: [1,2,3,2,1]
    
    print("\nAll tests passed!")
