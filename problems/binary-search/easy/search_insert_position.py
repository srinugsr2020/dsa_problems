"""
Search Insert Position Problem

Problem Statement:
------------------
Given a sorted array of distinct integers and a target value, return the index 
if the target is found. If not, return the index where it would be if it were 
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order
- -10^4 <= target <= 10^4

Examples:
---------
Example 1:
    Input: nums = [1, 3, 5, 6], target = 5
    Output: 2
    Explanation: 5 is found at index 2

Example 2:
    Input: nums = [1, 3, 5, 6], target = 2
    Output: 1
    Explanation: 2 would be inserted at index 1

Example 3:
    Input: nums = [1, 3, 5, 6], target = 7
    Output: 4
    Explanation: 7 would be inserted at the end (index 4)

Example 4:
    Input: nums = [1, 3, 5, 6], target = 0
    Output: 0
    Explanation: 0 would be inserted at the beginning (index 0)

Visual Explanation:
-------------------
nums = [1, 3, 5, 6], target = 2

Step 1: left=0, right=3, mid=1
        nums[1]=3 > 2, search left half
        [1, 3, 5, 6]
         L  M     R

Step 2: left=0, right=0, mid=0
        nums[0]=1 < 2, search right half
        [1, 3, 5, 6]
         L
         M
         R

Step 3: left=1, right=0, left > right
        Return left=1 (insertion position)

Hints:
------
1. This is a variation of binary search finding the lower bound
2. When target is not found, left pointer will be at the insertion position
3. If target > all elements, return len(nums)
4. If target < all elements, return 0

Expected Time Complexity: O(log n)
Expected Space Complexity: O(1)
"""


def search_insert(nums: list[int], target: int) -> int:
    """
    Find the index of target or where it should be inserted.
    
    Args:
        nums: A sorted list of distinct integers
        target: The integer to search for or insert
    
    Returns:
        The index of target if found, or the index where it should be inserted
    
    Example:
        >>> search_insert([1, 3, 5, 6], 5)
        2
        >>> search_insert([1, 3, 5, 6], 2)
        1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


# Test cases
if __name__ == "__main__":
    # Test case 1: Target exists
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Output: {search_insert(nums1, target1)}")
    print(f"Expected: 2\n")
    
    # Test case 2: Target between elements
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(f"Test 2: nums = {nums2}, target = {target2}")
    print(f"Output: {search_insert(nums2, target2)}")
    print(f"Expected: 1\n")
    
    # Test case 3: Target greater than all elements
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(f"Test 3: nums = {nums3}, target = {target3}")
    print(f"Output: {search_insert(nums3, target3)}")
    print(f"Expected: 4\n")
    
    # Test case 4: Target less than all elements
    nums4 = [1, 3, 5, 6]
    target4 = 0
    print(f"Test 4: nums = {nums4}, target = {target4}")
    print(f"Output: {search_insert(nums4, target4)}")
    print(f"Expected: 0\n")
    
    # Test case 5: Single element, target found
    nums5 = [1]
    target5 = 1
    print(f"Test 5: nums = {nums5}, target = {target5}")
    print(f"Output: {search_insert(nums5, target5)}")
    print(f"Expected: 0\n")
    
    # Test case 6: Single element, target greater
    nums6 = [1]
    target6 = 2
    print(f"Test 6: nums = {nums6}, target = {target6}")
    print(f"Output: {search_insert(nums6, target6)}")
    print(f"Expected: 1\n")
    
    # Test case 7: Single element, target smaller
    nums7 = [1]
    target7 = 0
    print(f"Test 7: nums = {nums7}, target = {target7}")
    print(f"Output: {search_insert(nums7, target7)}")
    print(f"Expected: 0\n")
    
    # Test case 8: Target at the first position
    nums8 = [1, 3, 5, 6]
    target8 = 1
    print(f"Test 8: nums = {nums8}, target = {target8}")
    print(f"Output: {search_insert(nums8, target8)}")
    print(f"Expected: 0\n")
