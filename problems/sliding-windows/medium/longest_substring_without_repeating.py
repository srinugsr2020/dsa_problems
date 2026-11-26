"""
Longest Substring Without Repeating Characters Problem

Problem Statement:
------------------
Given a string 's', find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within a string.

Constraints:
------------
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols, and spaces

Examples:
---------
Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with length 3

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with length 1

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with length 3
    Note: "pwke" is a subsequence, not a substring

Example 4:
    Input: s = ""
    Output: 0

Hints:
------
1. Use the sliding window technique with two pointers
2. Maintain a hash set/map to track characters in the current window
3. When you encounter a duplicate, shrink the window from the left
4. Alternative: store the last index of each character for O(1) window adjustment
5. The window [left, right] always contains unique characters

Expected Time Complexity: O(n)
Expected Space Complexity: O(min(n, m)) where m is the size of character set
"""


def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Uses sliding window with a hash set to track characters in current window.
    
    Args:
        s: Input string
    
    Returns:
        Length of the longest substring without repeating characters
    
    Example:
        >>> length_of_longest_substring("abcabcbb")
        3
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window from left until no duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to the set
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


def length_of_longest_substring_optimized(s: str) -> int:
    """
    Optimized approach: use hash map to store last index of each character.
    
    Instead of shrinking one by one, jump directly to the position after
    the last occurrence of the duplicate character.
    
    Args:
        s: Input string
    
    Returns:
        Length of the longest substring without repeating characters
    """
    char_index = {}  # character -> last seen index
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If character was seen and is within current window
        if char in char_index and char_index[char] >= left:
            # Jump left pointer to position after the duplicate
            left = char_index[char] + 1
        
        # Update last seen index
        char_index[char] = right
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


def length_of_longest_substring_array(s: str) -> int:
    """
    Alternative approach using array instead of hash map (for ASCII characters).
    
    Slightly faster due to array indexing vs hash lookups.
    
    Args:
        s: Input string
    
    Returns:
        Length of the longest substring without repeating characters
    """
    # Array to store last index of each character (-1 means not seen)
    last_index = [-1] * 128  # ASCII characters
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        char_code = ord(char)
        
        # If character was seen within current window
        if last_index[char_code] >= left:
            left = last_index[char_code] + 1
        
        last_index[char_code] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"Test 1: s = '{s1}'")
    print(f"Output: {length_of_longest_substring(s1)}")
    print(f"Expected: 3 (substring 'abc')\n")
    
    # Test case 2
    s2 = "bbbbb"
    print(f"Test 2: s = '{s2}'")
    print(f"Output: {length_of_longest_substring(s2)}")
    print(f"Expected: 1 (substring 'b')\n")
    
    # Test case 3
    s3 = "pwwkew"
    print(f"Test 3: s = '{s3}'")
    print(f"Output: {length_of_longest_substring(s3)}")
    print(f"Expected: 3 (substring 'wke')\n")
    
    # Test case 4: Empty string
    s4 = ""
    print(f"Test 4: s = '{s4}'")
    print(f"Output: {length_of_longest_substring(s4)}")
    print(f"Expected: 0\n")
    
    # Test case 5: All unique characters
    s5 = "abcdef"
    print(f"Test 5: s = '{s5}'")
    print(f"Output: {length_of_longest_substring(s5)}")
    print(f"Expected: 6\n")
    
    # Test case 6: Single character
    s6 = "a"
    print(f"Test 6: s = '{s6}'")
    print(f"Output: {length_of_longest_substring(s6)}")
    print(f"Expected: 1\n")
    
    # Test case 7: With spaces and special characters
    s7 = "a b c a"
    print(f"Test 7: s = '{s7}'")
    print(f"Output: {length_of_longest_substring(s7)}")
    print(f"Expected: 4 (substring 'b c ' or ' c a')\n")
    
    # Test optimized approach
    print("--- Testing optimized approach ---")
    print(f"Optimized Test 1: {length_of_longest_substring_optimized(s1)}")
    print(f"Optimized Test 2: {length_of_longest_substring_optimized(s2)}")
    print(f"Optimized Test 3: {length_of_longest_substring_optimized(s3)}")
    
    print("\n--- Testing array approach ---")
    print(f"Array Test 1: {length_of_longest_substring_array(s1)}")
    print(f"Array Test 2: {length_of_longest_substring_array(s2)}")
    print(f"Array Test 3: {length_of_longest_substring_array(s3)}")
