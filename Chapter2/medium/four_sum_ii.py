"""
4Sum II Problem

Problem Statement:
------------------
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number 
of tuples (i, j, k, l) such that:
    - 0 <= i, j, k, l < n
    - nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Constraints:
------------
- n == nums1.length == nums2.length == nums3.length == nums4.length
- 1 <= n <= 200
- -2^28 <= nums1[i], nums2[j], nums3[k], nums4[l] <= 2^28

Examples:
---------
Example 1:
    Input: nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]
    Output: 2
    Explanation: The two tuples are:
        1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
        2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:
    Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
    Output: 1

Hints:
------
1. Brute force would be O(n^4) - too slow
2. Key insight: split into two groups of two arrays each
3. Compute all possible sums of nums1[i] + nums2[j] and store in hash map
4. For each sum of nums3[k] + nums4[l], check if its negation exists in the map
5. This reduces complexity from O(n^4) to O(n^2)

Expected Time Complexity: O(n^2)
Expected Space Complexity: O(n^2)
"""

from collections import defaultdict


def four_sum_count(nums1: list[int], nums2: list[int], 
                   nums3: list[int], nums4: list[int]) -> int:
    """
    Count tuples (i, j, k, l) where nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0.
    
    Split the problem: store sums of first two arrays, then look up complements
    from sums of last two arrays.
    
    Args:
        nums1: First array of integers
        nums2: Second array of integers
        nums3: Third array of integers
        nums4: Fourth array of integers
    
    Returns:
        Number of tuples that sum to zero
    
    Example:
        >>> four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2])
        2
    """
    # Store all possible sums of nums1[i] + nums2[j] with their counts
    sum_ab = defaultdict(int)
    
    for a in nums1:
        for b in nums2:
            sum_ab[a + b] += 1
    
    # For each sum of nums3[k] + nums4[l], check if its negation exists
    count = 0
    for c in nums3:
        for d in nums4:
            target = -(c + d)
            if target in sum_ab:
                count += sum_ab[target]
    
    return count


def four_sum_count_verbose(nums1: list[int], nums2: list[int], 
                           nums3: list[int], nums4: list[int]) -> int:
    """
    Same algorithm with verbose output to understand the process.
    
    Args:
        nums1, nums2, nums3, nums4: Four arrays of integers
    
    Returns:
        Number of tuples that sum to zero
    """
    print("Step 1: Compute all sums of nums1[i] + nums2[j]")
    sum_ab = defaultdict(int)
    
    for i, a in enumerate(nums1):
        for j, b in enumerate(nums2):
            s = a + b
            sum_ab[s] += 1
            print(f"  nums1[{i}] + nums2[{j}] = {a} + {b} = {s}")
    
    print(f"\nSum map: {dict(sum_ab)}")
    print("\nStep 2: For each sum of nums3[k] + nums4[l], find complement")
    
    count = 0
    for k, c in enumerate(nums3):
        for l, d in enumerate(nums4):
            cd_sum = c + d
            target = -cd_sum
            print(f"  nums3[{k}] + nums4[{l}] = {c} + {d} = {cd_sum}, need {target}")
            
            if target in sum_ab:
                found = sum_ab[target]
                print(f"    Found {found} way(s) to make {target} from nums1+nums2")
                count += found
    
    return count


def four_sum_count_brute_force(nums1: list[int], nums2: list[int], 
                                nums3: list[int], nums4: list[int]) -> int:
    """
    Brute force approach: check all combinations.
    
    Time: O(n^4) - only for small inputs or verification.
    
    Args:
        nums1, nums2, nums3, nums4: Four arrays of integers
    
    Returns:
        Number of tuples that sum to zero
    """
    count = 0
    
    for a in nums1:
        for b in nums2:
            for c in nums3:
                for d in nums4:
                    if a + b + c + d == 0:
                        count += 1
    
    return count


def four_sum_count_counter(nums1: list[int], nums2: list[int], 
                           nums3: list[int], nums4: list[int]) -> int:
    """
    Alternative using Counter for cleaner code.
    
    Args:
        nums1, nums2, nums3, nums4: Four arrays of integers
    
    Returns:
        Number of tuples that sum to zero
    """
    from collections import Counter
    
    # Count all sums of first two arrays
    sum_ab = Counter(a + b for a in nums1 for b in nums2)
    
    # Count matching complements from last two arrays
    return sum(sum_ab[-(c + d)] for c in nums3 for d in nums4)


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1_a = [1, 2]
    nums2_a = [-2, -1]
    nums3_a = [-1, 2]
    nums4_a = [0, 2]
    print(f"Test 1:")
    print(f"  nums1 = {nums1_a}")
    print(f"  nums2 = {nums2_a}")
    print(f"  nums3 = {nums3_a}")
    print(f"  nums4 = {nums4_a}")
    print(f"  Output: {four_sum_count(nums1_a, nums2_a, nums3_a, nums4_a)}")
    print(f"  Expected: 2\n")
    
    # Test case 2: All zeros
    nums1_b = [0]
    nums2_b = [0]
    nums3_b = [0]
    nums4_b = [0]
    print(f"Test 2: All zeros")
    print(f"  Output: {four_sum_count(nums1_b, nums2_b, nums3_b, nums4_b)}")
    print(f"  Expected: 1\n")
    
    # Test case 3: No valid tuples
    nums1_c = [1]
    nums2_c = [1]
    nums3_c = [1]
    nums4_c = [1]
    print(f"Test 3: No valid tuples (all 1s)")
    print(f"  Output: {four_sum_count(nums1_c, nums2_c, nums3_c, nums4_c)}")
    print(f"  Expected: 0\n")
    
    # Test case 4: Multiple ways to sum to zero
    nums1_d = [0, 0]
    nums2_d = [0, 0]
    nums3_d = [0, 0]
    nums4_d = [0, 0]
    print(f"Test 4: Multiple zeros (2^4 = 16 combinations)")
    print(f"  Output: {four_sum_count(nums1_d, nums2_d, nums3_d, nums4_d)}")
    print(f"  Expected: 16\n")
    
    # Verbose example
    print("=" * 50)
    print("VERBOSE EXAMPLE")
    print("=" * 50)
    result = four_sum_count_verbose([1, 2], [-2, -1], [-1, 2], [0, 2])
    print(f"\nFinal count: {result}")
    
    # Verify with brute force
    print("\n--- Verifying with brute force ---")
    print(f"Brute force Test 1: {four_sum_count_brute_force(nums1_a, nums2_a, nums3_a, nums4_a)}")
    print(f"Counter Test 1: {four_sum_count_counter(nums1_a, nums2_a, nums3_a, nums4_a)}")
