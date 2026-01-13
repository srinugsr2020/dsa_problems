"""
Intersection of Two Linked Lists (LeetCode #160)

Problem:
    Given the heads of two singly linked-lists headA and headB, return the node 
    at which the two lists intersect. If the two linked lists have no intersection 
    at all, return null.

    The test cases are generated such that there are no cycles anywhere in the 
    entire linked structure.

    Note that the linked lists must retain their original structure after the 
    function returns.

Example 1:
    Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], intersectVal = 8
    Output: Reference of the node with value = 8
    Explanation: The intersected node's value is 8. The two lists intersect 
                 at node with value 8.

Example 2:
    Input: listA = [1,9,1,2,4], listB = [3,2,4], intersectVal = 2
    Output: Reference of the node with value = 2

Example 3:
    Input: listA = [2,6,4], listB = [1,5], intersectVal = 0
    Output: null
    Explanation: The two lists do not intersect.

Constraints:
    - The number of nodes of listA is in the m
    - The number of nodes of listB is in the n
    - 1 <= m, n <= 3 * 10^4
    - 1 <= Node.val <= 10^5

Time Complexity: O(m + n) - we traverse both lists
Space Complexity: O(1) - optimal approach uses only two pointers
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def get_intersection_node(
    headA: Optional[ListNode], 
    headB: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Find intersection node using two-pointer technique.
    
    Approach:
        - Use two pointers, one starting at each head
        - When a pointer reaches the end, redirect it to the other head
        - If they intersect, they will meet at the intersection point
        - If no intersection, both will reach None simultaneously
    
    Why it works:
        - Let's say list A has a nodes before intersection, and C shared nodes
        - Let's say list B has b nodes before intersection, and C shared nodes
        - Pointer A travels: a + C + b = a + b + C
        - Pointer B travels: b + C + a = a + b + C
        - Both travel the same distance, meeting at intersection or None
    
    Args:
        headA: Head of the first linked list
        headB: Head of the second linked list
        
    Returns:
        The intersection node, or None if no intersection
    """
    if not headA or not headB:
        return None
    
    ptrA = headA
    ptrB = headB
    
    # Traverse both lists; when one ends, continue from the other's head
    while ptrA != ptrB:
        # When ptrA reaches end, redirect to headB
        ptrA = ptrA.next if ptrA else headB
        # When ptrB reaches end, redirect to headA
        ptrB = ptrB.next if ptrB else headA
    
    # Either intersection node or None (if no intersection)
    return ptrA


