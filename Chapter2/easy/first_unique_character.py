"""
First Unique Character in a String Problem

Problem Statement:
------------------
Given a string 's', find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Constraints:
------------
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters

Examples:
---------
Example 1:
    Input: s = "leetcode"
    Output: 0
    Explanation: 'l' is the first character that appears only once

Example 2:
    Input: s = "loveleetcode"
    Output: 2
    Explanation: 'l' appears twice, 'o' appears twice, 'v' is the first unique character at index 2

Example 3:
    Input: s = "aabb"
    Output: -1
    Explanation: All characters repeat, no unique character exists

Hints:
------
1. Use a hash map to count the frequency of each character
2. First pass: count all character occurrences
3. Second pass: find the first character with count == 1
4. Alternative: use collections.Counter for cleaner code

Expected Time Complexity: O(n) where n is the length of the string
Expected Space Complexity: O(1) since we have at most 26 lowercase letters
"""

from collections import Counter


def first_uniq_char(s: str) -> int:
    """
    Find the index of the first non-repeating character in a string.
    
    Args:
        s: A string consisting of lowercase English letters
    
    Returns:
        Index of the first unique character, or -1 if none exists
    
    Example:
        >>> first_uniq_char("leetcode")
        0
    """
    # Count frequency of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find first character with count == 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1


def first_uniq_char_counter(s: str) -> int:
    """
    Alternative approach using collections.Counter.
    
    Args:
        s: A string consisting of lowercase English letters
    
    Returns:
        Index of the first unique character, or -1 if none exists
    """
    freq = Counter(s)
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1


def first_uniq_char_index_tracking(s: str) -> int:
    """
    Alternative approach: track first occurrence index.
    
    Uses a hash map to store first index of each character.
    Characters that appear multiple times are marked with -1.
    
    Args:
        s: A string consisting of lowercase English letters
    
    Returns:
        Index of the first unique character, or -1 if none exists
    """
    first_index = {}
    
    for i, char in enumerate(s):
        if char not in first_index:
            first_index[char] = i  # First occurrence
        else:
            first_index[char] = -1  # Mark as duplicate
    
    # Find minimum index among non-duplicate characters
    min_index = float('inf')
    for char, idx in first_index.items():
        if idx != -1:
            min_index = min(min_index, idx)
    
    return min_index if min_index != float('inf') else -1


# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "leetcode"
    print(f"Test 1: s = '{s1}'")
    print(f"Output: {first_uniq_char(s1)}")
    print(f"Expected: 0\n")
    
    # Test case 2
    s2 = "loveleetcode"
    print(f"Test 2: s = '{s2}'")
    print(f"Output: {first_uniq_char(s2)}")
    print(f"Expected: 2\n")
    
    # Test case 3
    s3 = "aabb"
    print(f"Test 3: s = '{s3}'")
    print(f"Output: {first_uniq_char(s3)}")
    print(f"Expected: -1\n")
    
    # Test case 4: Single character
    s4 = "z"
    print(f"Test 4: s = '{s4}'")
    print(f"Output: {first_uniq_char(s4)}")
    print(f"Expected: 0\n")
    
    # Test case 5: All same characters
    s5 = "aaaa"
    print(f"Test 5: s = '{s5}'")
    print(f"Output: {first_uniq_char(s5)}")
    print(f"Expected: -1\n")
    
    # Test case 6: Unique at the end
    s6 = "aabbccd"
    print(f"Test 6: s = '{s6}'")
    print(f"Output: {first_uniq_char(s6)}")
    print(f"Expected: 6\n")
    
    # Test alternative approaches
    print("--- Testing Counter approach ---")
    print(f"Counter Test 1: {first_uniq_char_counter(s1)}")
    print(f"Counter Test 2: {first_uniq_char_counter(s2)}")
    
    print("\n--- Testing Index Tracking approach ---")
    print(f"Index Tracking Test 1: {first_uniq_char_index_tracking(s1)}")
    print(f"Index Tracking Test 2: {first_uniq_char_index_tracking(s2)}")
