"""
Intersection of Two Arrays Problem

Problem Statement:
------------------
Given two integer arrays 'nums1' and 'nums2', return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Constraints:
------------
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

Examples:
---------
Example 1:
    Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    Output: [2]

Example 2:
    Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
    Output: [9, 4] or [4, 9]
    Explanation: [4, 9] is also accepted

Hints:
------
1. Convert both arrays to sets to remove duplicates
2. Use set intersection operation to find common elements
3. Alternatively, iterate through one set and check membership in the other
4. The result should only contain unique elements

Expected Time Complexity: O(n + m) where n and m are lengths of the two arrays
Expected Space Complexity: O(n + m) for storing the sets
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Find the intersection of two arrays (unique elements only).
    
    Args:
        nums1: First list of integers
        nums2: Second list of integers
    
    Returns:
        A list of unique elements that appear in both arrays
    
    Example:
        >>> intersection([1, 2, 2, 1], [2, 2])
        [2]
    """
    # Convert both arrays to sets and use set intersection
    set1 = set(nums1)
    set2 = set(nums2)
    
    return list(set1 & set2)


def intersection_manual(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Alternative approach: manually iterate and check membership.
    
    Args:
        nums1: First list of integers
        nums2: Second list of integers
    
    Returns:
        A list of unique elements that appear in both arrays
    """
    set1 = set(nums1)
    result = set()
    
    for num in nums2:
        if num in set1:
            result.add(num)
    
    return list(result)


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1_a = [1, 2, 2, 1]
    nums2_a = [2, 2]
    print(f"Test 1: nums1 = {nums1_a}, nums2 = {nums2_a}")
    print(f"Output: {intersection(nums1_a, nums2_a)}")
    print(f"Expected: [2]\n")
    
    # Test case 2
    nums1_b = [4, 9, 5]
    nums2_b = [9, 4, 9, 8, 4]
    print(f"Test 2: nums1 = {nums1_b}, nums2 = {nums2_b}")
    print(f"Output: {intersection(nums1_b, nums2_b)}")
    print(f"Expected: [9, 4] or [4, 9]\n")
    
    # Test case 3: No intersection
    nums1_c = [1, 2, 3]
    nums2_c = [4, 5, 6]
    print(f"Test 3: nums1 = {nums1_c}, nums2 = {nums2_c}")
    print(f"Output: {intersection(nums1_c, nums2_c)}")
    print(f"Expected: []\n")
    
    # Test case 4: Complete overlap
    nums1_d = [1, 2, 3]
    nums2_d = [1, 2, 3]
    print(f"Test 4: nums1 = {nums1_d}, nums2 = {nums2_d}")
    print(f"Output: {intersection(nums1_d, nums2_d)}")
    print(f"Expected: [1, 2, 3]\n")
    
    # Test case 5: Single element arrays
    nums1_e = [1]
    nums2_e = [1]
    print(f"Test 5: nums1 = {nums1_e}, nums2 = {nums2_e}")
    print(f"Output: {intersection(nums1_e, nums2_e)}")
    print(f"Expected: [1]\n")
    
    # Test manual approach
    print("--- Testing manual approach ---")
    print(f"Manual approach Test 1: {intersection_manual(nums1_a, nums2_a)}")
    print(f"Manual approach Test 2: {intersection_manual(nums1_b, nums2_b)}")
