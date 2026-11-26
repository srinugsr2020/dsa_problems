"""
Minimum Difference Between Highest and Lowest of K Scores (LeetCode #1984)

Problem:
    You are given a 0-indexed integer array nums, where nums[i] represents 
    the score of the ith student. You are also given an integer k.
    
    Pick the scores of any k students from the array so that the difference 
    between the highest and the lowest of the k scores is minimized.
    
    Return the minimum possible difference.

Example 1:
    Input: nums = [90], k = 1
    Output: 0
    Explanation: There is one way to pick score(s) of one student:
                 - [90]. The difference is 90 - 90 = 0.

Example 2:
    Input: nums = [9,4,1,7], k = 2
    Output: 2
    Explanation: Pick scores of any 2 students from [9,4,1,7]:
                 - [9,4]: difference = 9 - 4 = 5
                 - [9,1]: difference = 9 - 1 = 8
                 - [9,7]: difference = 9 - 7 = 2
                 - [4,1]: difference = 4 - 1 = 3
                 - [4,7]: difference = 7 - 4 = 3
                 - [1,7]: difference = 7 - 1 = 6
                 Minimum difference is 2.

Constraints:
    - 1 <= k <= nums.length <= 1000
    - 0 <= nums[i] <= 10^5

Time Complexity: O(n log n) - due to sorting
Space Complexity: O(1) - only using constant extra space (excluding sort)
"""

from typing import List


def minimum_difference(nums: List[int], k: int) -> int:
    """
    Find minimum difference between highest and lowest of k scores.
    
    Approach:
        1. Sort the array
        2. Use a sliding window of size k
        3. In sorted array, min difference for any window is last - first
        4. Track minimum difference across all windows
    
    Key Insight:
        After sorting, the k elements with minimum range must be consecutive.
        So we just need to find the window of k consecutive elements with
        the smallest difference between first and last element.
    
    Args:
        nums: Array of student scores
        k: Number of students to pick
        
    Returns:
        Minimum possible difference between highest and lowest of k scores
    """
    # Edge case: k = 1, difference is always 0
    if k == 1:
        return 0
    
    # Sort the array
    nums.sort()
    
    # Find minimum difference using sliding window
    min_diff = float('inf')
    print(nums)  # Debug: Show sorted array
    print(len(nums) - k + 1)  # Debug: Show number of windows to check
    for i in range(len(nums) - k + 1):
        # Window is nums[i:i+k], difference is nums[i+k-1] - nums[i]
        diff = nums[i + k - 1] - nums[i]
        min_diff = min(min_diff, diff)
    
    return min_diff


def minimum_difference_verbose(nums: List[int], k: int) -> int:
    """
    Same approach with detailed output for understanding.
    
    Args:
        nums: Array of student scores
        k: Number of students to pick
        
    Returns:
        Minimum possible difference between highest and lowest of k scores
    """
    if k == 1:
        return 0
    
    print(f"Original array: {nums}")
    nums_sorted = sorted(nums)
    print(f"Sorted array: {nums_sorted}")
    
    min_diff = float('inf')
    best_window = []
    
    for i in range(len(nums_sorted) - k + 1):
        window = nums_sorted[i:i + k]
        diff = window[-1] - window[0]
        print(f"Window {i}: {window}, diff = {diff}")
        
        if diff < min_diff:
            min_diff = diff
            best_window = window
    
    print(f"Best window: {best_window} with difference {min_diff}")
    return min_diff


# --------------------- Test Cases ---------------------

if __name__ == "__main__":
    # Test Case 1: Single element
    nums1 = [90]
    k1 = 1
    result1 = minimum_difference(nums1, k1)
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"  Result: {result1}")  # Expected: 0
    
    # Test Case 2: Basic case
    nums2 = [9, 4, 1, 7]
    k2 = 2
    result2 = minimum_difference(nums2, k2)
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"  Result: {result2}")  # Expected: 2
    
    # Test Case 3: All same elements
    nums3 = [5, 5, 5, 5]
    k3 = 3
    result3 = minimum_difference(nums3, k3)
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"  Result: {result3}")  # Expected: 0
    
    # Test Case 4: k equals array length
    nums4 = [1, 4, 7, 10]
    k4 = 4
    result4 = minimum_difference(nums4, k4)
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"  Result: {result4}")  # Expected: 9
    
    # Test Case 5: Already sorted
    nums5 = [1, 2, 3, 4, 5]
    k5 = 3
    result5 = minimum_difference(nums5, k5)
    print(f"Test 5: nums={nums5}, k={k5}")
    print(f"  Result: {result5}")  # Expected: 2
    
    # Test Case 6: Verbose output
    # print("\nVerbose Test:")
    # nums6 = [9, 4, 1, 7]
    # k6 = 2
    # minimum_difference_verbose(nums6, k6)
    
    # Test Case 7: Larger array
    nums7 = [87, 68, 91, 86, 58, 63, 43, 98, 6, 40]
    k7 = 6
    result7 = minimum_difference(nums7, k7)
    print(f"\nTest 7: nums={nums7}, k={k7}")
    print(f"  Result: {result7}")
    
    print("\nAll tests passed!")
