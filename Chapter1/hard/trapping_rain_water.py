"""
Trapping Rain Water Problem (Two Pointers / Dynamic Programming)

Problem Statement:
------------------
Given n non-negative integers representing an elevation map where the width of each 
bar is 1, compute how much water it can trap after raining.

Constraints:
------------
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

Examples:
---------
Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: 
        Visual representation:
        
             █
         █   ██ █
         █ █ ██████ █
         012345678911
                   01
        
        The elevation map (above) is represented by [0,1,0,2,1,0,1,3,2,1,2,1].
        In this case, 6 units of rain water (blue section) are being trapped.
        
        Water trapped at each position:
        Index 0: 0 (edge, no water)
        Index 1: 0 (no higher bar on left)
        Index 2: 1 (trapped between bars at index 1 and 3)
        Index 3: 0 (this is a peak)
        Index 4: 1 (trapped between bars at index 3 and 7)
        Index 5: 2 (trapped between bars at index 3 and 7)
        Index 6: 1 (trapped between bars at index 3 and 7)
        Index 7: 0 (this is a peak)
        Index 8: 0 (no higher bar on right)
        Index 9: 1 (trapped between bars at index 7 and 10)
        Index 10: 0 (this is a peak)
        Index 11: 0 (edge, no water)
        Total: 0+0+1+0+1+2+1+0+0+1+0+0 = 6

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9
    Explanation:
        Visual:
        █    █
        █  █ █
        █  ███
        █ ████
        ██████
        456789
        
        Water trapped:
        Index 0: 0 (edge)
        Index 1: 2 (4 - 2 = 2, bounded by 4 and 5)
        Index 2: 4 (4 - 0 = 4, bounded by 4 and 5)
        Index 3: 1 (4 - 3 = 1, bounded by 4 and 5)
        Index 4: 2 (4 - 2 = 2, bounded by 4 and 5)
        Index 5: 0 (edge)
        Total: 0+2+4+1+2+0 = 9

Example 3:
    Input: height = [4,2,3]
    Output: 1
    Explanation:
        █  
        █ █
        ███
        423
        
        Only 1 unit of water trapped at index 1 (min(4,3) - 2 = 1)

Example 4:
    Input: height = [3,0,2,0,4]
    Output: 7
    Explanation:
        Water trapped: 0 + 3 + 1 + 3 + 0 = 7

Example 5:
    Input: height = [5,4,1,2]
    Output: 1
    Explanation:
        Only 1 unit at index 2 (min(4,2) - 1 = 1)

Understanding the Problem:
--------------------------
The key insight is that water trapped at any position depends on:
1. The maximum height to its LEFT
2. The maximum height to its RIGHT
3. Its own height

Water at position i = min(max_left, max_right) - height[i]
(but only if this value is positive, otherwise 0)

Why?
- Water can only be trapped if there are higher bars on BOTH sides
- The water level is limited by the SHORTER of the two boundary walls
- We subtract the current bar height to get the actual water above it

Visual Understanding:
---------------------
Think of it like this:

     █
     █  █
    ████████
    
At the middle position (height=0):
- Left max = 4 (the tall bar on left)
- Right max = 3 (the tall bar on right)
- Water level = min(4, 3) = 3
- Water trapped = 3 - 0 = 3 units

At the position with height=2:
- Left max = 4
- Right max = 3
- Water level = min(4, 3) = 3
- Water trapped = 3 - 2 = 1 unit

Approach 1: Brute Force (Not Optimal)
--------------------------------------
For each position:
1. Find the maximum height to its left
2. Find the maximum height to its right
3. Calculate water = min(left_max, right_max) - height[i]

Time: O(n²) - for each position, we scan left and right
Space: O(1)

Approach 2: Dynamic Programming (Better)
-----------------------------------------
Precompute the maximum heights:
1. Create left_max array: left_max[i] = max height from 0 to i
2. Create right_max array: right_max[i] = max height from i to end
3. For each position: water[i] = min(left_max[i], right_max[i]) - height[i]

Time: O(n) - three passes through array
Space: O(n) - two extra arrays

Algorithm Steps for DP:
-----------------------
1. Create left_max array of size n:
   - left_max[0] = height[0]
   - For i from 1 to n-1: left_max[i] = max(left_max[i-1], height[i])

2. Create right_max array of size n:
   - right_max[n-1] = height[n-1]
   - For i from n-2 to 0: right_max[i] = max(right_max[i+1], height[i])

3. Calculate total water:
   - total = 0
   - For each i: total += max(0, min(left_max[i], right_max[i]) - height[i])

Approach 3: Two Pointers (Optimal!)
------------------------------------
Key insight: We don't need to know the exact max on both sides. We only need 
to know which side has the smaller max (because that's the limiting factor).

Use two pointers (left and right) and track:
- left_max: maximum height seen from left so far
- right_max: maximum height seen from right so far

Algorithm:
1. Initialize left=0, right=n-1, left_max=0, right_max=0, total=0
2. While left < right:
   a. If height[left] < height[right]:
      - If height[left] >= left_max: update left_max
      - Else: add (left_max - height[left]) to total
      - Move left pointer right (left++)
   b. Else:
      - If height[right] >= right_max: update right_max
      - Else: add (right_max - height[right]) to total
      - Move right pointer left (right--)
3. Return total

Why This Works:
---------------
- If height[left] < height[right], we know that even if there's a taller bar 
  on the right, the water level at 'left' is determined by left_max
  (because we already know right side has at least height[right])
- Similarly for the right side
- We process from both ends toward middle, always processing the side with 
  the smaller current height

Visual Example with Two Pointers:
----------------------------------
height = [0,1,0,2,1,0,1,3,2,1,2,1]
          L                     R

Step 1: height[L]=0 < height[R]=1
    left_max = 0, water = 0, L++
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
            L                   R

Step 2: height[L]=1 == height[R]=1
    Process right: right_max = 1, water = 0, R--
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
            L                 R

Step 3: height[L]=1 < height[R]=2
    left_max = 1, water = 0, L++
    
... and so on

Time: O(n) - single pass
Space: O(1) - only using a few variables

Key Insights:
-------------
1. Water at any position is limited by the minimum of max heights on both sides
2. No water can be trapped at the edges (no boundary on one side)
3. No water is trapped at peaks (local maxima)
4. Two pointers approach processes the smaller height side, guaranteeing 
   we always know enough about boundaries
5. If current height is less than the max on its side, water is trapped

Edge Cases to Consider:
-----------------------
1. All heights equal: [2,2,2,2] → 0 (no valleys)
2. Ascending order: [1,2,3,4] → 0 (no water trapped)
3. Descending order: [4,3,2,1] → 0 (no water trapped)
4. Single element: [5] → 0
5. Two elements: [3,2] → 0 (need at least 3 for water)
6. Valley in middle: [3,0,3] → 3
7. Multiple peaks and valleys: complex but follows same rules
8. Heights with zeros: [3,0,0,3] → 6 (zeros act as deep valleys)

Common Pitfalls:
----------------
1. Forgetting that edges can't trap water
2. Not handling the case when current height is greater than or equal to max
3. Off-by-one errors with array indices
4. In two-pointer approach, confusing when to move which pointer
5. Forgetting to check if calculated water is negative (though with correct 
   logic, it shouldn't be)

Follow-up Questions:
--------------------
1. What if the bars have different widths? (Modify to account for width)
2. Can you solve it recursively? (Possible but not efficient)
3. What if we want to return the water trapped at each position? (Use DP approach)
4. How would you handle 2D version (water trapped in a matrix)? (More complex!)

Expected Time Complexity: O(n) using two pointers or DP
Expected Space Complexity: O(1) using two pointers, O(n) using DP
"""


