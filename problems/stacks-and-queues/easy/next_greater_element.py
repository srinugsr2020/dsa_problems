"""
Next Greater Element I (LeetCode #496)

Problem:
The next greater element of some element x in an array is the first greater
element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where
nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
and determine the next greater element of nums2[j] in nums2. If there is no
next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater
element as described above.

Examples:
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]
    Explanation:
    - For 4, there is no next greater element, so answer is -1.
    - For 1, the next greater element in nums2 is 3.
    - For 2, there is no next greater element, so answer is -1.

    Input: nums1 = [2,4], nums2 = [1,2,3,4]
    Output: [3,-1]

Constraints:
    - 1 <= nums1.length <= nums2.length <= 1000
    - 0 <= nums1[i], nums2[i] <= 10^4
    - All integers in nums1 and nums2 are unique.
    - All integers in nums1 also appear in nums2.
"""

from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find next greater element using monotonic stack.
    
    Approach:
    - Build a map of each element to its next greater element in nums2
    - Use monotonic decreasing stack
    - Look up the answer for each element in nums1
    
    Time Complexity: O(n + m) where n = len(nums1), m = len(nums2)
    Space Complexity: O(m)
    """
    # Build next greater map for nums2
    next_greater = {}
    stack = []  # Monotonic decreasing stack
    
    for num in nums2:
        # Pop elements smaller than current - current is their next greater
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    # Elements remaining in stack have no next greater element
    while stack:
        next_greater[stack.pop()] = -1
    
    # Build result for nums1
    return [next_greater[num] for num in nums1]


def next_greater_element_brute(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Brute force approach for comparison.
    
    Time Complexity: O(n * m)
    Space Complexity: O(1) extra
    """
    result = []
    
    for num in nums1:
        # Find position in nums2
        idx = nums2.index(num)
        found = -1
        
        # Search for next greater
        for j in range(idx + 1, len(nums2)):
            if nums2[j] > num:
                found = nums2[j]
                break
        
        result.append(found)
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7]),
        ([1], [1], [-1]),
    ]
    
    for i, (nums1, nums2, expected) in enumerate(test_cases):
        result = next_greater_element(nums1, nums2)
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} next_greater_element({nums1}, {nums2})")
        print(f"         Result: {result}, Expected: {expected}")
