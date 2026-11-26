"""
Squares of a Sorted Array Problem (Two Pointers Approach)

Problem Statement:
------------------
Given an integer array 'nums' sorted in non-decreasing order, return an array of the 
squares of each number sorted in non-decreasing order.

Important Notes:
----------------
1. Input array is already sorted in ascending order
2. Array may contain negative numbers, zero, and positive numbers
3. Output must also be sorted in ascending order
4. You need to return a NEW array (not in-place modification)

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order

Examples:
---------
Example 1:
    Input: nums = [-4, -1, 0, 3, 10]
    Output: [0, 1, 9, 16, 100]
    Explanation: 
        Squares: [16, 1, 0, 9, 100]
        Sorted:  [0, 1, 9, 16, 100]

Example 2:
    Input: nums = [-7, -3, 2, 3, 11]
    Output: [4, 9, 9, 49, 121]
    Explanation:
        Squares: [49, 9, 4, 9, 121]
        Sorted:  [4, 9, 9, 49, 121]

Example 3:
    Input: nums = [-5, -3, -2, -1]
    Output: [1, 4, 9, 25]
    Explanation: All negatives - squares in reverse order

Example 4:
    Input: nums = [1, 2, 3, 4, 5]
    Output: [1, 4, 9, 16, 25]
    Explanation: All positives - squares in same order

Example 5:
    Input: nums = [0, 1, 2]
    Output: [0, 1, 4]
    Explanation: Starting with zero

Example 6:
    Input: nums = [-1, 0, 1]
    Output: [0, 1, 1]
    Explanation: Symmetrical around zero

The Challenge:
--------------
The tricky part is that negative numbers become positive when squared!

Example:
    Input:  [-4, -1, 0, 3, 10]
    Squares: [16,  1, 0, 9, 100]
                ↑   ↑        ↑
              large small  large

Notice: The LARGEST squared values are at the ENDS (extreme negatives or large positives)!

Approach 1: Brute Force (Not Optimal)
--------------------------------------
1. Square all elements
2. Sort the result

Time: O(n log n) due to sorting
Space: O(n) for the result array
This works but we can do better!

Approach 2: Two Pointers (Optimal!)
------------------------------------
Key insight: Since input is sorted, the largest absolute values (which become 
the largest squares) are at the ENDS of the array!

Strategy:
1. Use two pointers: left at start, right at end
2. Compare absolute values (or squares) at both pointers
3. The larger square goes at the END of result array
4. Fill result array from right to left (largest to smallest)
5. Move the pointer that had the larger absolute value

Why This Works:
---------------
- Input is sorted: [...negative... | 0 | ...positive...]
- Largest absolute values are at the extremes
- We can build the result by picking the larger square from either end
- Fill from back to front (largest squares first)

Algorithm Steps:
----------------
1. Create result array of same size
2. Initialize: left = 0, right = n-1, position = n-1
3. While left <= right:
   a. Calculate left_square = nums[left]²
   b. Calculate right_square = nums[right]²
   c. If left_square > right_square:
      - Place left_square at result[position]
      - Move left pointer right (left++)
   d. Else:
      - Place right_square at result[position]
      - Move right pointer left (right--)
   e. Move position left (position--)
4. Return result

Visual Example:
---------------
nums = [-4, -1, 0, 3, 10]
        L              R    position = 4

Iteration 1: |-4| = 4, |10| = 10 → 10² = 100 is larger
    result = [_, _, _, _, 100]
    right--, position--
    
nums = [-4, -1, 0, 3, 10]
        L           R       position = 3

Iteration 2: |-4| = 4, |3| = 3 → 4² = 16 is larger
    result = [_, _, _, 16, 100]
    left++, position--
    
nums = [-4, -1, 0, 3, 10]
            L       R       position = 2

Iteration 3: |-1| = 1, |3| = 3 → 3² = 9 is larger
    result = [_, _, 9, 16, 100]
    right--, position--
    
nums = [-4, -1, 0, 3, 10]
            L    R          position = 1

Iteration 4: |-1| = 1, |0| = 0 → 1² = 1 is larger
    result = [_, 1, 9, 16, 100]
    left++, position--
    
nums = [-4, -1, 0, 3, 10]
               LR           position = 0

Iteration 5: |0| = 0 → 0² = 0
    result = [0, 1, 9, 16, 100]
    Done!

Key Insights:
-------------
1. The largest squares come from the extremes (most negative or most positive)
2. Build result from largest to smallest (right to left)
3. Use absolute values or squares for comparison
4. Two pointers move inward from both ends
5. No sorting needed - input is already sorted!

Edge Cases to Consider:
-----------------------
- All negative numbers
- All positive numbers
- All zeros
- Single element
- Array with zero in the middle
- Symmetric array like [-3, -2, -1, 0, 1, 2, 3]

Follow-up Questions:
--------------------
1. What if the input array was NOT sorted? How would your approach change?
2. Can you solve it in-place (without creating a new array)?
   (Answer: Not really, because squares change the values)
3. What if duplicates are allowed? Does your solution still work?
   (Answer: Yes, the algorithm handles duplicates naturally)

Expected Time Complexity: O(n) - single pass through the array
Expected Space Complexity: O(n) - for the result array (not counting input)
"""


