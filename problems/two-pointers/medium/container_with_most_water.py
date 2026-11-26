"""
Container With Most Water Problem (Two Pointers Approach)

Problem Statement:
------------------
You are given an integer array 'height' of length n. There are n vertical lines drawn 
such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

Visual Explanation:
-------------------
If height = [1,8,6,2,5,4,8,3,7], imagine vertical lines at each index:

    |
    |                   |
    |   |               |       |
    |   |   |           |       |
    |   |   |   |       |       |
    |   |   |   | |     |       |
    |   |   |   | | |   |   |   |
    |   |   |   | | | | |   | | |
  +--+--+--+--+--+--+--+--+--+--+
    0  1  2  3  4  5  6  7  8

The container formed by lines at index 1 (height=8) and index 8 (height=7) can hold 
the most water. The area is calculated as:
- Width: 8 - 1 = 7
- Height: min(8, 7) = 7
- Area: 7 * 7 = 49

Important Notes:
----------------
1. The water level is determined by the SHORTER of the two lines
2. Width is the distance between the two lines (difference in indices)
3. Area = width * min(left_height, right_height)
4. You cannot "tilt" the container to hold more water

Constraints:
------------
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Examples:
---------
Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The vertical lines are at indices 1 and 8 with heights 8 and 7.
                 Area = (8-1) * min(8,7) = 7 * 7 = 49

Example 2:
    Input: height = [1,1]
    Output: 1
    Explanation: Only two lines available.
                 Area = (1-0) * min(1,1) = 1 * 1 = 1

Example 3:
    Input: height = [4,3,2,1,4]
    Output: 16
    Explanation: Lines at indices 0 and 4 both have height 4.
                 Area = (4-0) * min(4,4) = 4 * 4 = 16

Example 4:
    Input: height = [1,2,1]
    Output: 2
    Explanation: Lines at indices 0 and 2 or 1 and 2.
                 Best is indices 1 and 2: Area = (2-1) * min(2,1) = 1 * 1 = 1
                 Or indices 0 and 1: Area = (1-0) * min(1,2) = 1 * 1 = 1
                 Actually best is 0 and 2: Area = (2-0) * min(1,1) = 2 * 1 = 2

Example 5:
    Input: height = [2,3,4,5,18,17,6]
    Output: 17
    Explanation: Lines at indices 4 and 5.
                 Area = (5-4) * min(18,17) = 1 * 17 = 17

Hints:
------
1. Start with two pointers: one at the beginning (left) and one at the end (right)
2. Calculate the area formed by these two lines
3. Keep track of the maximum area seen so far
4. The key insight: the width decreases as you move pointers inward, so you need 
   to find taller lines to potentially get a larger area
5. Which pointer should you move? Think about this: if you move the pointer at the 
   taller line, you're guaranteed to get a smaller or equal area (same or shorter 
   height, but definitely smaller width). So move the pointer at the SHORTER line!
6. Continue until the two pointers meet

Why the Greedy Approach Works:
-------------------------------
- You always want to maximize: width * min(height[left], height[right])
- As width decreases when moving pointers inward, you need taller lines
- Moving the shorter line's pointer gives you a chance to find a taller line
- Moving the taller line's pointer cannot improve the result (width decreases and 
  height can only stay same or decrease)

Expected Time Complexity: O(n) - single pass through the array
Expected Space Complexity: O(1) - only using pointers and variables
"""


def max_area(height: list[int]) -> int:
    """
    Find the maximum area of water that can be contained between two vertical lines.
    
    Args:
        height: List of integers representing the height of vertical lines
    
    Returns:
        The maximum area of water that can be contained
    
    Example:
        >>> max_area([1,8,6,2,5,4,8,3,7])
        49
        >>> max_area([1,1])
        1
    """
    left , right = 0, len(height) - 1
    max_area = 0
    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


# Test cases
if __name__ == "__main__":
    # Test case 1: Classic example with multiple peaks
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Test 1: height = {height1}")
    result1 = max_area(height1)
    print(f"Output: {result1}")
    print(f"Expected: 49")
    print(f"Explanation: Lines at indices 1 and 8 -> (8-1) * min(8,7) = 49\n")
    
    # Test case 2: Minimum input
    height2 = [1, 1]
    print(f"Test 2: height = {height2}")
    result2 = max_area(height2)
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print(f"Explanation: Only two lines -> (1-0) * min(1,1) = 1\n")
    
    # Test case 3: Equal heights at extremes
    height3 = [4, 3, 2, 1, 4]
    print(f"Test 3: height = {height3}")
    result3 = max_area(height3)
    print(f"Output: {result3}")
    print(f"Expected: 16")
    print(f"Explanation: Lines at indices 0 and 4 -> (4-0) * min(4,4) = 16\n")
    
    # Test case 4: Small array
    height4 = [1, 2, 1]
    print(f"Test 4: height = {height4}")
    result4 = max_area(height4)
    print(f"Output: {result4}")
    print(f"Expected: 2")
    print(f"Explanation: Lines at indices 0 and 2 -> (2-0) * min(1,1) = 2\n")
    
    # Test case 5: High peaks close together
    height5 = [2, 3, 4, 5, 18, 17, 6]
    print(f"Test 5: height = {height5}")
    result5 = max_area(height5)
    print(f"Output: {result5}")
    print(f"Expected: 17")
    print(f"Explanation: Lines at indices 4 and 5 -> (5-4) * min(18,17) = 17\n")
    
    # Test case 6: Ascending then descending
    height6 = [1, 3, 5, 4, 2]
    print(f"Test 6: height = {height6}")
    result6 = max_area(height6)
    print(f"Output: {result6}")
    print(f"Expected: 6")
    print(f"Explanation: Lines at indices 1 and 4 -> (4-1) * min(3,2) = 6\n")
    
    # Test case 7: Large width with lower heights vs smaller width with higher heights
    height7 = [2, 2, 2, 2, 2, 2, 2, 100, 100, 2]
    print(f"Test 7: height = {height7}")
    result7 = max_area(height7)
    print(f"Output: {result7}")
    print(f"Expected: 100")
    print(f"Explanation: Lines at indices 7 and 8 -> (8-7) * min(100,100) = 100\n")
    
    # Test case 8: All same height
    height8 = [5, 5, 5, 5, 5]
    print(f"Test 8: height = {height8}")
    result8 = max_area(height8)
    print(f"Output: {result8}")
    print(f"Expected: 20")
    print(f"Explanation: Lines at indices 0 and 4 -> (4-0) * min(5,5) = 20\n")
