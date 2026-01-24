"""
4Sum Problem (Sorting + Two Pointers)

Problem Statement:
------------------
Given an array nums of n integers, return an array of all the UNIQUE quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n
- a, b, c, and d are distinct (different indices)
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Important Notes:
----------------
1. The solution set must NOT contain duplicate quadruplets
2. The same element can be used multiple times if it appears multiple times in the array
3. The four indices must be different, but values can be the same
4. Order of quadruplets in result doesn't matter
5. Order within each quadruplet doesn't matter

Constraints:
------------
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

Examples:
---------
Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    Explanation:
        -2 + -1 + 1 + 2 = 0
        -2 + 0 + 0 + 2 = 0
        -1 + 0 + 0 + 1 = 0

Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
    Explanation:
        2 + 2 + 2 + 2 = 8
        Only one unique quadruplet even though there are multiple ways to pick indices

Example 3:
    Input: nums = [1,0,-1,0,-2,2], target = 1
    Output: [[-2,-1,2,2],[-2,0,1,2],[-1,0,1,1]]
    
Example 4:
    Input: nums = [-3,-1,0,2,4,5], target = 2
    Output: [[-3,-1,2,4],[-3,0,2,3]]
    Wait, that's wrong! Let me recalculate:
        -3 + -1 + 2 + 4 = 2 ✓
        -3 + 0 + 0 + 5 = 2 (but we don't have two 0s)
        -1 + 0 + 2 + 1 (we don't have 1)
    Output: [[-3,-1,2,4]]

Example 5:
    Input: nums = [], target = 0
    Output: []
    Explanation: Empty array, no quadruplets possible

Example 6:
    Input: nums = [1,2,3], target = 10
    Output: []
    Explanation: Not enough elements (need at least 4)

Understanding the Problem:
--------------------------
This is an extension of the 3Sum problem, but now we need FOUR numbers that sum 
to a target.

Key differences from 3Sum:
1. 3Sum target was always 0, here target can be any value
2. We need 4 numbers instead of 3
3. Same approach: sort + fix elements + two pointers

The Challenge:
--------------
The main difficulty is:
1. Avoiding duplicate quadruplets
2. Efficiently searching through 4 nested levels
3. Handling edge cases (not enough elements, all same values, etc.)

Approach: Sorting + Four Pointers (Two Fixed + Two Moving)
-----------------------------------------------------------
This is similar to 3Sum but with an extra layer:

1. SORT the array first
2. Use FOUR pointers:
   - First pointer (i): loops from 0 to n-4
   - Second pointer (j): loops from i+1 to n-3
   - Third pointer (left): starts at j+1
   - Fourth pointer (right): starts at n-1
3. For each combination of i and j, use two-pointer technique on left and right
4. Skip duplicates at ALL four levels

Algorithm Steps:
----------------
1. Sort the array in ascending order
2. If array length < 4, return empty list
3. Initialize result list
4. First loop (i from 0 to n-4):
   a. Skip duplicates: if i > 0 and nums[i] == nums[i-1], continue
   b. Second loop (j from i+1 to n-3):
      - Skip duplicates: if j > i+1 and nums[j] == nums[j-1], continue
      - Initialize left = j+1, right = n-1
      - While left < right:
        * Calculate sum = nums[i] + nums[j] + nums[left] + nums[right]
        * If sum == target:
          - Add [nums[i], nums[j], nums[left], nums[right]] to result
          - Skip duplicates for left: while left < right and nums[left] == nums[left+1], left++
          - Skip duplicates for right: while left < right and nums[right] == nums[right-1], right--
          - Move both pointers: left++, right--
        * Else if sum < target:
          - left++ (need larger sum)
        * Else:
          - right-- (need smaller sum)
5. Return result

Visual Example:
---------------
nums = [1,0,-1,0,-2,2], target = 0
After sorting: [-2,-1,0,0,1,2]

Iteration with i=0 (nums[i]=-2), j=1 (nums[j]=-1):
    [-2, -1, 0, 0, 1, 2]
      i   j  L        R
    
    sum = -2 + -1 + 0 + 2 = -1 < 0
    Move left: L++
    
    [-2, -1, 0, 0, 1, 2]
      i   j     L     R
    
    sum = -2 + -1 + 0 + 2 = -1 < 0
    Move left: L++
    
    [-2, -1, 0, 0, 1, 2]
      i   j        L  R
    
    sum = -2 + -1 + 1 + 2 = 0 ✓
    Found quadruplet: [-2, -1, 1, 2]
    Move both: L++, R--
    
    L >= R, done with this (i,j) pair

Iteration with i=0 (nums[i]=-2), j=2 (nums[j]=0):
    [-2, -1, 0, 0, 1, 2]
      i      j  L     R
    
    sum = -2 + 0 + 0 + 2 = 0 ✓
    Found quadruplet: [-2, 0, 0, 2]
    ...continue...

And so on for all combinations.

Key Insights for Avoiding Duplicates:
--------------------------------------
You must skip duplicates at ALL FOUR levels:

1. Skip duplicate i values:
   if i > 0 and nums[i] == nums[i-1]: continue

2. Skip duplicate j values:
   if j > i+1 and nums[j] == nums[j-1]: continue

3. Skip duplicate left values (after finding a match):
   while left < right and nums[left] == nums[left+1]: left++

4. Skip duplicate right values (after finding a match):
   while left < right and nums[right] == nums[right-1]: right--

Why after sorting?
------------------
Sorting allows us to:
1. Use two-pointer technique (move based on sum comparison)
2. Easily skip duplicates (they'll be adjacent)
3. Early termination (if smallest possible sum > target, break)

Optimization Opportunities:
---------------------------
1. Early break: If nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target, break
   (smallest possible sum with current i is already too large)

2. Early continue: If nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target, continue
   (largest possible sum with current i is still too small)

3. Similar optimizations for j loop

Visual Duplicate Handling:
--------------------------
Consider: nums = [-2,-1,-1,0,0,0,2,2], target = 0

After sorting, we have:
    [-2, -1, -1, 0, 0, 0, 2, 2]

Without duplicate handling:
    [-2, -1, 0, 2] ✓ (indices 0,1,3,6)
    [-2, -1, 0, 2] ✗ (indices 0,1,3,7) - DUPLICATE!
    [-2, -1, 0, 2] ✗ (indices 0,1,4,6) - DUPLICATE!
    ... many more duplicates ...

With duplicate handling:
    [-2, -1, 0, 2] ✓ (only once!)

Edge Cases to Consider:
-----------------------
1. Array length < 4: return []
2. All elements same: [2,2,2,2,2], target=8 → [[2,2,2,2]]
3. No solution exists: [1,2,3,4], target=100 → []
4. Target is 0: classic case
5. Large positive target
6. Large negative target
7. All negative numbers
8. All positive numbers
9. Mix of positive, negative, and zero
10. Array with many duplicates

Relationship to Other Problems:
-------------------------------
- 2Sum: Use hash map or two pointers (if sorted)
- 3Sum: Sort + fix one element + two pointers
- 4Sum: Sort + fix TWO elements + two pointers
- kSum: Generalized version (can use recursion)

Common Pitfalls:
----------------
1. Forgetting to skip duplicates at any of the four levels
2. Wrong condition for skipping duplicates (e.g., j > 0 instead of j > i+1)
3. Not moving both pointers after finding a match
4. Off-by-one errors in loop boundaries
5. Integer overflow (when nums[i] values are large and target is large)
6. Not handling negative numbers correctly

Follow-up Questions:
--------------------
1. How would you generalize this to kSum? (Use recursion!)
2. What if we needed to return indices instead of values?
3. Can you solve 4Sum without sorting? (Much harder, involves hash maps)
4. What's the time complexity? O(n³) for 4Sum, O(n^(k-1)) for kSum
5. How would you handle integer overflow for very large numbers?

Expected Time Complexity: O(n³)
    - O(n log n) for sorting
    - O(n) for first loop (i)
    - O(n) for second loop (j)
    - O(n) for two-pointer search (left, right)
    - Total: O(n³)

Expected Space Complexity: O(1) or O(n)
    - O(1) if we don't count the output array
    - O(n) for sorting (depending on sort implementation)
    - Output space doesn't count toward space complexity
"""


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Find all unique quadruplets in the array that sum to the target.
    
    Args:
        nums: A list of integers
        target: The target sum
    
    Returns:
        A list of lists, where each inner list contains four integers that sum to target
    
    Example:
        >>> four_sum([1,0,-1,0,-2,2], 0)
        [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        >>> four_sum([2,2,2,2,2], 8)
        [[2,2,2,2]]
    """
    four_sum_list = []
    nums.sort()
    
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left , right = j + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    four_sum_list.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    return four_sum_list

# Test cases
if __name__ == "__main__":
    # Test case 1: Example from problem
    nums1 = [1,0,-1,0,-2,2]
    target1 = 0
    print(f"Test 1: nums = {nums1}, target = {target1}")
    result1 = four_sum(nums1, target1)
    print(f"Output: {result1}")
    print(f"Expected: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]\n")
    
    # Test case 2: All same elements
    nums2 = [2,2,2,2,2]
    target2 = 8
    print(f"Test 2: nums = {nums2}, target = {target2}")
    result2 = four_sum(nums2, target2)
    print(f"Output: {result2}")
    print(f"Expected: [[2,2,2,2]]\n")
    
    # Test case 3: Different target
    nums3 = [1,0,-1,0,-2,2]
    target3 = 1
    print(f"Test 3: nums = {nums3}, target = {target3}")
    result3 = four_sum(nums3, target3)
    print(f"Output: {result3}")
    print(f"Expected: [[-2,0,1,2],[-1,0,0,2]]\n")
    
    # Test case 4: No solution
    nums4 = [1,2,3,4]
    target4 = 100
    print(f"Test 4: nums = {nums4}, target = {target4}")
    result4 = four_sum(nums4, target4)
    print(f"Output: {result4}")
    print(f"Expected: []\n")
    
    # Test case 5: Not enough elements
    nums5 = [1,2,3]
    target5 = 10
    print(f"Test 5: nums = {nums5}, target = {target5}")
    result5 = four_sum(nums5, target5)
    print(f"Output: {result5}")
    print(f"Expected: []\n")
    
    # Test case 6: Empty array
    nums6 = []
    target6 = 0
    print(f"Test 6: nums = {nums6}, target = {target6}")
    result6 = four_sum(nums6, target6)
    print(f"Output: {result6}")
    print(f"Expected: []\n")
    
    # Test case 7: Exactly 4 elements that sum to target
    nums7 = [1,2,3,4]
    target7 = 10
    print(f"Test 7: nums = {nums7}, target = {target7}")
    result7 = four_sum(nums7, target7)
    print(f"Output: {result7}")
    print(f"Expected: [[1,2,3,4]]\n")
    
    # Test case 8: Multiple duplicates
    nums8 = [-2,-1,-1,0,0,0,2,2]
    target8 = 0
    print(f"Test 8: nums = {nums8}, target = {target8}")
    result8 = four_sum(nums8, target8)
    print(f"Output: {result8}")
    print(f"Expected: [[-2,-1,0,2],[-2,0,0,2]]\n")
    
    # Test case 9: All negative
    nums9 = [-5,-4,-3,-2,-1]
    target9 = -14
    print(f"Test 9: nums = {nums9}, target = {target9}")
    result9 = four_sum(nums9, target9)
    print(f"Output: {result9}")
    print(f"Expected: [[-5,-4,-3,-2]]\n")
    
    # Test case 10: All positive
    nums10 = [1,2,3,4,5]
    target10 = 10
    print(f"Test 10: nums = {nums10}, target = {target10}")
    result10 = four_sum(nums10, target10)
    print(f"Output: {result10}")
    print(f"Expected: [[1,2,3,4]]\n")
    
    # Test case 11: Large target
    nums11 = [1,2,3,4,5,6,7,8]
    target11 = 20
    print(f"Test 11: nums = {nums11}, target = {target11}")
    result11 = four_sum(nums11, target11)
    print(f"Output: {result11}")
    print(f"Expected: [[2,4,6,8],[2,5,6,7],[3,4,5,8],[3,4,6,7]]\n")
    
    # Test case 12: Negative target
    nums12 = [-1,-2,-3,-4,-5]
    target12 = -10
    print(f"Test 12: nums = {nums12}, target = {target12}")
    result12 = four_sum(nums12, target12)
    print(f"Output: {result12}")
    print(f"Expected: [[-5,-4,-1,0],[-5,-3,-2,0]] (wait, we don't have 0!)")
    print(f"Expected: [[-5,-4,-1,-0] is wrong]")
    print(f"Expected: [[-5,-3,-2,-0] is wrong]")
    print(f"Correct Expected: [[-4,-3,-2,-1]]\n")
    
    # Test case 13: Mix of pos/neg
    nums13 = [-3,-2,-1,0,1,2,3]
    target13 = 0
    print(f"Test 13: nums = {nums13}, target = {target13}")
    result13 = four_sum(nums13, target13)
    print(f"Output: {result13}")
    print(f"Expected: [[-3,-2,2,3],[-3,-1,1,3],[-3,0,1,2],[-2,-1,1,2],[-2,-1,0,3],[-2,0,0,2],[-1,0,0,1]]\n")
