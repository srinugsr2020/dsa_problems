"""
Three Sum Problem (Two Pointers Approach)

Problem Statement:
------------------
Given an integer array 'nums', return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Important Notes:
----------------
1. Each triplet should contain three distinct elements from different indices
2. The triplets themselves should be unique (no duplicate triplets in result)
3. The order of triplets in the result doesn't matter
4. The order of elements within each triplet doesn't matter
5. You cannot use the same element twice in a triplet

Constraints:
------------
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Examples:
---------
Example 1:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    Explanation: 
        - nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
        - nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
        - nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
        Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0, 1, 1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0, 0, 0]
    Output: [[0, 0, 0]]
    Explanation: The only possible triplet sums up to 0.

Example 4:
    Input: nums = [-2, 0, 1, 1, 2]
    Output: [[-2, 0, 2], [-2, 1, 1]]
    Explanation: Two unique triplets sum to 0.

Example 5:
    Input: nums = [-1, 0, 1]
    Output: [[-1, 0, 1]]
    Explanation: Single triplet sums to 0.

Visual Explanation:
-------------------
nums = [-1, 0, 1, 2, -1, -4]

Step 1: Sort the array
sorted = [-4, -1, -1, 0, 1, 2]

Step 2: Fix first element, use two pointers for remaining
Fix i=0 (value=-4): Look for two numbers that sum to 4
    [-4, -1, -1, 0, 1, 2]
      ↑   L           R
    -1 + 2 = 1 (< 4, move L right)
    ... no valid pairs

Fix i=1 (value=-1): Look for two numbers that sum to 1
    [-4, -1, -1, 0, 1, 2]
          ↑   L      R
    -1 + 2 = 1 ✓ Found: [-1, -1, 2]
    
    Skip duplicate at i=2 (also -1)

Fix i=3 (value=0): Look for two numbers that sum to 0
    [-4, -1, -1, 0, 1, 2]
                 ↑ L  R
    1 + 2 = 3 (> 0, move R left)
    [-4, -1, -1, 0, 1, 2]
                 ↑ L R
    1 + 1 = 2 (> 0, move R left)
    ... Found: [0, -1, 1] = [-1, 0, 1]

Result: [[-1, -1, 2], [-1, 0, 1]]

Approach: Sort + Two Pointers
------------------------------
This problem combines sorting with the two-pointers technique.

Algorithm Steps:
1. Sort the array in ascending order
2. Iterate through the array with index i (this is the first element)
3. For each i, use two pointers (left and right) to find pairs that sum to -nums[i]
   - left starts at i+1
   - right starts at the end of array
4. Calculate sum = nums[i] + nums[left] + nums[right]
   - If sum == 0: Found a triplet! Add to result
   - If sum < 0: Move left pointer right (need larger sum)
   - If sum > 0: Move right pointer left (need smaller sum)
5. Skip duplicate values to avoid duplicate triplets
6. Return all unique triplets

Key Insights:
-------------
1. Sorting helps in two ways:
   - Enables two-pointer technique
   - Makes it easier to skip duplicates
2. Fix one element, then it becomes a Two Sum problem for the rest
3. For each fixed element nums[i], find two numbers that sum to -nums[i]
4. Time complexity: O(n²) because we iterate once (O(n)) and for each 
   iteration, we do a two-pointer search (O(n))

Handling Duplicates:
--------------------
Critical for avoiding duplicate triplets!

1. Skip duplicate values for the first element (i):
   if i > 0 and nums[i] == nums[i-1]:
       continue

2. Skip duplicate values for left pointer:
   while left < right and nums[left] == nums[left+1]:
       left += 1

3. Skip duplicate values for right pointer:
   while left < right and nums[right] == nums[right-1]:
       right -= 1

Why Sort First?
---------------
- Allows two-pointer technique to work (move based on sum comparison)
- Makes duplicate detection easy (adjacent elements)
- Doesn't lose information (we return values, not indices)

Edge Cases to Consider:
-----------------------
- Array with fewer than 3 elements (impossible per constraints)
- Array with all same values (e.g., [0,0,0] or [1,1,1])
- Array with no valid triplets
- Array with many duplicate values
- Array with all positive or all negative numbers

Example Walkthrough:
--------------------
nums = [-1, 0, 1, 2, -1, -4]

After sorting: [-4, -1, -1, 0, 1, 2]

i=0, nums[i]=-4, target=4:
    left=1, right=5: -1+2=1 < 4, left++
    left=2, right=5: -1+2=1 < 4, left++
    left=3, right=5: 0+2=2 < 4, left++
    left=4, right=5: 1+2=3 < 4, left++
    left=5, right=5: stop

i=1, nums[i]=-1, target=1:
    left=2, right=5: -1+2=1 == 1 ✓ Add [-1,-1,2]
    Move both: left=3, right=4
    left=3, right=4: 0+1=1 == 1 ✓ Add [-1,0,1]
    Move both: left=4, right=3: stop

i=2, nums[i]=-1: Skip (duplicate of previous)

i=3, nums[i]=0: Already found in i=1
    ...

Result: [[-1,-1,2], [-1,0,1]]

Optimization Tips:
------------------
1. If nums[i] > 0, break early (sorted array, all remaining are positive)
2. If nums[i] + nums[i+1] + nums[i+2] > 0, skip to next i
3. If nums[i] + nums[n-2] + nums[n-1] < 0, skip to next i

Expected Time Complexity: O(n²) where n is the length of the array
Expected Space Complexity: O(1) or O(n) depending on sorting algorithm (ignore output array)
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in the array that sum to zero.
    
    Args:
        nums: List of integers
    
    Returns:
        List of lists, where each inner list is a triplet that sums to 0
    
    Example:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> three_sum([0, 1, 1])
        []
        >>> three_sum([0, 0, 0])
        [[0, 0, 0]]
    """
    tripplets = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        first_ele = nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right] + first_ele
            if current_sum == 0:
                tripplets.append([first_ele, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return tripplets
                

                                 



# Test cases
if __name__ == "__main__":
    # Test case 1: Classic example with duplicates
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Test 1: nums = {nums1}")
    result1 = three_sum(nums1)
    print(f"Output: {result1}")
    print(f"Expected: [[-1, -1, 2], [-1, 0, 1]] (order may vary)\n")
    
    # Test case 2: No valid triplets
    nums2 = [0, 1, 1]
    print(f"Test 2: nums = {nums2}")
    result2 = three_sum(nums2)
    print(f"Output: {result2}")
    print(f"Expected: []\n")
    
    # Test case 3: All zeros
    nums3 = [0, 0, 0]
    print(f"Test 3: nums = {nums3}")
    result3 = three_sum(nums3)
    print(f"Output: {result3}")
    print(f"Expected: [[0, 0, 0]]\n")
    
    # Test case 4: Multiple valid triplets
    nums4 = [-2, 0, 1, 1, 2]
    print(f"Test 4: nums = {nums4}")
    result4 = three_sum(nums4)
    print(f"Output: {result4}")
    print(f"Expected: [[-2, 0, 2], [-2, 1, 1]] (order may vary)\n")
    
    # Test case 5: Single triplet
    nums5 = [-1, 0, 1]
    print(f"Test 5: nums = {nums5}")
    result5 = three_sum(nums5)
    print(f"Output: {result5}")
    print(f"Expected: [[-1, 0, 1]]\n")
    
    # Test case 6: Many duplicates
    nums6 = [-1, -1, -1, 0, 1, 1, 1]
    print(f"Test 6: nums = {nums6}")
    result6 = three_sum(nums6)
    print(f"Output: {result6}")
    print(f"Expected: [[-1, 0, 1]] (only one unique triplet)\n")
    
    # Test case 7: All positive numbers
    nums7 = [1, 2, 3, 4]
    print(f"Test 7: nums = {nums7}")
    result7 = three_sum(nums7)
    print(f"Output: {result7}")
    print(f"Expected: [] (no triplet can sum to 0)\n")
    
    # Test case 8: All negative numbers
    nums8 = [-1, -2, -3, -4]
    print(f"Test 8: nums = {nums8}")
    result8 = three_sum(nums8)
    print(f"Output: {result8}")
    print(f"Expected: [] (no triplet can sum to 0)\n")
    
    # Test case 9: Larger example
    nums9 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    print(f"Test 9: nums = {nums9}")
    result9 = three_sum(nums9)
    print(f"Output: {result9}")
    print(f"Expected: Multiple triplets like [[-4,-2,6], [-4,0,4], [-4,1,3], ...]\n")
    
    # Test case 10: Minimum size
    nums10 = [0, 0, 0, 0]
    print(f"Test 10: nums = {nums10}")
    result10 = three_sum(nums10)
    print(f"Output: {result10}")
    print(f"Expected: [[0, 0, 0]]\n")
    
    # Test case 11: Mix of positive, negative, and zero
    nums11 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    print(f"Test 11: nums = {nums11}")
    result11 = three_sum(nums11)
    print(f"Output: {result11}")
    print(f"Expected: Many triplets like [[-5,1,4], [-5,2,3], [-4,0,4], ...]\n")
    
    # Test case 12: Two zeros
    nums12 = [-1, 0, 0, 1]
    print(f"Test 12: nums = {nums12}")
    result12 = three_sum(nums12)
    print(f"Output: {result12}")
    print(f"Expected: [[-1, 0, 1]]\n")
