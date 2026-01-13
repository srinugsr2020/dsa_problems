"""
Two Sum Problem (Two Pointers Approach)

Problem Statement:
------------------
Given a sorted array of integers 'nums' and an integer 'target', return the indices 
of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.

Return the answer as a list of two indices [index1, index2] where index1 < index2.

Note: The indices are 0-based.

Constraints:
------------
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- The array is sorted in ascending order
- Only one valid answer exists

Examples:
---------
Example 1:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Example 2:
    Input: nums = [2, 3, 4], target = 6
    Output: [0, 2]
    Explanation: nums[0] + nums[2] = 2 + 4 = 6

Example 3:
    Input: nums = [-1, 0], target = -1
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = -1 + 0 = -1

Example 4:
    Input: nums = [1, 2, 3, 4, 5, 6], target = 10
    Output: [3, 5]
    Explanation: nums[3] + nums[5] = 4 + 6 = 10

Hints:
------
1. Since the array is sorted, you can use the two pointers technique
2. Start with one pointer at the beginning and one at the end
3. Calculate the sum of elements at both pointers
4. If sum equals target, you found the answer
5. If sum is less than target, move the left pointer right
6. If sum is greater than target, move the right pointer left

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers in a sorted array that add up to the target.
    
    Args:
        nums: A sorted list of integers
        target: The target sum
    
    Returns:
        A list containing two indices [index1, index2] where nums[index1] + nums[index2] = target
    
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    hash_dict = {}
    left, right = 0, len(nums) - 1
    while left <= right:
        diff = target - nums[left]
        if hash_dict.get(diff) is not None:
            return [hash_dict[diff], left]
        hash_dict[nums[left]] = left
        left += 1
    pass


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")
    print(f"Expected: [0, 1]\n")
    
    # Test case 2
    nums2 = [2, 3, 4]
    target2 = 6
    print(f"Test 2: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")
    print(f"Expected: [0, 2]\n")
    
    # Test case 3
    nums3 = [-1, 0]
    target3 = -1
    print(f"Test 3: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")
    print(f"Expected: [0, 1]\n")
    
    # Test case 4
    nums4 = [1, 2, 3, 4, 5, 6]
    target4 = 10
    print(f"Test 4: nums = {nums4}, target = {target4}")
    print(f"Output: {two_sum(nums4, target4)}")
    print(f"Expected: [3, 5]\n")
    
    # Test case 5: Edge case with negative numbers
    nums5 = [-5, -2, 0, 3, 7]
    target5 = 1
    print(f"Test 5: nums = {nums5}, target = {target5}")
    print(f"Output: {two_sum(nums5, target5)}")
    print(f"Expected: [1, 3]\n")
