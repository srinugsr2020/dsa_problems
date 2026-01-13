"""
Move Zeroes Problem (Two Pointers Approach)

Problem Statement:
------------------
Given an integer array 'nums', move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.

Note: You must do this in-place without making a copy of the array.

Important Notes:
----------------
1. Modify the array in-place (O(1) extra space)
2. Maintain the relative order of non-zero elements
3. All zeros should be at the end
4. Minimize the total number of operations

Constraints:
------------
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Examples:
---------
Example 1:
    Input: nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]
    Explanation: All non-zero elements (1, 3, 12) moved to the front in order,
                 zeros moved to the end.

Example 2:
    Input: nums = [0]
    Output: [0]
    Explanation: Single zero remains in place.

Example 3:
    Input: nums = [1, 2, 3]
    Output: [1, 2, 3]
    Explanation: No zeros to move, array unchanged.

Example 4:
    Input: nums = [0, 0, 1]
    Output: [1, 0, 0]
    Explanation: Non-zero element (1) moved to front, zeros to end.

Example 5:
    Input: nums = [2, 1]
    Output: [2, 1]
    Explanation: No zeros, array unchanged.

Example 6:
    Input: nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
    Explanation: Non-zeros (4, 2, 4, 3, 5, 1) maintain order, zeros at end.

Visual Transformation:
----------------------
Input:  [0, 1, 0, 3, 12]
         ↓  ↓  ↓  ↓  ↓
Step 1: [1, 1, 0, 3, 12]  (found 1, move to position 0)
Step 2: [1, 3, 0, 3, 12]  (found 3, move to position 1)
Step 3: [1, 3, 12, 3, 12] (found 12, move to position 2)
Step 4: [1, 3, 12, 0, 0]  (fill remaining with zeros)

Output: [1, 3, 12, 0, 0]

Approach Hints:
---------------
There are multiple approaches, but the two-pointer approach is most efficient:

Approach 1: Two Pointers (Optimal)
1. Use a "slow" pointer to track where the next non-zero should be placed
2. Use a "fast" pointer to scan through the array
3. When fast pointer finds a non-zero, swap it with the slow pointer position
4. Move slow pointer forward after each swap
5. This ensures non-zeros are moved to the front in order

Approach 2: Two Pass (Alternative)
1. First pass: Move all non-zeros to the front
2. Second pass: Fill remaining positions with zeros
(Less efficient in terms of operations)

Key Insights:
-------------
1. You need to maintain the ORDER of non-zero elements
2. In-place means O(1) extra space - no extra array
3. Using swap operation helps maintain order and move zeros simultaneously
4. The slow pointer marks the "write" position for non-zero elements

Algorithm Steps (Two Pointers):
--------------------------------
1. Initialize slow pointer at 0 (marks position for next non-zero)
2. Iterate through array with fast pointer
3. When nums[fast] is non-zero:
   - Swap nums[slow] with nums[fast]
   - Increment slow pointer
4. Continue until fast pointer reaches the end
5. All zeros will naturally end up at the end

Why Swap Works:
---------------
- When both pointers point to non-zero: swapping doesn't change anything, just moves slow forward
- When slow points to zero and fast points to non-zero: swap moves non-zero to front
- When fast points to zero: no swap, fast just moves forward
- This automatically groups all zeros at the end!

Edge Cases to Consider:
-----------------------
- Array with no zeros
- Array with all zeros
- Array with single element
- Array with zeros at the beginning
- Array with zeros at the end
- Array with alternating zeros and non-zeros

Follow-up Questions:
--------------------
1. Could you minimize the total number of operations?
   (Think about when to perform swaps - only when necessary)
2. What if you needed to move zeros to the beginning instead?
3. What if you needed to move a specific value (not just zero)?

Expected Time Complexity: O(n) where n is the length of the array
Expected Space Complexity: O(1) - in-place modification
"""


