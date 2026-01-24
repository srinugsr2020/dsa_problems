"""
Substring with Concatenation of All Words Problem (Sliding Window + Hash Map)

Problem Statement:
------------------
You are given a string s and an array of strings words. All the strings in words 
are of the SAME length.

A concatenated substring is a substring of s that contains ALL the strings in words 
concatenated in ANY order.

Return the starting indices of all the concatenated substrings in s. You can return 
the answer in any order.

Important Notes:
----------------
1. All strings in words have THE SAME length
2. The words can appear in ANY order in the concatenated substring
3. Each word in words must be used EXACTLY ONCE in each valid substring
4. Words can repeat in the words array (duplicates allowed)
5. The concatenated substring must be a CONTIGUOUS substring of s

Constraints:
------------
- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters

Examples:
---------
Example 1:
    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0, 9]
    Explanation:
        The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"].
        The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"].
        
        Breakdown:
        Index 0: "barfoo" = "bar" + "foo" ✓
        Index 9: "foobar" = "foo" + "bar" ✓

Example 2:
    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    Output: []
    Explanation:
        We need to use each word exactly once.
        words has "word" twice, "good" once, "best" once.
        
        No valid concatenation exists because:
        - "wordgoodgoodgoodbest" has three "good"s (we only have one in words)
        - We need exactly: 2 "word"s, 1 "good", 1 "best"

Example 3:
    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6, 9, 12]
    Explanation:
        Index 6: "foobarthe" = "foo" + "bar" + "the" ✓
        Index 9: "barthefoo" = "bar" + "the" + "foo" ✓
        Index 12: "thefoobar" = "the" + "foo" + "bar" ✓

Example 4:
    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"]
    Output: [8]
    Explanation:
        We need: 1 "word", 2 "good"s, 1 "best"
        Index 8: "goodgoodgoodbestword" - wait, that's too long!
        Actually: Index 8: "goodgoodbestword" = "good" + "good" + "best" + "word" ✓

Example 5:
    Input: s = "lingmindraboofooowingdingbarrwingmonkeypoundcake", words = ["fooo","barr","wing","ding","wing"]
    Output: [13]
    Explanation:
        We need: 1 "fooo", 1 "barr", 2 "wing"s, 1 "ding"
        Index 13: "fooowingdingbarrwing" = "fooo" + "wing" + "ding" + "barr" + "wing" ✓

Understanding the Problem:
--------------------------
Key insight: This is NOT a permutation problem where you check all permutations.
Instead, use a sliding window approach!

Given:
- Each word has the same length (let's call it word_len)
- Number of words = word_count
- Total concatenation length = word_len * word_count

We need to find all substrings of length (word_len * word_count) in s that can 
be split into word_count chunks of length word_len, where these chunks exactly 
match the words array (considering frequency).

Approach: Sliding Window with Word Frequency Map
-------------------------------------------------
1. Create a frequency map of words (handles duplicates)
2. Calculate the total length needed: word_len * word_count
3. Use a sliding window of that length
4. For each window, split it into chunks of word_len
5. Check if these chunks match the word frequency map
6. If yes, add the starting index to results

Algorithm Steps:
----------------
1. Edge cases:
   - If s is empty or words is empty, return []
   - If len(s) < word_len * word_count, return []

2. Create word_freq: a frequency map of all words in words array
   Example: ["foo", "bar", "foo"] → {"foo": 2, "bar": 1}

3. Initialize:
   - word_len = len(words[0])
   - word_count = len(words)
   - total_len = word_len * word_count
   - result = []

4. Sliding window approach (optimized):
   - Instead of checking every index (which would be O(n * m)),
   - We check only word_len different starting positions (0 to word_len-1)
   - For each starting position, slide by word_len each time
   
5. For each starting offset (0 to word_len-1):
   - Use a window that slides by word_len
   - Maintain a current_freq map for words in current window
   - Use two pointers: left and right
   - Expand right by word_len each time
   - Contract left when we have too many words or invalid words

6. For each position in the window:
   - Extract word of length word_len
   - If word is in word_freq:
     * Add it to current_freq
     * If frequency exceeds word_freq, shrink window from left
   - If word is not in word_freq:
     * Reset window (start fresh from next position)
   - If current window size == total_len and frequencies match:
     * Add starting index to result

Visual Example:
---------------
s = "barfoothefoobarman", words = ["foo","bar"]

word_len = 3, word_count = 2, total_len = 6
word_freq = {"foo": 1, "bar": 1}

Starting offset 0: Check positions 0, 6, 12, ...
    Position 0: "barfoo"
        Split: "bar" + "foo"
        Check: {"bar": 1, "foo": 1} == word_freq ✓
        Result: [0]
    
    Position 6: "thefo" + next... (incomplete, skip)

Starting offset 1: Check positions 1, 7, 13, ...
    Position 1: "arfoot"
        Split: "arf" + "oot"
        "arf" not in word_freq ✗

Starting offset 2: Check positions 2, 8, 14, ...
    Position 2: "rfothe"
        Split: "rfo" + "the"
        "rfo" not in word_freq ✗

... continuing through all offsets ...

Starting offset 0 (continuing from position 12):
    Position 12: "foobar"... wait, that's only 6 chars starting from index 9!
    
Let me recalculate:
    s = "barfoothefoobarman"
         0123456789...
    
    Position 9: "foobar"
        Split: "foo" + "bar"
        Check: {"foo": 1, "bar": 1} == word_freq ✓
        Result: [0, 9]

Optimized Sliding Window Approach:
-----------------------------------
Instead of checking EVERY position (which gives O(n * m) time where n = len(s), 
m = word_count), we can optimize:

1. We only need to check word_len different starting positions (0, 1, 2, ..., word_len-1)
2. For each starting position, we slide by word_len each time
3. Use a sliding window with two pointers to track valid word sequences

This reduces time complexity significantly!

Pseudocode for Optimized Approach:
-----------------------------------
for offset in range(word_len):
    left = offset
    right = offset
    current_freq = {}
    count = 0  # number of valid words matched
    
    while right + word_len <= len(s):
        # Get the word at right pointer
        word = s[right:right + word_len]
        right += word_len
        
        if word in word_freq:
            current_freq[word] = current_freq.get(word, 0) + 1
            count += 1
            
            # If word appears too many times, shrink from left
            while current_freq[word] > word_freq[word]:
                left_word = s[left:left + word_len]
                current_freq[left_word] -= 1
                count -= 1
                left += word_len
            
            # If we have exactly word_count words, we found a match
            if count == word_count:
                result.append(left)
                # Shrink window by one word to continue searching
                left_word = s[left:left + word_len]
                current_freq[left_word] -= 1
                count -= 1
                left += word_len
        else:
            # Word not in words list, reset window
            current_freq.clear()
            count = 0
            left = right

Key Insights:
-------------
1. Use frequency maps to handle duplicate words
2. Sliding window approach is more efficient than checking all substrings
3. Only need to check word_len different starting positions
4. When a word appears too many times, shrink window from left
5. When an invalid word is found, reset the window entirely

Edge Cases to Consider:
-----------------------
1. Empty s or empty words: return []
2. s shorter than concatenation length: return []
3. Single word in words: find all occurrences of that word
4. All words are the same: need correct frequency count
5. No valid concatenations: return []
6. words array has duplicates: use frequency map
7. s has repeated patterns
8. Overlapping valid substrings

Common Pitfalls:
----------------
1. Forgetting that words can have duplicates (must use frequency map!)
2. Not handling the case when word appears more times than needed
3. Off-by-one errors in substring extraction
4. Not resetting window when an invalid word is encountered
5. Inefficient approach checking every single position
6. Not accounting for word_len when sliding the window

Follow-up Questions:
--------------------
1. What if words can have different lengths? (Much harder!)
2. Can you solve it without the sliding window optimization? (Yes, but slower)
3. What if we need to find the longest concatenation instead? (Different problem)
4. How would you handle case-insensitive matching?

Expected Time Complexity: O(n * word_len) where n = len(s)
    - We check word_len different offsets
    - For each offset, we scan through s once
    - Each substring extraction is O(word_len)
    
Expected Space Complexity: O(word_count * word_len)
    - Storing the word frequency map
    - Current window frequency map
"""