def sorted_squares(nums: list[int]) -> list[int]:
    """
    Return the squares of a sorted array, sorted in ascending order.
    
    Args:
        nums: A sorted list of integers (may include negative, zero, positive)
    
    Returns:
        A new list containing the squares of nums, sorted in ascending order
    
    Example:
        >>> sorted_squares([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
        >>> sorted_squares([-7, -3, 2, 3, 11])
        [4, 9, 9, 49, 121]
    """
    new_list = [0] * len(nums)
    left , right = 0, len(nums) - 1
    position = len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if left_square > right_square:
            new_list[position] = left_square
            left += 1
        else:
            new_list[position] = right_square
            right -= 1
        position -= 1

    return new_list


# Test cases
if __name__ == "__main__":
    # Test case 1: Mixed negative and positive
    nums1 = [-4, -1, 0, 3, 10]
    print(f"Test 1: nums = {nums1}")
    result1 = sorted_squares(nums1)
    print(f"Output: {result1}")
    print(f"Expected: [0, 1, 9, 16, 100]\n")
    
    # Test case 2: Mixed with duplicates
    nums2 = [-7, -3, 2, 3, 11]
    print(f"Test 2: nums = {nums2}")
    result2 = sorted_squares(nums2)
    print(f"Output: {result2}")
    print(f"Expected: [4, 9, 9, 49, 121]\n")
    
    # Test case 3: All negative
    nums3 = [-5, -3, -2, -1]
    print(f"Test 3: nums = {nums3}")
    result3 = sorted_squares(nums3)
    print(f"Output: {result3}")
    print(f"Expected: [1, 4, 9, 25]\n")
    
    # Test case 4: All positive
    nums4 = [1, 2, 3, 4, 5]
    print(f"Test 4: nums = {nums4}")
    result4 = sorted_squares(nums4)
    print(f"Output: {result4}")
    print(f"Expected: [1, 4, 9, 16, 25]\n")
    
    # Test case 5: Starting with zero
    nums5 = [0, 1, 2]
    print(f"Test 5: nums = {nums5}")
    result5 = sorted_squares(nums5)
    print(f"Output: {result5}")
    print(f"Expected: [0, 1, 4]\n")
    
    # Test case 6: Symmetric around zero
    nums6 = [-1, 0, 1]
    print(f"Test 6: nums = {nums6}")
    result6 = sorted_squares(nums6)
    print(f"Output: {result6}")
    print(f"Expected: [0, 1, 1]\n")
    
    # Test case 7: Single element (negative)
    nums7 = [-5]
    print(f"Test 7: nums = {nums7}")
    result7 = sorted_squares(nums7)
    print(f"Output: {result7}")
    print(f"Expected: [25]\n")
    
    # Test case 8: Single element (positive)
    nums8 = [5]
    print(f"Test 8: nums = {nums8}")
    result8 = sorted_squares(nums8)
    print(f"Output: {result8}")
    print(f"Expected: [25]\n")
    
    # Test case 9: All zeros
    nums9 = [0, 0, 0]
    print(f"Test 9: nums = {nums9}")
    result9 = sorted_squares(nums9)
    print(f"Output: {result9}")
    print(f"Expected: [0, 0, 0]\n")
    
    # Test case 10: Large symmetric array
    nums10 = [-10, -5, -3, 0, 3, 5, 10]
    print(f"Test 10: nums = {nums10}")
    result10 = sorted_squares(nums10)
    print(f"Output: {result10}")
    print(f"Expected: [0, 9, 9, 25, 25, 100, 100]\n")
    
    # Test case 11: Two elements
    nums11 = [-1, 2]
    print(f"Test 11: nums = {nums11}")
    result11 = sorted_squares(nums11)
    print(f"Output: {result11}")
    print(f"Expected: [1, 4]\n")
    
    # Test case 12: Larger negatives than positives
    nums12 = [-100, -50, 1, 2]
    print(f"Test 12: nums = {nums12}")
    result12 = sorted_squares(nums12)
    print(f"Output: {result12}")
    print(f"Expected: [1, 4, 2500, 10000]\n")
    
    # Test case 13: Edge case with very large numbers
    nums13 = [-10000, -5000, 0, 5000, 10000]
    print(f"Test 13: nums = {nums13}")
    result13 = sorted_squares(nums13)
    print(f"Output: {result13}")
    print(f"Expected: [0, 25000000, 25000000, 100000000, 100000000]\n")