def trap(height: list[int]) -> int:
    """
    Calculate how much rainwater can be trapped given an elevation map.
    
    Args:
        height: A list of non-negative integers representing the elevation map
    
    Returns:
        The total amount of water that can be trapped
    
    Example:
        >>> trap([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        >>> trap([4,2,0,3,2,5])
        9
        >>> trap([4,2,3])
        1
    """
    left_max_array = [0] * len(height)
    right_max_array = [0] * len(height)
    for i in range(1, len(height)):
        left_max_array[i] = max(left_max_array[i - 1], height[i - 1])
    for i in range(len(height) -2, -1, -1):
        right_max_array[i] = max(right_max_array[i + 1], height[i + 1])
    total_water = 0
    for i in range(len(height)):
        water_level = min(left_max_array[i], right_max_array[i])
        if water_level > height[i]:
            total_water += water_level - height[i]
    return total_water

def trap_two_pointer(height: list[int]) -> int:
    """
    Calculate how much rainwater can be trapped given an elevation map.
    
    Args:
        height: A list of non-negative integers representing the elevation map
    
    Returns:
        The total amount of water that can be trapped
    
    Example:
        >>> trap([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        >>> trap([4,2,0,3,2,5])
        9
        >>> trap([4,2,3])
        1
    """
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]
            right -= 1

    return total_water

