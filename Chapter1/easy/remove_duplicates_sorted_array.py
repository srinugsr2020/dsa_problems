"""
Remove Duplicates from Sorted Array Problem (Two Pointers Approach)

Problem Statement:
------------------
Given an integer array 'nums' sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of the 
elements should be kept the same. Then return the number of unique elements in 'nums'.

Consider the number of unique elements of 'nums' to be 'k'. To get accepted, you need 
to do the following things:

1. Change the array 'nums' such that the first 'k' elements of 'nums' contain the 
   unique elements in the order they were present in 'nums' initially.
2. The remaining elements of 'nums' are not important as well as the size of 'nums'.
3. Return 'k'.

Custom Judge:
-------------
The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length
    
    int k = removeDuplicates(nums); // Calls your implementation
    
    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

If all assertions pass, then your solution will be accepted.

Constraints:
------------
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order
- You must do this in-place with O(1) extra memory

Examples:
---------
Example 1:
    Input: nums = [1, 1, 2]
    Output: 2, nums = [1, 2, _]
    Explanation: Your function should return k = 2, with the first two elements 
                 of nums being 1 and 2 respectively. It does not matter what you 
                 leave beyond the returned k (hence they are underscores).

Example 2:
    Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
    Explanation: Your function should return k = 5, with the first five elements 
                 of nums being 0, 1, 2, 3, and 4 respectively. It does not matter 
                 what you leave beyond the returned k.

Example 3:
    Input: nums = [1, 1, 1, 1]
    Output: 1, nums = [1, _, _, _]
    Explanation: All elements are duplicates, so only one unique element.

Example 4:
    Input: nums = [1, 2, 3, 4, 5]
    Output: 5, nums = [1, 2, 3, 4, 5]
    Explanation: No duplicates, all elements are unique.

Hints:
------
1. Use two pointers: slow pointer for the position to place next unique element,
   and fast pointer to scan through the array
2. Start with slow pointer at index 0 or 1 (since first element is always unique)
3. Move fast pointer through the array
4. When you find an element different from the previous one, place it at slow pointer
5. Increment slow pointer after placing a unique element
6. The slow pointer's position will give you the count of unique elements
7. Since the array is sorted, duplicates are always adjacent

Expected Time Complexity: O(n) where n is the length of the array
Expected Space Complexity: O(1) - in-place modification
"""


def remove_duplicates(nums: list[int]) -> int:
    """
    Remove duplicates from a sorted array in-place.
    
    Args:
        nums: A sorted list of integers (sorted in non-decreasing order)
    
    Returns:
        The number of unique elements in the array. The first k elements of nums
        should contain the unique elements.
    
    Example:
        >>> nums = [1, 1, 2]
        >>> k = remove_duplicates(nums)
        >>> k
        2
        >>> nums[:k]
        [1, 2]
    """
    i , j = 0, 1
    while j < len(nums):
        print(i , j)
        if nums[i] == nums[j]:
            j += 1
        else:
            nums[i + 1] = nums[j]
            i += 1
            j += 1
    return i + 1


# Test cases
if __name__ == "__main__":
    # Test case 1: Array with some duplicates
    nums1 = [1, 1, 2]
    print(f"Test 1: nums = {nums1}")
    k1 = remove_duplicates(nums1)
    print(f"Output: k = {k1}, nums = {nums1}")
    print(f"Expected: k = 2, nums[:k] = [1, 2]\n")
    
    # Test case 2: Array with many duplicates
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Test 2: nums = {nums2}")
    k2 = remove_duplicates(nums2)
    print(f"Output: k = {k2}, nums = {nums2}")
    print(f"Expected: k = 5, nums[:k] = [0, 1, 2, 3, 4]\n")
    
    # Test case 3: All elements are duplicates
    nums3 = [1, 1, 1, 1]
    print(f"Test 3: nums = {nums3}")
    k3 = remove_duplicates(nums3)
    print(f"Output: k = {k3}, nums = {nums3}")
    print(f"Expected: k = 1, nums[:k] = [1]\n")
    
    # Test case 4: No duplicates
    nums4 = [1, 2, 3, 4, 5]
    print(f"Test 4: nums = {nums4}")
    k4 = remove_duplicates(nums4)
    print(f"Output: k = {k4}, nums = {nums4}")
    print(f"Expected: k = 5, nums[:k] = [1, 2, 3, 4, 5]\n")
    
    # Test case 5: Single element
    nums5 = [1]
    print(f"Test 5: nums = {nums5}")
    k5 = remove_duplicates(nums5)
    print(f"Output: k = {k5}, nums = {nums5}")
    print(f"Expected: k = 1, nums[:k] = [1]\n")
    
    # Test case 6: Negative numbers with duplicates
    nums6 = [-3, -3, -2, -1, -1, 0, 0, 0, 1]
    print(f"Test 6: nums = {nums6}")
    k6 = remove_duplicates(nums6)
    print(f"Output: k = {k6}, nums = {nums6}")
    print(f"Expected: k = 5, nums[:k] = [-3, -2, -1, 0, 1]\n")
    
    # Test case 7: Two unique elements with many duplicates
    nums7 = [1, 1, 1, 1, 2, 2, 2, 2]
    print(f"Test 7: nums = {nums7}")
    k7 = remove_duplicates(nums7)
    print(f"Output: k = {k7}, nums = {nums7}")
    print(f"Expected: k = 2, nums[:k] = [1, 2]\n")
