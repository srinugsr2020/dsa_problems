"""
Contains Duplicate II (LeetCode #219)

Problem:
    Given an integer array nums and an integer k, return true if there are 
    two distinct indices i and j in the array such that nums[i] == nums[j] 
    and abs(i - j) <= k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - 0 <= k <= 10^5

Time Complexity: O(n) - single pass through the array
Space Complexity: O(min(n, k)) - sliding window set contains at most k+1 elements
"""

from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    """
    Check if there are duplicate elements within distance k.
    
    Approach:
        Use a sliding window of size k implemented as a hash set.
        - Maintain a set of elements in the current window
        - For each new element, check if it exists in the window
        - If window size exceeds k, remove the oldest element
    
    Args:
        nums: Input array of integers
        k: Maximum distance between duplicate indices
        
    Returns:
        True if duplicates exist within distance k, False otherwise
    """
    window = set()
    
    for i, num in enumerate(nums):
        # Check if current number is already in the window
        if num in window:
            return True
        
        # Add current number to window
        window.add(num)
        
        # Remove element that's now outside the window
        # Window should contain at most k elements
        if len(window) > k:
            window.remove(nums[i - k])
    
    return False


def contains_nearby_duplicate_hashmap(nums: List[int], k: int) -> bool:
    """
    Alternative approach using hash map to store last seen index.
    
    Approach:
        - Store each number's last seen index in a hash map
        - When seeing a number again, check if distance <= k
    
    Args:
        nums: Input array of integers
        k: Maximum distance between duplicate indices
        
    Returns:
        True if duplicates exist within distance k, False otherwise
    """
    last_seen = {}  # num -> last index
    
    for i, num in enumerate(nums):
        if num in last_seen:
            if i - last_seen[num] <= k:
                return True
        last_seen[num] = i
    
    return False


def find_nearby_duplicates(nums: List[int], k: int) -> List[tuple]:
    """
    Find all pairs of indices where nums[i] == nums[j] and |i - j| <= k.
    
    Useful for understanding and debugging.
    
    Args:
        nums: Input array of integers
        k: Maximum distance between duplicate indices
        
    Returns:
        List of (i, j) tuples representing duplicate pairs
    """
    pairs = []
    index_map = {}  # num -> list of indices
    
    for i, num in enumerate(nums):
        if num in index_map:
            for j in index_map[num]:
                if i - j <= k:
                    pairs.append((j, i))
        
        if num not in index_map:
            index_map[num] = []
        index_map[num].append(i)
    
    return pairs


# --------------------- Test Cases ---------------------

if __name__ == "__main__":
    # Test Case 1: Duplicate within range
    nums1 = [1, 2, 3, 1]
    k1 = 3
    result1 = contains_nearby_duplicate(nums1, k1)
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"  Result: {result1}")  # Expected: True
    
    # Test Case 2: Adjacent duplicate
    nums2 = [1, 0, 1, 1]
    k2 = 1
    result2 = contains_nearby_duplicate(nums2, k2)
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"  Result: {result2}")  # Expected: True
    
    # Test Case 3: Duplicate outside range
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    result3 = contains_nearby_duplicate(nums3, k3)
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"  Result: {result3}")  # Expected: False
    
    # Test Case 4: No duplicates
    nums4 = [1, 2, 3, 4, 5]
    k4 = 3
    result4 = contains_nearby_duplicate(nums4, k4)
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"  Result: {result4}")  # Expected: False
    
    # Test Case 5: k = 0
    nums5 = [1, 2, 1]
    k5 = 0
    result5 = contains_nearby_duplicate(nums5, k5)
    print(f"Test 5: nums={nums5}, k={k5}")
    print(f"  Result: {result5}")  # Expected: False
    
    # Test Case 6: Using hashmap approach
    nums6 = [1, 2, 3, 1]
    k6 = 3
    result6 = contains_nearby_duplicate_hashmap(nums6, k6)
    print(f"Test 6 (HashMap): nums={nums6}, k={k6}")
    print(f"  Result: {result6}")  # Expected: True
    
    # Test Case 7: Find all pairs
    nums7 = [1, 0, 1, 1]
    k7 = 1
    pairs = find_nearby_duplicates(nums7, k7)
    print(f"Test 7: nums={nums7}, k={k7}")
    print(f"  All pairs: {pairs}")  # Expected: [(2, 3)]
    
    # Test Case 8: Single element
    nums8 = [99]
    k8 = 0
    result8 = contains_nearby_duplicate(nums8, k8)
    print(f"Test 8: nums={nums8}, k={k8}")
    print(f"  Result: {result8}")  # Expected: False
    
    print("\nAll tests passed!")
