"""
Longest Consecutive Sequence Problem

Problem Statement:
------------------
Given an unsorted array of integers 'nums', return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Constraints:
------------
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Examples:
---------
Example 1:
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Length = 4.

Example 2:
    Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9
    Explanation: The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Length = 9.

Example 3:
    Input: nums = []
    Output: 0

Hints:
------
1. Sorting would give O(n log n), but we need O(n)
2. Use a hash set for O(1) lookup
3. Key insight: only start counting from the START of a sequence
4. A number is the start of a sequence if (num - 1) is NOT in the set
5. From each start, count consecutive numbers until one is missing

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
"""


def longest_consecutive(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive sequence using a hash set.
    
    The key insight is to only start counting from sequence starts.
    A number is a sequence start if (num - 1) is not in the set.
    
    Args:
        nums: List of integers (unsorted, may contain duplicates)
    
    Returns:
        Length of the longest consecutive elements sequence
    
    Example:
        >>> longest_consecutive([100, 4, 200, 1, 3, 2])
        4
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting if this is the START of a sequence
        # (i.e., num - 1 is not in the set)
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length


def longest_consecutive_verbose(nums: list[int]) -> int:
    """
    Same algorithm with verbose output to understand the process.
    
    Args:
        nums: List of integers
    
    Returns:
        Length of the longest consecutive elements sequence
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    print(f"Input: {nums}")
    print(f"Set: {sorted(num_set)}\n")
    
    for num in sorted(num_set):  # Sorted just for clearer output
        if num - 1 not in num_set:
            print(f"Starting sequence at {num} (since {num - 1} not in set)")
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                print(f"  Extended to {current_num}, length = {current_length}")
            
            print(f"  Sequence: {list(range(num, current_num + 1))}, length = {current_length}")
            max_length = max(max_length, current_length)
        else:
            print(f"Skipping {num} (not a sequence start, {num - 1} exists)")
    
    return max_length


def longest_consecutive_sorting(nums: list[int]) -> int:
    """
    Alternative approach using sorting.
    
    Time: O(n log n) - doesn't meet the O(n) requirement but useful for comparison.
    
    Args:
        nums: List of integers
    
    Returns:
        Length of the longest consecutive elements sequence
    """
    if not nums:
        return 0
    
    # Remove duplicates and sort
    nums = sorted(set(nums))
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length


def longest_consecutive_union_find(nums: list[int]) -> int:
    """
    Alternative approach using Union-Find (Disjoint Set Union).
    
    Connect consecutive numbers and find the largest component.
    
    Args:
        nums: List of integers
    
    Returns:
        Length of the longest consecutive elements sequence
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    
    # parent[num] = parent of num in union-find
    parent = {num: num for num in num_set}
    # size[num] = size of component containing num
    size = {num: 1 for num in num_set}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            # Union by size
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]
    
    # Union consecutive numbers
    for num in num_set:
        if num + 1 in num_set:
            union(num, num + 1)
    
    return max(size.values())


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Test 1: nums = {nums1}")
    print(f"Output: {longest_consecutive(nums1)}")
    print(f"Expected: 4 (sequence: [1, 2, 3, 4])\n")
    
    # Test case 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"Test 2: nums = {nums2}")
    print(f"Output: {longest_consecutive(nums2)}")
    print(f"Expected: 9 (sequence: [0, 1, 2, 3, 4, 5, 6, 7, 8])\n")
    
    # Test case 3: Empty array
    nums3 = []
    print(f"Test 3: nums = {nums3}")
    print(f"Output: {longest_consecutive(nums3)}")
    print(f"Expected: 0\n")
    
    # Test case 4: Single element
    nums4 = [1]
    print(f"Test 4: nums = {nums4}")
    print(f"Output: {longest_consecutive(nums4)}")
    print(f"Expected: 1\n")
    
    # Test case 5: All same elements
    nums5 = [1, 1, 1, 1]
    print(f"Test 5: nums = {nums5}")
    print(f"Output: {longest_consecutive(nums5)}")
    print(f"Expected: 1\n")
    
    # Test case 6: Negative numbers
    nums6 = [-2, -1, 0, 1, 5, 6]
    print(f"Test 6: nums = {nums6}")
    print(f"Output: {longest_consecutive(nums6)}")
    print(f"Expected: 4 (sequence: [-2, -1, 0, 1])\n")
    
    # Verbose example
    print("=" * 50)
    print("VERBOSE EXAMPLE")
    print("=" * 50)
    result = longest_consecutive_verbose([100, 4, 200, 1, 3, 2])
    print(f"\nFinal answer: {result}")
    
    # Test all approaches
    print("\n--- Comparing all approaches ---")
    test_nums = [100, 4, 200, 1, 3, 2]
    print(f"Input: {test_nums}")
    print(f"Hash Set: {longest_consecutive(test_nums)}")
    print(f"Sorting: {longest_consecutive_sorting(test_nums)}")
    print(f"Union-Find: {longest_consecutive_union_find(test_nums)}")
