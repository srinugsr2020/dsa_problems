"""
Group Anagrams Problem

Problem Statement:
------------------
Given an array of strings 'strs', group the anagrams together. You can return the answer 
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.

Constraints:
------------
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters

Examples:
---------
Example 1:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Hints:
------
1. Two strings are anagrams if they have the same characters with the same frequencies
2. One way to identify anagrams: sort the characters - anagrams will have the same sorted form
3. Another way: use a character count tuple as the key
4. Use a hash map to group strings by their "anagram signature"
5. The key must be hashable (use tuple, not list)

Expected Time Complexity: O(n * k log k) where n = number of strings, k = max string length
                          (O(n * k) if using character count approach)
Expected Space Complexity: O(n * k) for storing all strings in the hash map
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams together using sorted string as key.
    
    Args:
        strs: List of strings to group
    
    Returns:
        List of grouped anagrams
    
    Example:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Sort characters to create anagram signature
        key = tuple(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


def group_anagrams_count(strs: list[str]) -> list[list[str]]:
    """
    Alternative approach: use character count as key (O(n * k) time).
    
    Instead of sorting, count frequency of each character.
    This is faster for long strings since counting is O(k) vs sorting O(k log k).
    
    Args:
        strs: List of strings to group
    
    Returns:
        List of grouped anagrams
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Create a count array for 26 lowercase letters
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple of counts as key (hashable)
        key = tuple(count)
        groups[key].append(s)
    
    return list(groups.values())


def group_anagrams_prime(strs: list[str]) -> list[list[str]]:
    """
    Alternative approach: use prime number product as key.
    
    Map each letter to a unique prime number. The product of primes
    for a string will be unique for each set of anagrams.
    
    Note: This can overflow for very long strings, but works for typical inputs.
    
    Args:
        strs: List of strings to group
    
    Returns:
        List of grouped anagrams
    """
    # First 26 prime numbers for a-z
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    
    groups = defaultdict(list)
    
    for s in strs:
        # Product of primes is unique for each anagram group
        key = 1
        for char in s:
            key *= primes[ord(char) - ord('a')]
        groups[key].append(s)
    
    return list(groups.values())


# Test cases
if __name__ == "__main__":
    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Test 1: strs = {strs1}")
    result1 = group_anagrams(strs1)
    print(f"Output: {result1}")
    print(f"Expected: [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']] (order may vary)\n")
    
    # Test case 2: Empty string
    strs2 = [""]
    print(f"Test 2: strs = {strs2}")
    print(f"Output: {group_anagrams(strs2)}")
    print(f"Expected: [['']]\n")
    
    # Test case 3: Single character
    strs3 = ["a"]
    print(f"Test 3: strs = {strs3}")
    print(f"Output: {group_anagrams(strs3)}")
    print(f"Expected: [['a']]\n")
    
    # Test case 4: No anagrams
    strs4 = ["abc", "def", "ghi"]
    print(f"Test 4: strs = {strs4}")
    print(f"Output: {group_anagrams(strs4)}")
    print(f"Expected: [['abc'], ['def'], ['ghi']]\n")
    
    # Test case 5: All anagrams
    strs5 = ["abc", "bca", "cab", "cba"]
    print(f"Test 5: strs = {strs5}")
    print(f"Output: {group_anagrams(strs5)}")
    print(f"Expected: [['abc', 'bca', 'cab', 'cba']]\n")
    
    # Test alternative approaches
    print("--- Testing character count approach ---")
    print(f"Count approach Test 1: {group_anagrams_count(strs1)}")
    
    print("\n--- Testing prime product approach ---")
    print(f"Prime approach Test 1: {group_anagrams_prime(strs1)}")
