"""
Contains Duplicate Problem

Problem Statement:
------------------
Given an integer array 'nums', return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Constraints:
------------
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Examples:
---------
Example 1:
    Input: nums = [1, 2, 3, 1]
    Output: true
    Explanation: 1 appears twice

Example 2:
    Input: nums = [1, 2, 3, 4]
    Output: false
    Explanation: All elements are distinct

Example 3:
    Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    Output: true
    Explanation: Multiple elements appear multiple times

Hints:
------
1. A brute force approach would compare every element with every other element (O(n^2))
2. Sorting the array would bring duplicates together (O(n log n))
3. A hash set can store elements we've seen so far with O(1) lookup time
4. Iterate through the array, checking if the current element is already in the set
5. If it is, return True. If not, add it to the set

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
"""


def contains_duplicate(nums: list[int]) -> bool:
    """
    Check if the array contains any duplicate elements.
    
    Args:
        nums: A list of integers
    
    Returns:
        True if any value appears at least twice, False otherwise
    
    Example:
        >>> contains_duplicate([1, 2, 3, 1])
        True
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Test 1: nums = {nums1}")
    print(f"Output: {contains_duplicate(nums1)}")
    print(f"Expected: True\n")
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    print(f"Test 2: nums = {nums2}")
    print(f"Output: {contains_duplicate(nums2)}")
    print(f"Expected: False\n")
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Test 3: nums = {nums3}")
    print(f"Output: {contains_duplicate(nums3)}")
    print(f"Expected: True\n")
    
    # Test case 4: Empty array (though constraint says length >= 1)
    nums4 = []
    print(f"Test 4: nums = {nums4}")
    print(f"Output: {contains_duplicate(nums4)}")
    print(f"Expected: False\n")
    
    # Test case 5: Single element
    nums5 = [1]
    print(f"Test 5: nums = {nums5}")
    print(f"Output: {contains_duplicate(nums5)}")
    print(f"Expected: False\n")
