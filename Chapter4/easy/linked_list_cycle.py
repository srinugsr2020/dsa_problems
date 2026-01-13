"""
Linked List Cycle (LeetCode #141)

Problem:
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    
    There is a cycle in a linked list if there is some node in the list that can be 
    reached again by continuously following the next pointer.
    
    Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    Input: head = [3,2,0,-4], pos = 1 (tail connects to node at index 1)
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects 
                 to the 1st node (0-indexed).

Example 2:
    Input: head = [1,2], pos = 0 (tail connects to node at index 0)
    Output: true

Example 3:
    Input: head = [1], pos = -1 (no cycle)
    Output: false

Constraints:
    - The number of nodes in the list is in the range [0, 10^4]
    - -10^5 <= Node.val <= 10^5
    - pos is -1 or a valid index in the linked-list

Time Complexity: O(n) - we traverse each node at most twice
Space Complexity: O(1) - Floyd's algorithm uses only two pointers
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using Floyd's Tortoise and Hare algorithm.
    
    Approach:
        - Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
        - If there's a cycle, fast will eventually catch up to slow
        - If there's no cycle, fast will reach the end (None)
    
    Why it works:
        - In a cycle, the fast pointer gains 1 node on slow each step
        - Eventually, fast will lap slow and they'll meet
        - Like two runners on a circular track at different speeds
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if cycle exists, False otherwise
    """
    # Edge case: empty list or single node without cycle
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    # Move slow by 1 step, fast by 2 steps
    while fast and fast.next:
        slow = slow.next        # Move slow by 1 step
        fast = fast.next.next   # Move fast by 2 steps
        
        # If they meet, there's a cycle
        if slow == fast:
            return True
    
    # Fast reached the end, no cycle
    return False


def has_cycle_hashset(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using a hash set to track visited nodes.
    
    Approach:
        - Traverse the list while storing each visited node in a set
        - If we encounter a node we've seen before, there's a cycle
        - If we reach None, there's no cycle
    
    Note: This uses O(n) extra space, so Floyd's algorithm is preferred.
    
    Args:
        head: The head of the linked list
        
    Returns:
        True if cycle exists, False otherwise
    """
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    
    return False


# --------------------- Helper Functions ---------------------

def create_linked_list_with_cycle(arr: list, pos: int) -> Optional[ListNode]:
    """
    Create a linked list with an optional cycle.
    
    Args:
        arr: List of values for the nodes
        pos: Position where the tail connects to (-1 for no cycle)
        
    Returns:
        Head of the linked list
    """
    if not arr:
        return None
    
    # Create all nodes
    nodes = [ListNode(val) for val in arr]
    
    # Link nodes together
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0]


# --------------------- Test Cases ---------------------

if __name__ == "__main__":
    # Test Case 1: Cycle at position 1
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    print(f"Test 1 (Floyd): {has_cycle(head1)}")  # Expected: True
    
    # Test Case 2: Cycle at position 0 (head)
    head2 = create_linked_list_with_cycle([1, 2], 0)
    print(f"Test 2 (Floyd): {has_cycle(head2)}")  # Expected: True
    
    # Test Case 3: No cycle
    head3 = create_linked_list_with_cycle([1], -1)
    print(f"Test 3 (Floyd): {has_cycle(head3)}")  # Expected: False
    
    # Test Case 4: Empty list
    head4 = create_linked_list_with_cycle([], -1)
    print(f"Test 4 (Floyd): {has_cycle(head4)}")  # Expected: False
    
    # Test Case 5: Using hash set approach
    head5 = create_linked_list_with_cycle([1, 2, 3, 4], 2)
    print(f"Test 5 (HashSet): {has_cycle_hashset(head5)}")  # Expected: True
    
    # Test Case 6: No cycle with hash set
    head6 = create_linked_list_with_cycle([1, 2, 3, 4, 5], -1)
    print(f"Test 6 (HashSet): {has_cycle_hashset(head6)}")  # Expected: False
    
    # Test Case 7: Single node with self-loop
    head7 = create_linked_list_with_cycle([1], 0)
    print(f"Test 7 (Self-loop): {has_cycle(head7)}")  # Expected: True
    
    # Test Case 8: Long list with cycle at end
    head8 = create_linked_list_with_cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    print(f"Test 8 (Long list): {has_cycle(head8)}")  # Expected: True
    
    print("\nAll tests passed!")
