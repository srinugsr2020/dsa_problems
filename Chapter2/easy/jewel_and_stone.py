"""
Jewels and Stones Problem

Problem Statement:
------------------
You're given strings 'jewels' representing the types of stones that are jewels, 
and 'stones' representing the stones you have. Each character in 'stones' is a type 
of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Constraints:
------------
- 1 <= jewels.length, stones.length <= 50
- jewels and stones consist of only English letters
- All the characters of jewels are unique

Examples:
---------
Example 1:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3
    Explanation: 'a' appears 1 time, 'A' appears 2 times = 3 jewels total

Example 2:
    Input: jewels = "z", stones = "ZZ"
    Output: 0
    Explanation: 'z' != 'Z', so no stones are jewels

Hints:
------
1. Convert jewels string to a set for O(1) lookup
2. Iterate through stones and count how many are in the jewels set
3. This is a classic "membership testing" problem perfect for sets

Expected Time Complexity: O(j + s) where j = len(jewels), s = len(stones)
Expected Space Complexity: O(j) for storing the jewels set
"""


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    """
    Count how many stones are jewels.
    
    Args:
        jewels: String of unique characters representing jewel types
        stones: String of characters representing stones you have
    
    Returns:
        Number of stones that are also jewels
    
    Example:
        >>> num_jewels_in_stones("aA", "aAAbbbb")
        3
    """
    jewel_set = set(jewels)
    count = 0
    
    for stone in stones:
        if stone in jewel_set:
            count += 1
    
    return count


def num_jewels_in_stones_oneliner(jewels: str, stones: str) -> int:
    """
    One-liner approach using sum and generator expression.
    
    Args:
        jewels: String of unique characters representing jewel types
        stones: String of characters representing stones you have
    
    Returns:
        Number of stones that are also jewels
    """
    return sum(stone in set(jewels) for stone in stones)


def num_jewels_in_stones_optimized(jewels: str, stones: str) -> int:
    """
    Optimized one-liner (creates set once, not per iteration).
    
    Args:
        jewels: String of unique characters representing jewel types
        stones: String of characters representing stones you have
    
    Returns:
        Number of stones that are also jewels
    """
    jewel_set = set(jewels)
    return sum(1 for stone in stones if stone in jewel_set)


# Test cases
if __name__ == "__main__":
    # Test case 1
    jewels1 = "aA"
    stones1 = "aAAbbbb"
    print(f"Test 1: jewels = '{jewels1}', stones = '{stones1}'")
    print(f"Output: {num_jewels_in_stones(jewels1, stones1)}")
    print(f"Expected: 3\n")
    
    # Test case 2
    jewels2 = "z"
    stones2 = "ZZ"
    print(f"Test 2: jewels = '{jewels2}', stones = '{stones2}'")
    print(f"Output: {num_jewels_in_stones(jewels2, stones2)}")
    print(f"Expected: 0\n")
    
    # Test case 3: All stones are jewels
    jewels3 = "abc"
    stones3 = "aabbcc"
    print(f"Test 3: jewels = '{jewels3}', stones = '{stones3}'")
    print(f"Output: {num_jewels_in_stones(jewels3, stones3)}")
    print(f"Expected: 6\n")
    
    # Test case 4: No stones are jewels
    jewels4 = "xyz"
    stones4 = "abcdef"
    print(f"Test 4: jewels = '{jewels4}', stones = '{stones4}'")
    print(f"Output: {num_jewels_in_stones(jewels4, stones4)}")
    print(f"Expected: 0\n")
    
    # Test case 5: Single character each
    jewels5 = "a"
    stones5 = "a"
    print(f"Test 5: jewels = '{jewels5}', stones = '{stones5}'")
    print(f"Output: {num_jewels_in_stones(jewels5, stones5)}")
    print(f"Expected: 1\n")
    
    # Test alternative approaches
    print("--- Testing one-liner approach ---")
    print(f"One-liner Test 1: {num_jewels_in_stones_oneliner(jewels1, stones1)}")
    print(f"One-liner Test 2: {num_jewels_in_stones_oneliner(jewels2, stones2)}")
    
    print("\n--- Testing optimized approach ---")
    print(f"Optimized Test 1: {num_jewels_in_stones_optimized(jewels1, stones1)}")
    print(f"Optimized Test 2: {num_jewels_in_stones_optimized(jewels2, stones2)}")
