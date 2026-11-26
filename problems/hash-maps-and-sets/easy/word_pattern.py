"""
Word Pattern Problem

Problem Statement:
------------------
Given a pattern and a string 's', find if 's' follows the same pattern.

Here "follow" means a full match, such that there is a bijection (one-to-one mapping) 
between a letter in pattern and a non-empty word in 's'.

Constraints:
------------
- 1 <= pattern.length <= 300
- pattern contains only lowercase English letters
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '
- s does not contain any leading or trailing spaces
- All the words in s are separated by a single space

Examples:
---------
Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
    Explanation: 'a' -> "dog", 'b' -> "cat" (bijection holds)

Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false
    Explanation: 'a' maps to "dog" initially, but later 'a' maps to "fish"

Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false
    Explanation: 'a' cannot map to both "dog" and "cat"

Example 4:
    Input: pattern = "abba", s = "dog dog dog dog"
    Output: false
    Explanation: 'a' -> "dog" and 'b' -> "dog", but bijection requires unique mappings

Hints:
------
1. Split the string 's' into words
2. Check if the number of pattern characters equals the number of words
3. Use two hash maps: one for pattern -> word, another for word -> pattern
4. This ensures a bijection (one-to-one mapping in both directions)
5. If pattern char maps to different word OR word maps to different pattern char, return False

Expected Time Complexity: O(n + m) where n = len(pattern), m = len(s)
Expected Space Complexity: O(n) for the hash maps
"""


def word_pattern(pattern: str, s: str) -> bool:
    """
    Check if string s follows the given pattern.
    
    Args:
        pattern: A string of lowercase letters representing the pattern
        s: A string of space-separated words
    
    Returns:
        True if s follows the pattern (bijection exists), False otherwise
    
    Example:
        >>> word_pattern("abba", "dog cat cat dog")
        True
    """
    words = s.split()
    
    # Length mismatch means pattern cannot match
    if len(pattern) != len(words):
        return False
    
    # Two maps for bijection: pattern_char -> word and word -> pattern_char
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        # Check if pattern char already maps to a different word
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        # Check if word already maps to a different pattern char
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True


def word_pattern_single_pass(pattern: str, s: str) -> bool:
    """
    Alternative approach: compare first occurrence indices.
    
    If two elements have the same "first occurrence pattern", they match.
    
    Args:
        pattern: A string of lowercase letters representing the pattern
        s: A string of space-separated words
    
    Returns:
        True if s follows the pattern, False otherwise
    """
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    # Map each char/word to its first occurrence index
    # If patterns of first occurrences match, bijection exists
    def get_pattern(sequence):
        mapping = {}
        result = []
        for item in sequence:
            if item not in mapping:
                mapping[item] = len(mapping)
            result.append(mapping[item])
        return result
    
    return get_pattern(pattern) == get_pattern(words)


# Test cases
if __name__ == "__main__":
    # Test case 1: Valid pattern
    pattern1 = "abba"
    s1 = "dog cat cat dog"
    print(f"Test 1: pattern = '{pattern1}', s = '{s1}'")
    print(f"Output: {word_pattern(pattern1, s1)}")
    print(f"Expected: True\n")
    
    # Test case 2: Pattern char maps to different words
    pattern2 = "abba"
    s2 = "dog cat cat fish"
    print(f"Test 2: pattern = '{pattern2}', s = '{s2}'")
    print(f"Output: {word_pattern(pattern2, s2)}")
    print(f"Expected: False\n")
    
    # Test case 3: Same char cannot map to multiple words
    pattern3 = "aaaa"
    s3 = "dog cat cat dog"
    print(f"Test 3: pattern = '{pattern3}', s = '{s3}'")
    print(f"Output: {word_pattern(pattern3, s3)}")
    print(f"Expected: False\n")
    
    # Test case 4: Two chars cannot map to same word (no bijection)
    pattern4 = "abba"
    s4 = "dog dog dog dog"
    print(f"Test 4: pattern = '{pattern4}', s = '{s4}'")
    print(f"Output: {word_pattern(pattern4, s4)}")
    print(f"Expected: False\n")
    
    # Test case 5: Length mismatch
    pattern5 = "abc"
    s5 = "dog cat"
    print(f"Test 5: pattern = '{pattern5}', s = '{s5}'")
    print(f"Output: {word_pattern(pattern5, s5)}")
    print(f"Expected: False\n")
    
    # Test case 6: Single character pattern
    pattern6 = "a"
    s6 = "dog"
    print(f"Test 6: pattern = '{pattern6}', s = '{s6}'")
    print(f"Output: {word_pattern(pattern6, s6)}")
    print(f"Expected: True\n")
    
    # Test alternative approach
    print("--- Testing single pass approach ---")
    print(f"Single pass Test 1: {word_pattern_single_pass(pattern1, s1)}")
    print(f"Single pass Test 2: {word_pattern_single_pass(pattern2, s2)}")
    print(f"Single pass Test 3: {word_pattern_single_pass(pattern3, s3)}")
    print(f"Single pass Test 4: {word_pattern_single_pass(pattern4, s4)}")
