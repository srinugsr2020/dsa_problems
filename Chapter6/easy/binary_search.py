"""
Binary Search Problem

Problem Statement:
------------------
Given a sorted array of distinct integers 'nums' and a target value 'target',
return the index if the target is found. If not, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique
- nums is sorted in ascending order

Examples:
---------
Example 1:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Example 3:
    Input: nums = [5], target = 5
    Output: 0
    Explanation: Single element array, target found at index 0

Example 4:
    Input: nums = [2, 5], target = 5
    Output: 1
    Explanation: Target found at index 1

Visual Explanation:
-------------------
nums = [-1, 0, 3, 5, 9, 12], target = 9

Step 1: left=0, right=5, mid=2
        nums[2]=3 < 9, search right half
        [-1, 0, 3, 5, 9, 12]
         L      M        R

Step 2: left=3, right=5, mid=4
        nums[4]=9 == 9, found!
        [-1, 0, 3, 5, 9, 12]
                  L  M   R

Return: 4

Hints:
------
1. Initialize left and right pointers at the start and end of the array
2. Calculate mid using left + (right - left) // 2 to avoid overflow
3. If nums[mid] == target, return mid
4. If nums[mid] < target, search in the right half (left = mid + 1)
5. If nums[mid] > target, search in the left half (right = mid - 1)
6. If left > right, the target is not found

Expected Time Complexity: O(log n)
Expected Space Complexity: O(1)
"""


def binary_search(nums: list[int], target: int) -> int:
    """
    Search for target in a sorted array using binary search.
    
    Args:
        nums: A sorted list of distinct integers
        target: The integer to search for
    
    Returns:
        The index of target if found, -1 otherwise
    
    Example:
        >>> binary_search([-1, 0, 3, 5, 9, 12], 9)
        4
        >>> binary_search([-1, 0, 3, 5, 9, 12], 2)
        -1
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
    
    return -1


# Test cases
if __name__ == "__main__":
    # Test case 1: Target exists in the middle
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Output: {binary_search(nums1, target1)}")
    print(f"Expected: 4\n")
    
    # Test case 2: Target does not exist
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Test 2: nums = {nums2}, target = {target2}")
    print(f"Output: {binary_search(nums2, target2)}")
    print(f"Expected: -1\n")
    
    # Test case 3: Single element array, target found
    nums3 = [5]
    target3 = 5
    print(f"Test 3: nums = {nums3}, target = {target3}")
    print(f"Output: {binary_search(nums3, target3)}")
    print(f"Expected: 0\n")
    
    # Test case 4: Two element array
    nums4 = [2, 5]
    target4 = 5
    print(f"Test 4: nums = {nums4}, target = {target4}")
    print(f"Output: {binary_search(nums4, target4)}")
    print(f"Expected: 1\n")
    
    # Test case 5: Target at the beginning
    nums5 = [1, 2, 3, 4, 5]
    target5 = 1
    print(f"Test 5: nums = {nums5}, target = {target5}")
    print(f"Output: {binary_search(nums5, target5)}")
    print(f"Expected: 0\n")
    
    # Test case 6: Target at the end
    nums6 = [1, 2, 3, 4, 5]
    target6 = 5
    print(f"Test 6: nums = {nums6}, target = {target6}")
    print(f"Output: {binary_search(nums6, target6)}")
    print(f"Expected: 4\n")
    
    # Test case 7: Target smaller than all elements
    nums7 = [2, 4, 6, 8, 10]
    target7 = 1
    print(f"Test 7: nums = {nums7}, target = {target7}")
    print(f"Output: {binary_search(nums7, target7)}")
    print(f"Expected: -1\n")
    
    # Test case 8: Target larger than all elements
    nums8 = [2, 4, 6, 8, 10]
    target8 = 12
    print(f"Test 8: nums = {nums8}, target = {target8}")
    print(f"Output: {binary_search(nums8, target8)}")
    print(f"Expected: -1\n")
