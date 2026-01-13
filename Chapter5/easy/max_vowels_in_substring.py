"""
Maximum Number of Vowels in a Substring of Given Length (LeetCode #1456)

Problem:
    Given a string s and an integer k, return the maximum number of vowel 
    letters in any substring of s with length k.
    
    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
    - 1 <= s.length <= 10^5
    - s consists of lowercase English letters.
    - 1 <= k <= s.length

Time Complexity: O(n) - single pass through the string
Space Complexity: O(1) - only using constant extra space
"""


def max_vowels(s: str, k: int) -> int:
    """
    Find maximum number of vowels in any substring of length k.
    
    Approach:
        Use a fixed-size sliding window of size k.
        - Count vowels in the first window
        - Slide window: add new char vowel status, remove old char vowel status
        - Track maximum vowel count
    
    Args:
        s: Input string of lowercase letters
        k: Length of substring
        
    Returns:
        Maximum number of vowels in any substring of length k
    """
    vowels = set('aeiou')
    
    # Count vowels in first window
    vowel_count = sum(1 for char in s[:k] if char in vowels)
    max_count = vowel_count
    
    # Early exit if we already have all vowels
    if max_count == k:
        return k
    
    # Slide the window
    for i in range(k, len(s)):
        # Add new character
        if s[i] in vowels:
            vowel_count += 1
        
        # Remove old character
        if s[i - k] in vowels:
            vowel_count -= 1
        
        max_count = max(max_count, vowel_count)
        
        # Early exit optimization
        if max_count == k:
            return k
    
    return max_count


def max_vowels_with_positions(s: str, k: int) -> tuple:
    """
    Find maximum vowels and return the substring with most vowels.
    
    Useful for debugging and understanding.
    
    Args:
        s: Input string of lowercase letters
        k: Length of substring
        
    Returns:
        Tuple of (max_vowels, best_substring, start_index)
    """
    vowels = set('aeiou')
    
    # Count vowels in first window
    vowel_count = sum(1 for char in s[:k] if char in vowels)
    max_count = vowel_count
    best_start = 0
    
    # Slide the window
    for i in range(k, len(s)):
        # Add new character
        if s[i] in vowels:
            vowel_count += 1
        
        # Remove old character
        if s[i - k] in vowels:
            vowel_count -= 1
        
        if vowel_count > max_count:
            max_count = vowel_count
            best_start = i - k + 1
    
    best_substring = s[best_start:best_start + k]
    return max_count, best_substring, best_start


def count_vowels_brute_force(s: str, k: int) -> int:
    """
    Brute force approach for comparison (O(n*k) time).
    
    Args:
        s: Input string of lowercase letters
        k: Length of substring
        
    Returns:
        Maximum number of vowels in any substring of length k
    """
    vowels = set('aeiou')
    max_count = 0
    
    for i in range(len(s) - k + 1):
        substring = s[i:i + k]
        count = sum(1 for char in substring if char in vowels)
        max_count = max(max_count, count)
    
    return max_count


# --------------------- Test Cases ---------------------

if __name__ == "__main__":
    # Test Case 1: Consecutive vowels
    s1 = "abciiidef"
    k1 = 3
    result1 = max_vowels(s1, k1)
    print(f"Test 1: s='{s1}', k={k1}")
    print(f"  Result: {result1}")  # Expected: 3
    
    # Test Case 2: All vowels
    s2 = "aeiou"
    k2 = 2
    result2 = max_vowels(s2, k2)
    print(f"Test 2: s='{s2}', k={k2}")
    print(f"  Result: {result2}")  # Expected: 2
    
    # Test Case 3: Mixed
    s3 = "leetcode"
    k3 = 3
    result3 = max_vowels(s3, k3)
    print(f"Test 3: s='{s3}', k={k3}")
    print(f"  Result: {result3}")  # Expected: 2
    
    # Test Case 4: No vowels
    s4 = "bcdfg"
    k4 = 2
    result4 = max_vowels(s4, k4)
    print(f"Test 4: s='{s4}', k={k4}")
    print(f"  Result: {result4}")  # Expected: 0
    
    # Test Case 5: k equals string length
    s5 = "aeiou"
    k5 = 5
    result5 = max_vowels(s5, k5)
    print(f"Test 5: s='{s5}', k={k5}")
    print(f"  Result: {result5}")  # Expected: 5
    
    # Test Case 6: Single character
    s6 = "a"
    k6 = 1
    result6 = max_vowels(s6, k6)
    print(f"Test 6: s='{s6}', k={k6}")
    print(f"  Result: {result6}")  # Expected: 1
    
    # Test Case 7: With positions
    s7 = "abciiidef"
    k7 = 3
    count, substring, start = max_vowels_with_positions(s7, k7)
    print(f"Test 7: s='{s7}', k={k7}")
    print(f"  Max vowels: {count}, Substring: '{substring}' at index {start}")
    
    # Test Case 8: Verify with brute force
    s8 = "weallloveyou"
    k8 = 7
    result8 = max_vowels(s8, k8)
    result8_brute = count_vowels_brute_force(s8, k8)
    print(f"Test 8: s='{s8}', k={k8}")
    print(f"  Sliding Window: {result8}, Brute Force: {result8_brute}")
    assert result8 == result8_brute, "Results don't match!"
    
    print("\nAll tests passed!")