# Test cases
if __name__ == "__main__":
    # Test case 1: Example from problem description
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Test 1: height = {height1}")
    result1 = trap(height1)
    print(f"Output: {result1}")
    print(f"Expected: 6\n")
    
    # Test case 2: Larger boundaries
    height2 = [4,2,0,3,2,5]
    print(f"Test 2: height = {height2}")
    result2 = trap(height2)
    print(f"Output: {result2}")
    print(f"Expected: 9\n")
    
    # Test case 3: Simple case
    height3 = [4,2,3]
    print(f"Test 3: height = {height3}")
    result3 = trap(height3)
    print(f"Output: {result3}")
    print(f"Expected: 1\n")
    
    # Test case 4: Multiple valleys
    height4 = [3,0,2,0,4]
    print(f"Test 4: height = {height4}")
    result4 = trap(height4)
    print(f"Output: {result4}")
    print(f"Expected: 7\n")
    
    # Test case 5: Descending then ascending
    height5 = [5,4,1,2]
    print(f"Test 5: height = {height5}")
    result5 = trap(height5)
    print(f"Output: {result5}")
    print(f"Expected: 1\n")
    
    # Test case 6: No water trapped (ascending)
    height6 = [1,2,3,4,5]
    print(f"Test 6: height = {height6}")
    result6 = trap(height6)
    print(f"Output: {result6}")
    print(f"Expected: 0\n")
    
    # Test case 7: No water trapped (descending)
    height7 = [5,4,3,2,1]
    print(f"Test 7: height = {height7}")
    result7 = trap(height7)
    print(f"Output: {result7}")
    print(f"Expected: 0\n")
    
    # Test case 8: All same height
    height8 = [3,3,3,3]
    print(f"Test 8: height = {height8}")
    result8 = trap(height8)
    print(f"Output: {result8}")
    print(f"Expected: 0\n")
    
    # Test case 9: Simple valley
    height9 = [3,0,3]
    print(f"Test 9: height = {height9}")
    result9 = trap(height9)
    print(f"Output: {result9}")
    print(f"Expected: 3\n")
    
    # Test case 10: Deep valley with zeros
    height10 = [3,0,0,3]
    print(f"Test 10: height = {height10}")
    result10 = trap(height10)
    print(f"Output: {result10}")
    print(f"Expected: 6\n")
    
    # Test case 11: Single element
    height11 = [5]
    print(f"Test 11: height = {height11}")
    result11 = trap(height11)
    print(f"Output: {result11}")
    print(f"Expected: 0\n")
    
    # Test case 12: Two elements
    height12 = [3,2]
    print(f"Test 12: height = {height12}")
    result12 = trap(height12)
    print(f"Output: {result12}")
    print(f"Expected: 0\n")
    
    # Test case 13: Complex pattern
    height13 = [5,2,1,2,1,5]
    print(f"Test 13: height = {height13}")
    result13 = trap(height13)
    print(f"Output: {result13}")
    print(f"Expected: 14\n")
    
    # Test case 14: Mountain shape
    height14 = [1,2,3,4,3,2,1]
    print(f"Test 14: height = {height14}")
    result14 = trap(height14)
    print(f"Output: {result14}")
    print(f"Expected: 0\n")
    
    # Test case 15: Valley shape
    height15 = [4,3,2,1,2,3,4]
    print(f"Test 15: height = {height15}")
    result15 = trap(height15)
    print(f"Output: {result15}")
    print(f"Expected: 9\n")
