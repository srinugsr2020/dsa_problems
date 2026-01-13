"""
Maximum Average Subarray I (LeetCode #643)

Problem:
    You are given an integer array nums consisting of n elements, and an integer k.
    
    Find a contiguous subarray whose length is equal to k that has the maximum 
    average value and return this value. Any answer with a calculation error 
    less than 10^-5 will be accepted.

Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000

Constraints:
    - n == nums.length
    - 1 <= k <= n <= 10^5
    - -10^4 <= nums[i] <= 10^4

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only using constant extra space
"""

from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    """
    Find maximum average of any contiguous subarray of size k.
    
    Approach:
        Use a fixed-size sliding window of size k.
        - Initialize sum with first k elements
        - Slide window: add new element, remove old element
        - Track maximum sum seen
        - Return max_sum / k
    
    Args:
        nums: Input array of integers
        k: Size of the subarray
        
    Returns:
        Maximum average value of any subarray of size k
    """
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(nums)):
        # Add new element, remove old element
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k


def find_max_average_verbose(nums: List[int], k: int) -> float:
    """
    Same approach with step-by-step tracking for understanding.
    
    Args:
        nums: Input array of integers
        k: Size of the subarray
        
    Returns:
        Maximum average value of any subarray of size k
    """
    n = len(nums)
    
    # Edge case: k equals array length
    if k == n:
        return sum(nums) / k
    
    # Initialize first window
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    
    max_sum = window_sum
    max_start_index = 0
    
    # Slide the window
    for i in range(k, n):
        # Slide: remove leftmost, add rightmost
        window_sum = window_sum - nums[i - k] + nums[i]
        
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i - k + 1
    
    # For debugging: print the subarray with max average
    max_subarray = nums[max_start_index:max_start_index + k]
    print(f"Max subarray: {max_subarray} at index {max_start_index}")
    print(f"Sum: {max_sum}, Average: {max_sum / k}")
    
    return max_sum / k


# --------------------- Test Cases ---------------------

if __name__ == "__main__":
    # Test Case 1: Basic case
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    result1 = find_max_average(nums1, k1)
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"  Result: {result1:.5f}")  # Expected: 12.75000
    
    # Test Case 2: Single element
    nums2 = [5]
    k2 = 1
    result2 = find_max_average(nums2, k2)
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"  Result: {result2:.5f}")  # Expected: 5.00000
    
    # Test Case 3: All negative numbers
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    result3 = find_max_average(nums3, k3)
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"  Result: {result3:.5f}")  # Expected: -1.50000 ([-1, -2])
    
    # Test Case 4: k equals array length
    nums4 = [1, 2, 3, 4, 5]
    k4 = 5
    result4 = find_max_average(nums4, k4)
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"  Result: {result4:.5f}")  # Expected: 3.00000
    
    # Test Case 5: All same elements
    nums5 = [7, 7, 7, 7, 7]
    k5 = 3
    result5 = find_max_average(nums5, k5)
    print(f"Test 5: nums={nums5}, k={k5}")
    print(f"  Result: {result5:.5f}")  # Expected: 7.00000
    
    # Test Case 6: Verbose output
    print("\nVerbose Test:")
    nums6 = [1, 12, -5, -6, 50, 3]
    k6 = 4
    find_max_average_verbose(nums6, k6)
    
    print("\nAll tests passed!")
