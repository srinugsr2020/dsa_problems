"""
Valid Anagram Problem

Problem Statement:
------------------
Given two strings 's' and 't', return true if 't' is an anagram of 's', and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Constraints:
------------
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

Examples:
---------
Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Hints:
------
1. If the lengths of the two strings are different, they cannot be anagrams
2. You can sort both strings and compare them (O(n log n))
3. You can use a hash map (or frequency array) to count character occurrences (O(n))
4. Increment counts for string 's' and decrement for string 't'
5. If all counts are zero at the end, they are anagrams

Expected Time Complexity: O(n)
Expected Space Complexity: O(1) (since the character set is fixed at 26 lowercase letters)
"""


def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Args:
        s: First string
        t: Second string
    
    Returns:
        True if t is an anagram of s, False otherwise
    
    Example:
        >>> is_anagram("anagram", "nagaram")
        True
    """
    if len(s) != len(t):
        return False
    
    # Using a dictionary as a hash map
    count = {}
    
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
            
    return len(count) == 0


# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Test 1: s = '{s1}', t = '{t1}'")
    print(f"Output: {is_anagram(s1, t1)}")
    print(f"Expected: True\n")
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    print(f"Test 2: s = '{s2}', t = '{t2}'")
    print(f"Output: {is_anagram(s2, t2)}")
    print(f"Expected: False\n")
    
    # Test case 3: Different lengths
    s3 = "a"
    t3 = "ab"
    print(f"Test 3: s = '{s3}', t = '{t3}'")
    print(f"Output: {is_anagram(s3, t3)}")
    print(f"Expected: False\n")
    
    # Test case 4: Empty strings (though constraint says length >= 1)
    s4 = ""
    t4 = ""
    print(f"Test 4: s = '{s4}', t = '{t4}'")
    print(f"Output: {is_anagram(s4, t4)}")
    print(f"Expected: True\n")
    
    # Test case 5: Same characters but different counts
    s5 = "aa"
    t5 = "bb"
    print(f"Test 5: s = '{s5}', t = '{t5}'")
    print(f"Output: {is_anagram(s5, t5)}")
    print(f"Expected: False\n")