def move_zeroes(nums: list[int]) -> None:
    """
    Move all zeros to the end of the array while maintaining the relative order
    of non-zero elements. Modifies the array in-place.
    
    Args:
        nums: List of integers to modify in-place
    
    Returns:
        None (modifies nums in-place)
    
    Example:
        >>> nums = [0, 1, 0, 3, 12]
        >>> move_zeroes(nums)
        >>> nums
        [1, 3, 12, 0, 0]
    """
    i, j = 0, 1
    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        elif nums[i] == 0 and nums[j] == 0:
            j += 1
        else:
            i += 1
            j += 1


# Test cases
if __name__ == "__main__":
    # Test case 1: Mixed zeros and non-zeros
    nums1 = [0, 1, 0, 3, 12]
    print(f"Test 1: Before = {nums1}")
    move_zeroes(nums1)
    print(f"        After  = {nums1}")
    print(f"        Expected: [1, 3, 12, 0, 0]\n")
    
    # Test case 2: Single zero
    nums2 = [0]
    print(f"Test 2: Before = {nums2}")
    move_zeroes(nums2)
    print(f"        After  = {nums2}")
    print(f"        Expected: [0]\n")
    
    # Test case 3: No zeros
    nums3 = [1, 2, 3]
    print(f"Test 3: Before = {nums3}")
    move_zeroes(nums3)
    print(f"        After  = {nums3}")
    print(f"        Expected: [1, 2, 3]\n")
    
    # Test case 4: Zeros at beginning
    nums4 = [0, 0, 1]
    print(f"Test 4: Before = {nums4}")
    move_zeroes(nums4)
    print(f"        After  = {nums4}")
    print(f"        Expected: [1, 0, 0]\n")
    
    # Test case 5: No zeros at all
    nums5 = [2, 1]
    print(f"Test 5: Before = {nums5}")
    move_zeroes(nums5)
    print(f"        After  = {nums5}")
    print(f"        Expected: [2, 1]\n")
    
    # Test case 6: Complex case with multiple zeros
    nums6 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    print(f"Test 6: Before = {nums6}")
    move_zeroes(nums6)
    print(f"        After  = {nums6}")
    print(f"        Expected: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]\n")
    
    # Test case 7: All zeros
    nums7 = [0, 0, 0, 0]
    print(f"Test 7: Before = {nums7}")
    move_zeroes(nums7)
    print(f"        After  = {nums7}")
    print(f"        Expected: [0, 0, 0, 0]\n")
    
    # Test case 8: Single non-zero
    nums8 = [1]
    print(f"Test 8: Before = {nums8}")
    move_zeroes(nums8)
    print(f"        After  = {nums8}")
    print(f"        Expected: [1]\n")
    
    # Test case 9: Alternating zeros and non-zeros
    nums9 = [0, 1, 0, 2, 0, 3]
    print(f"Test 9: Before = {nums9}")
    move_zeroes(nums9)
    print(f"        After  = {nums9}")
    print(f"        Expected: [1, 2, 3, 0, 0, 0]\n")
    
    # Test case 10: Zeros at the end already
    nums10 = [1, 2, 3, 0, 0]
    print(f"Test 10: Before = {nums10}")
    move_zeroes(nums10)
    print(f"         After  = {nums10}")
    print(f"         Expected: [1, 2, 3, 0, 0]\n")
    
    # Test case 11: Negative numbers with zeros
    nums11 = [0, -1, 0, -2, 3]
    print(f"Test 11: Before = {nums11}")
    move_zeroes(nums11)
    print(f"         After  = {nums11}")
    print(f"         Expected: [-1, -2, 3, 0, 0]\n")
    
    # Test case 12: Large numbers
    nums12 = [1, 0, 2]
    print(f"Test 12: Before = {nums12}")
    move_zeroes(nums12)
    print(f"         After  = {nums12}")
    print(f"         Expected: [1000000, -1000000, 0, 0, 0]\n")
