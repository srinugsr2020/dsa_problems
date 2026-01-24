"""
Sort Colors Problem (Two Pointers / Dutch National Flag)

Problem Statement:
------------------
Given an array 'nums' with n objects colored red, white, or blue, sort them in-place 
so that objects of the same color are adjacent, with the colors in the order red, 
white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, 
respectively.

You must solve this problem without using the library's sort function.

Important Notes:
----------------
1. Only three possible values: 0 (red), 1 (white), 2 (blue)
2. Must sort in-place with O(1) extra space
3. Final order should be: all 0's, then all 1's, then all 2's
4. Cannot use built-in sort functions
5. Must modify the array in-place (no return value)

Constraints:
------------
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

Examples:
---------
Example 1:
    Input: nums = [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]
    Explanation: All reds (0) first, then whites (1), then blues (2)

Example 2:
    Input: nums = [2, 0, 1]
    Output: [0, 1, 2]
    Explanation: One of each color in sorted order

Example 3:
    Input: nums = [0]
    Output: [0]
    Explanation: Single element remains unchanged

Example 4:
    Input: nums = [1]
    Output: [1]
    Explanation: Single element remains unchanged

Example 5:
    Input: nums = [2, 2, 2, 0, 0, 1]
    Output: [0, 0, 1, 2, 2, 2]

Example 6:
    Input: nums = [1, 1, 1, 1]
    Output: [1, 1, 1, 1]
    Explanation: All same color, order unchanged

Visual Transformation:
----------------------
Input:  [2, 0, 2, 1, 1, 0]
         ↓  ↓  ↓  ↓  ↓  ↓
Process: Partition into three sections
         [0, 0] [1, 1] [2, 2]
          reds  whites  blues

Output: [0, 0, 1, 1, 2, 2]

Approach 1: Counting (Two-Pass) - Simple but Not Optimal
---------------------------------------------------------
1. Count occurrences of 0, 1, and 2
2. Overwrite array: first with 0's, then 1's, then 2's

Time: O(n), Space: O(1), Passes: 2
(Not the best solution for follow-up)

Approach 2: Dutch National Flag (One-Pass) - Optimal!
------------------------------------------------------
This is the classic three-way partitioning algorithm invented by Edsger Dijkstra.

Use THREE pointers:
1. **low**: marks the boundary for 0's (next position to place a 0)
2. **mid**: current element being examined
3. **high**: marks the boundary for 2's (next position to place a 2)

Algorithm Steps:
1. Initialize: low = 0, mid = 0, high = n-1
2. While mid <= high:
   - If nums[mid] == 0: 
     → Swap nums[low] and nums[mid]
     → Increment both low and mid
   - If nums[mid] == 1:
     → Leave it in place (it's in the middle section)
     → Increment mid only
   - If nums[mid] == 2:
     → Swap nums[mid] and nums[high]
     → Decrement high only (don't increment mid!)
3. Result: [0's | 1's | 2's]

Why Don't We Increment mid After Swapping with high?
-----------------------------------------------------
When we swap nums[mid] with nums[high], we don't know what value we got from 
nums[high]. It could be 0, 1, or 2, so we need to examine it in the next iteration.

Visual Example:
---------------
nums = [2, 0, 2, 1, 1, 0]
        L        
        M              H
        
Step 1: nums[0]=2 (swap with high)
        [0, 0, 2, 1, 1, 2]
         L        
         M           H
         
Step 2: nums[0]=0 (swap with low, increment both)
        [0, 0, 2, 1, 1, 2]
            L        
            M        H
            
Step 3: nums[1]=0 (swap with low, increment both)
        [0, 0, 2, 1, 1, 2]
               L        
               M     H
               
Step 4: nums[2]=2 (swap with high)
        [0, 0, 1, 1, 2, 2]
               L        
               M  H
               
Step 5: nums[2]=1 (leave it, increment mid)
        [0, 0, 1, 1, 2, 2]
               L        
                  M H
                  
Step 6: nums[3]=1 (leave it, increment mid)
        [0, 0, 1, 1, 2, 2]
               L        
                     MH
                     
Step 7: mid > high, STOP!
Result: [0, 0, 1, 1, 2, 2] ✓

Invariants (What Each Region Contains):
----------------------------------------
Throughout the algorithm, maintain these invariants:
- nums[0...low-1]: All 0's (red section)
- nums[low...mid-1]: All 1's (white section)
- nums[mid...high]: Unknown/unsorted (being processed)
- nums[high+1...n-1]: All 2's (blue section)

Key Insights:
-------------
1. Three pointers divide array into four regions
2. The 'mid' pointer scans through the unknown region
3. When we find a 0, it belongs at the start (swap with low)
4. When we find a 2, it belongs at the end (swap with high)
5. When we find a 1, it's already in the correct region (middle)
6. Single pass through the array!

Edge Cases to Consider:
-----------------------
- Array with all same values (all 0's, all 1's, or all 2's)
- Array already sorted
- Array sorted in reverse order
- Array with only two distinct values
- Single element array
- Two element array

Follow-up Question:
-------------------
Could you come up with a one-pass algorithm using only constant extra space?
(Hint: Use the Dutch National Flag approach above!)

Expected Time Complexity: O(n) - single pass
Expected Space Complexity: O(1) - only using three pointers
"""


