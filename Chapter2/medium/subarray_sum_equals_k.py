"""
Subarray Sum Equals K Problem

Problem Statement:
------------------
Given an array of integers 'nums' and an integer 'k', return the total number of 
subarrays whose sum equals to 'k'.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
------------
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

Examples:
---------
Example 1:
    Input: nums = [1, 1, 1], k = 2
    Output: 2
    Explanation: Subarrays [1, 1] at indices (0,1) and (1,2) both sum to 2

Example 2:
    Input: nums = [1, 2, 3], k = 3
    Output: 2
    Explanation: Subarrays [1, 2] and [3] both sum to 3

Example 3:
    Input: nums = [1, -1, 0], k = 0
    Output: 3
    Explanation: Subarrays [1, -1], [-1, 0, 1] wait... let me recalculate
                 [1, -1] = 0, [0] = 0, [1, -1, 0] = 0 → 3 subarrays

Hints:
------
1. Brute force: check all subarrays O(n^2) or O(n^3)
2. Key insight: use prefix sums
3. If prefix_sum[j] - prefix_sum[i] = k, then subarray (i, j] sums to k
4. Rearranging: prefix_sum[i] = prefix_sum[j] - k
5. Use a hash map to count occurrences of each prefix sum
6. For each prefix_sum[j], count how many prefix_sum[i] = prefix_sum[j] - k exist

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
"""

from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    """
    Count subarrays with sum equal to k using prefix sum and hash map.
    
    The key insight:
    - prefix_sum[j] - prefix_sum[i] = sum of elements from i+1 to j
    - If this equals k, then prefix_sum[i] = prefix_sum[j] - k
    - We count how many times we've seen (current_prefix_sum - k)
    
    Args:
        nums: List of integers (can include negatives)
        k: Target sum
    
    Returns:
        Number of subarrays with sum equal to k
    
    Example:
        >>> subarray_sum([1, 1, 1], 2)
        2
    """
    count = 0
    prefix_sum = 0
    
    # Map: prefix_sum -> number of times this sum has occurred
    # Initialize with {0: 1} to handle subarrays starting from index 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    
    for num in nums:
        prefix_sum += num
        print(f"Current number: {num}, Updated prefix_sum: {prefix_sum}")
        # If (prefix_sum - k) exists, those are valid starting points
        # for subarrays ending at current position with sum = k
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]
            print(f"  Found {prefix_count[prefix_sum - k]} subarray(s) ending here with sum = {k}")
        # Record this prefix sum
        print(prefix_count)
        prefix_count[prefix_sum] += 1
    
    return count


def subarray_sum_verbose(nums: list[int], k: int) -> int:
    """
    Same algorithm with verbose output to understand the process.
    
    Args:
        nums: List of integers
        k: Target sum
    
    Returns:
        Number of subarrays with sum equal to k
    """
    count = 0
    prefix_sum = 0
    prefix_count = {0: 1}
    
    print(f"Looking for subarrays with sum = {k}")
    print(f"Initial: prefix_count = {prefix_count}\n")
    
    for i, num in enumerate(nums):
        prefix_sum += num
        target = prefix_sum - k
        
        print(f"Index {i}, num = {num}")
        print(f"  prefix_sum = {prefix_sum}")
        print(f"  Looking for: prefix_sum - k = {prefix_sum} - {k} = {target}")
        
        if target in prefix_count:
            found = prefix_count[target]
            count += found
            print(f"  Found {found} occurrence(s) of {target} → count += {found}")
        else:
            print(f"  {target} not in prefix_count")
        
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        print(f"  Updated prefix_count = {prefix_count}\n")
    
    return count


def subarray_sum_brute_force(nums: list[int], k: int) -> int:
    """
    Brute force approach: check all subarrays.
    
    Time: O(n^2)
    
    Args:
        nums: List of integers
        k: Target sum
    
    Returns:
        Number of subarrays with sum equal to k
    """
    count = 0
    n = len(nums)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    
    return count


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1]
    k1 = 2
    print(f"Test 1: nums = {nums1}, k = {k1}")
    print(f"Output: {subarray_sum(nums1, k1)}")
    print(f"Expected: 2\n")
    
    # Test case 2
    nums2 = [1, 2, 3]
    k2 = 3
    print(f"Test 2: nums = {nums2}, k = {k2}")
    print(f"Output: {subarray_sum(nums2, k2)}")
    print(f"Expected: 2\n")
    
    # Test case 3: With zeros and negatives
    nums3 = [1, -1, 0]
    k3 = 0
    print(f"Test 3: nums = {nums3}, k = {k3}")
    print(f"Output: {subarray_sum(nums3, k3)}")
    print(f"Expected: 3\n")
    
    # Test case 4: Negative numbers
    nums4 = [-1, -1, 1]
    k4 = 0
    print(f"Test 4: nums = {nums4}, k = {k4}")
    print(f"Output: {subarray_sum(nums4, k4)}")
    print(f"Expected: 1\n")
    
    # Test case 5: Single element equals k
    nums5 = [3]
    k5 = 3
    print(f"Test 5: nums = {nums5}, k = {k5}")
    print(f"Output: {subarray_sum(nums5, k5)}")
    print(f"Expected: 1\n")
    
    # Test case 6: No valid subarray
    nums6 = [1, 2, 3]
    k6 = 7
    print(f"Test 6: nums = {nums6}, k = {k6}")
    print(f"Output: {subarray_sum(nums6, k6)}")
    print(f"Expected: 0\n")
    
    # Verbose example to understand the algorithm
    print("=" * 50)
    print("VERBOSE EXAMPLE")
    print("=" * 50)
    result = subarray_sum_verbose([1, 1, 1], 2)
    print(f"Final count: {result}")
    
    # Verify with brute force
    print("\n--- Verifying with brute force ---")
    print(f"Brute force Test 1: {subarray_sum_brute_force(nums1, k1)}")
    print(f"Brute force Test 2: {subarray_sum_brute_force(nums2, k2)}")
    print(f"Brute force Test 3: {subarray_sum_brute_force(nums3, k3)}")