def find_substring(s: str, words: list[str]) -> list[int]:
    """
    Find all starting indices of concatenated substrings in s that contain all words.
    
    Args:
        s: The main string to search in
        words: List of words (all same length) to find concatenated
    
    Returns:
        List of starting indices where concatenated substrings begin
    
    Example:
        >>> find_substring("barfoothefoobarman", ["foo","bar"])
        [0, 9]
        >>> find_substring("wordgoodgoodgoodbestword", ["word","good","best","word"])
        []
    """
    
    if not s or not words or not words[0]:
        return []
    from collections import defaultdict
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    result = []
    for offset in range(word_len):
        left = offset
        right = offset
        current_freq = defaultdict(int)
        count = 0  # number of valid words matched
        
        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len
            
            if word in word_freq:
                current_freq[word] += 1
                count += 1
                
                while current_freq[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    current_freq[left_word] -= 1
                    count -= 1
                    left += word_len
                
                if count == word_count:
                    result.append(left)
                    left_word = s[left:left + word_len]
                    current_freq[left_word] -= 1
                    count -= 1
                    left += word_len
            else:
                current_freq.clear()
                count = 0
                left = right

    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: Basic example
    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]
    print(f"Test 1: s = '{s1}', words = {words1}")
    result1 = find_substring(s1, words1)
    print(f"Output: {result1}")
    print(f"Expected: [0, 9]\n")
    
    # Test case 2: No valid concatenation
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word", "good", "best", "word"]
    print(f"Test 2: s = '{s2}', words = {words2}")
    result2 = find_substring(s2, words2)
    print(f"Output: {result2}")
    print(f"Expected: []\n")
    
    # Test case 3: Multiple valid positions
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar", "foo", "the"]
    print(f"Test 3: s = '{s3}', words = {words3}")
    result3 = find_substring(s3, words3)
    print(f"Output: {result3}")
    print(f"Expected: [6, 9, 12]\n")
    
    # Test case 4: Duplicate words
    s4 = "wordgoodgoodgoodbestword"
    words4 = ["word", "good", "best", "good"]
    print(f"Test 4: s = '{s4}', words = {words4}")
    result4 = find_substring(s4, words4)
    print(f"Output: {result4}")
    print(f"Expected: [8]\n")
    
    # Test case 5: Longer example
    s5 = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words5 = ["fooo", "barr", "wing", "ding", "wing"]
    print(f"Test 5: s = '{s5}', words = {words5}")
    result5 = find_substring(s5, words5)
    print(f"Output: {result5}")
    print(f"Expected: [13]\n")
    
    # Test case 6: Empty words
    s6 = "test"
    words6 = []
    print(f"Test 6: s = '{s6}', words = {words6}")
    result6 = find_substring(s6, words6)
    print(f"Output: {result6}")
    print(f"Expected: []\n")
    
    # Test case 7: s too short
    s7 = "a"
    words7 = ["a", "b"]
    print(f"Test 7: s = '{s7}', words = {words7}")
    result7 = find_substring(s7, words7)
    print(f"Output: {result7}")
    print(f"Expected: []\n")
    
    # Test case 8: Single word
    s8 = "aaaaa"
    words8 = ["aa"]
    print(f"Test 8: s = '{s8}', words = {words8}")
    result8 = find_substring(s8, words8)
    print(f"Output: {result8}")
    print(f"Expected: [0, 1, 2, 3]\n")
    
    # Test case 9: All same words
    s9 = "aaaa"
    words9 = ["aa", "aa"]
    print(f"Test 9: s = '{s9}', words = {words9}")
    result9 = find_substring(s9, words9)
    print(f"Output: {result9}")
    print(f"Expected: [0]\n")
    
    # Test case 10: Exact match
    s10 = "foobar"
    words10 = ["foo", "bar"]
    print(f"Test 10: s = '{s10}', words = {words10}")
    result10 = find_substring(s10, words10)
    print(f"Output: {result10}")
    print(f"Expected: [0]\n")
    
    # Test case 11: No match at all
    s11 = "abcdef"
    words11 = ["gh", "ij"]
    print(f"Test 11: s = '{s11}', words = {words11}")
    result11 = find_substring(s11, words11)
    print(f"Output: {result11}")
    print(f"Expected: []\n")
    
    # Test case 12: Overlapping patterns
    s12 = "ababab"
    words12 = ["ab", "ab"]
    print(f"Test 12: s = '{s12}', words = {words12}")
    result12 = find_substring(s12, words12)
    print(f"Output: {result12}")
    print(f"Expected: [0, 2]\n")