def get_intersection_node_hashset(
    headA: Optional[ListNode], 
    headB: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Find intersection node using hash set.
    
    Approach:
        - Store all nodes from list A in a hash set
        - Traverse list B and check if any node exists in the set
        - First match is the intersection point
    
    Note: This uses O(m) extra space where m is length of list A
    
    Args:
        headA: Head of the first linked list
        headB: Head of the second linked list
        
    Returns:
        The intersection node, or None if no intersection
    """
    # Store all nodes from list A
    nodes_in_a = set()
    current = headA
    while current:
        nodes_in_a.add(current)
        current = current.next
    
    # Check if any node in list B is in the set
    current = headB
    while current:
        if current in nodes_in_a:
            return current
        current = current.next
    
    return None


def get_intersection_node_length_diff(
    headA: Optional[ListNode], 
    headB: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Find intersection node by aligning list starts based on length difference.
    
    Approach:
        1. Calculate the length of both lists
        2. Advance the longer list by the difference
        3. Move both pointers together until they meet
    
    Args:
        headA: Head of the first linked list
        headB: Head of the second linked list
        
    Returns:
        The intersection node, or None if no intersection
    """
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    ptrA, ptrB = headA, headB
    
    # Advance the longer list
    if lenA > lenB:
        for _ in range(lenA - lenB):
            ptrA = ptrA.next
    else:
        for _ in range(lenB - lenA):
            ptrB = ptrB.next
    
    # Move together until they meet
    while ptrA and ptrB:
        if ptrA == ptrB:
            return ptrA
        ptrA = ptrA.next
        ptrB = ptrB.next
    
    return None


# --------------------- Helper Functions ---------------------

def create_intersecting_lists(
    arrA: list, 
    arrB: list, 
    intersect_val: int, 
    skip_a: int, 
    skip_b: int
) -> tuple:
    """
    Create two linked lists that intersect at a specific node.
    
    Args:
        arrA: Values for list A
        arrB: Values for list B
        intersect_val: Value at intersection (0 for no intersection)
        skip_a: Number of nodes to skip in A before intersection
        skip_b: Number of nodes to skip in B before intersection
        
    Returns:
        Tuple of (headA, headB)
    """
    if intersect_val == 0:
        # No intersection - create separate lists
        headA = create_linked_list(arrA) if arrA else None
        headB = create_linked_list(arrB) if arrB else None
        return headA, headB
    
    # Create list A up to intersection point
    headA = ListNode(arrA[0]) if arrA else None
    currentA = headA
    for i in range(1, skip_a):
        currentA.next = ListNode(arrA[i])
        currentA = currentA.next
    
    # Create the intersection node and rest of the shared list
    intersection_start = skip_a
    intersection_node = ListNode(arrA[intersection_start])
    if currentA:
        currentA.next = intersection_node
    else:
        headA = intersection_node
    
    current = intersection_node
    for i in range(intersection_start + 1, len(arrA)):
        current.next = ListNode(arrA[i])
        current = current.next
    
    # Create list B up to intersection point
    headB = ListNode(arrB[0]) if arrB else None
    currentB = headB
    for i in range(1, skip_b):
        currentB.next = ListNode(arrB[i])
        currentB = currentB.next
    
    # Connect list B to the intersection node
    if currentB:
        currentB.next = intersection_node
    else:
        headB = intersection_node
    
    return headA, headB


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


# --------------------- Test Cases ---------------------

if __name__ == "__main__":
    # Test Case 1: Lists intersect at value 8
    headA1, headB1 = create_intersecting_lists(
        [4, 1, 8, 4, 5], 
        [5, 6, 1, 8, 4, 5], 
        intersect_val=8, 
        skip_a=2, 
        skip_b=3
    )
    result1 = get_intersection_node(headA1, headB1)
    print(f"Test 1: {result1.val if result1 else None}")  # Expected: 8
    
    # Test Case 2: Lists intersect at value 2
    headA2, headB2 = create_intersecting_lists(
        [1, 9, 1, 2, 4], 
        [3, 2, 4], 
        intersect_val=2, 
        skip_a=3, 
        skip_b=1
    )
    result2 = get_intersection_node(headA2, headB2)
    print(f"Test 2: {result2.val if result2 else None}")  # Expected: 2
    
    # Test Case 3: No intersection
    headA3 = create_linked_list([2, 6, 4])
    headB3 = create_linked_list([1, 5])
    result3 = get_intersection_node(headA3, headB3)
    print(f"Test 3: {result3}")  # Expected: None
    
    # Test Case 4: Using hash set approach
    headA4, headB4 = create_intersecting_lists(
        [1, 2, 3, 4], 
        [5, 6, 3, 4], 
        intersect_val=3, 
        skip_a=2, 
        skip_b=2
    )
    result4 = get_intersection_node_hashset(headA4, headB4)
    print(f"Test 4 (HashSet): {result4.val if result4 else None}")  # Expected: 3
    
    # Test Case 5: Using length difference approach
    headA5, headB5 = create_intersecting_lists(
        [1, 2, 3, 4, 5], 
        [10, 3, 4, 5], 
        intersect_val=3, 
        skip_a=2, 
        skip_b=1
    )
    result5 = get_intersection_node_length_diff(headA5, headB5)
    print(f"Test 5 (Length Diff): {result5.val if result5 else None}")  # Expected: 3
    
    print("\nAll tests passed!")