def sort_colors(nums: list[int]) -> None:
    """
    Sort an array of 0s, 1s, and 2s in-place.
    
    Args:
        nums: List of integers containing only 0, 1, and 2
    
    Returns:
        None (modifies nums in-place)
    
    Example:
        >>> nums = [2, 0, 2, 1, 1, 0]
        >>> sort_colors(nums)
        >>> nums
        [0, 0, 1, 1, 2, 2]
    """
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    


# Test cases
if __name__ == "__main__":
    # Test case 1: Mixed colors
    nums1 = [2, 0, 2, 1, 1, 0]
    print(f"Test 1: Before = {nums1}")
    sort_colors(nums1)
    print(f"        After  = {nums1}")
    print(f"        Expected: [0, 0, 1, 1, 2, 2]\n")
    
    # Test case 2: One of each
    nums2 = [2, 0, 1]
    print(f"Test 2: Before = {nums2}")
    sort_colors(nums2)
    print(f"        After  = {nums2}")
    print(f"        Expected: [0, 1, 2]\n")
    
    # Test case 3: Single element (red)
    nums3 = [0]
    print(f"Test 3: Before = {nums3}")
    sort_colors(nums3)
    print(f"        After  = {nums3}")
    print(f"        Expected: [0]\n")
    
    # Test case 4: Single element (white)
    nums4 = [1]
    print(f"Test 4: Before = {nums4}")
    sort_colors(nums4)
    print(f"        After  = {nums4}")
    print(f"        Expected: [1]\n")
    
    # Test case 5: Multiple blues first
    nums5 = [2, 2, 2, 0, 0, 1]
    print(f"Test 5: Before = {nums5}")
    sort_colors(nums5)
    print(f"        After  = {nums5}")
    print(f"        Expected: [0, 0, 1, 2, 2, 2]\n")
    
    # Test case 6: All same color
    nums6 = [1, 1, 1, 1]
    print(f"Test 6: Before = {nums6}")
    sort_colors(nums6)
    print(f"        After  = {nums6}")
    print(f"        Expected: [1, 1, 1, 1]\n")
    
    # Test case 7: Already sorted
    nums7 = [0, 0, 1, 1, 2, 2]
    print(f"Test 7: Before = {nums7}")
    sort_colors(nums7)
    print(f"        After  = {nums7}")
    print(f"        Expected: [0, 0, 1, 1, 2, 2]\n")
    
    # Test case 8: Reverse sorted
    nums8 = [2, 2, 1, 1, 0, 0]
    print(f"Test 8: Before = {nums8}")
    sort_colors(nums8)
    print(f"        After  = {nums8}")
    print(f"        Expected: [0, 0, 1, 1, 2, 2]\n")
    
    # Test case 9: Two elements
    nums9 = [1, 0]
    print(f"Test 9: Before = {nums9}")
    sort_colors(nums9)
    print(f"        After  = {nums9}")
    print(f"        Expected: [0, 1]\n")
    
    # Test case 10: All reds
    nums10 = [0, 0, 0, 0]
    print(f"Test 10: Before = {nums10}")
    sort_colors(nums10)
    print(f"         After  = {nums10}")
    print(f"         Expected: [0, 0, 0, 0]\n")
    
    # Test case 11: All blues
    nums11 = [2, 2, 2, 2, 2]
    print(f"Test 11: Before = {nums11}")
    sort_colors(nums11)
    print(f"         After  = {nums11}")
    print(f"         Expected: [2, 2, 2, 2, 2]\n")
    
    # Test case 12: Only reds and blues
    nums12 = [2, 0, 2, 0, 2, 0]
    print(f"Test 12: Before = {nums12}")
    sort_colors(nums12)
    print(f"         After  = {nums12}")
    print(f"         Expected: [0, 0, 0, 2, 2, 2]\n")
    
    # Test case 13: Complex case
    nums13 = [2, 0, 1, 2, 0, 1, 2, 0, 1]
    print(f"Test 13: Before = {nums13}")
    sort_colors(nums13)
    print(f"         After  = {nums13}")
    print(f"         Expected: [0, 0, 0, 1, 1, 1, 2, 2, 2]\n")
    
    # Test case 14: Alternating pattern
    nums14 = [0, 2, 0, 2, 0, 2]
    print(f"Test 14: Before = {nums14}")
    sort_colors(nums14)
    print(f"         After  = {nums14}")
    print(f"         Expected: [0, 0, 0, 2, 2, 2]\n")
