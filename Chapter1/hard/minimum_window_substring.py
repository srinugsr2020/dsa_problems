"""
Minimum Window Substring Problem (Sliding Window + Hash Map)

Problem Statement:
------------------
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in 
the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Important Notes:
----------------
1. The window must contain ALL characters from t (including duplicates)
2. If t has duplicate characters, the window must have at least that many
3. The characters in the window don't need to be in the same order as t
4. We want the MINIMUM length window that satisfies the condition
5. If no valid window exists, return ""

Constraints:
------------
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters

Examples:
---------
Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation:
        The minimum window substring "BANC" includes:
        - 'A' from t ✓
        - 'B' from t ✓
        - 'C' from t ✓
        
        Other valid windows: "ADOBEC", "CODEBA", "BECODEBA", etc.
        But "BANC" has the minimum length (4).

Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation:
        The entire string s is the minimum window.

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation:
        Both 'a's from t must be included in the window.
        Since s only has one 'a', it is impossible to form such a window.
        Return empty string.

Example 4:
    Input: s = "ADOBECODEBANC", t = "AABC"
    Output: "ADOBECODEBA"
    Explanation:
        We need 2 'A's, 1 'B', and 1 'C'.
        "ADOBECODEBA" contains: A, D, O, B, E, C, O, D, E, B, A
        Which has: 2 'A's ✓, 2 'B's ✓, 1 'C' ✓

Example 5:
    Input: s = "ab", t = "b"
    Output: "b"
    Explanation:
        The minimum window is just "b" at index 1.

Example 6:
    Input: s = "bba", t = "ab"
    Output: "ba"
    Explanation:
        The window "ba" (indices 1-2) contains both 'a' and 'b'.

Understanding the Problem:
--------------------------
This is a classic sliding window problem with two pointers!

Key insight: We need to find the smallest window in s that contains all characters 
of t. We use:
1. A frequency map to track required characters from t
2. A sliding window with left and right pointers
3. Expand right to include characters, contract left to minimize window

The Challenge:
--------------
- Track which characters we need and how many
- Know when we have a valid window (all required characters present)
- Efficiently shrink the window while maintaining validity
- Track the minimum window found

Approach: Sliding Window with Two Hash Maps
--------------------------------------------
1. Create a frequency map for characters in t (what we need)
2. Use a sliding window with left and right pointers on s
3. Expand right pointer to include more characters
4. When we have a valid window, try to shrink from left
5. Track the minimum valid window

Algorithm Steps:
----------------
1. Edge cases:
   - If s is empty or t is empty, return ""
   - If len(t) > len(s), return "" (impossible)

2. Create frequency maps:
   - t_freq: frequency of each character in t (what we NEED)
   - window_freq: frequency of characters in current window (what we HAVE)

3. Initialize:
   - left = 0, right = 0
   - required = number of unique characters in t
   - formed = 0 (number of unique characters with desired frequency)
   - min_len = infinity, min_window = ""

4. Sliding window:
   - Expand right pointer:
     * Add s[right] to window_freq
     * If window_freq[s[right]] == t_freq[s[right]], increment formed
   
   - While formed == required (valid window):
     * Update min_window if current window is smaller
     * Try to shrink from left:
       - Remove s[left] from window_freq
       - If window_freq[s[left]] < t_freq[s[left]], decrement formed
       - Move left pointer right

5. Return min_window

Visual Example:
---------------
s = "ADOBECODEBANC", t = "ABC"

t_freq = {'A': 1, 'B': 1, 'C': 1}
required = 3 (need 3 unique characters satisfied)

Step-by-step:
                    ADOBECODEBANC
                    L
                    R

Expand R until valid window:
    R=0: 'A' → window={'A':1}, formed=1
    R=1: 'D' → window={'A':1,'D':1}, formed=1
    R=2: 'O' → window={'A':1,'D':1,'O':1}, formed=1
    R=3: 'B' → window={'A':1,'D':1,'O':1,'B':1}, formed=2
    R=4: 'E' → window={'A':1,'D':1,'O':1,'B':1,'E':1}, formed=2
    R=5: 'C' → window={'A':1,'D':1,'O':1,'B':1,'E':1,'C':1}, formed=3 ✓
    
    Valid window found: "ADOBEC" (length 6)
    
    Try to shrink from left:
    L=0→1: Remove 'A' → formed=2 (no longer valid)
    
Continue expanding R:
    R=6: 'O' → formed still 2
    R=7: 'D' → formed still 2
    R=8: 'E' → formed still 2
    R=9: 'B' → formed still 2
    R=10: 'A' → window={'A':1,...}, formed=3 ✓
    
    Valid window: "DOBECODEBA" - but wait, let me recalculate...
    
    Actually, window is s[1:11] = "DOBECODEBA"? No, we need to track properly.
    
Let me redo with proper tracking:
    After shrinking at R=5, L=1, window = "DOBEC" (no 'A', invalid)
    
    R=6,7,8,9: Still no 'A', keep expanding
    R=10: 'A' added → formed=3 ✓
    Window = s[1:11] = "DOBECODEBA" (length 10)
    
    Shrink: L=1→2: Remove 'D' → still valid
    L=2→3: Remove 'O' → still valid
    L=3→4: Remove 'B' → formed=2 (invalid, only 1 'B' was in t, but we removed it)
    
    Hmm, this needs more careful tracking. The window from L=1 to R=10 is:
    "OBECODEBA" after removing D at L=1... 
    
Let me simplify the key points:

The algorithm finds progressively smaller windows:
- First valid: "ADOBEC" (6)
- Later valid: "CODEBA" (6)  
- Even later: "BANC" (4) ← minimum!

Pseudocode:
-----------
def min_window(s, t):
    if not s or not t or len(s) < len(t):
        return ""
    
    # Count characters needed from t
    t_freq = Counter(t)
    required = len(t_freq)  # Unique chars we need
    
    # Sliding window
    window_freq = defaultdict(int)
    formed = 0  # Unique chars in window with required count
    
    left = 0
    min_len = float('inf')
    result = ""
    
    for right in range(len(s)):
        # Add character from right
        char = s[right]
        window_freq[char] += 1
        
        # Check if this char's count matches required count
        if char in t_freq and window_freq[char] == t_freq[char]:
            formed += 1
        
        # Try to shrink window while valid
        while formed == required:
            # Update result if smaller window found
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            # Remove from left
            left_char = s[left]
            window_freq[left_char] -= 1
            if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                formed -= 1
            left += 1
    
    return result

Key Insights:
-------------
1. Use TWO frequency maps: one for t (required), one for window (current)
2. Track "formed" = number of characters that have met their required count
3. When formed == required, we have a valid window
4. Shrink from left to find minimum while maintaining validity
5. The "formed" counter avoids comparing full frequency maps each time

Optimization with "formed" counter:
-----------------------------------
Instead of comparing window_freq == t_freq each time (O(26) or O(52)):
- Track how many unique characters have satisfied their frequency requirement
- When formed == len(t_freq), the window is valid
- This makes the check O(1)!

Edge Cases to Consider:
-----------------------
1. Empty s or t: return ""
2. t longer than s: return "" (impossible)
3. t has duplicates: must have at least that many in window
4. s equals t: return s
5. t is single character: find first occurrence
6. No valid window exists: return ""
7. Multiple valid windows of same minimum length: return any (leftmost)

Common Pitfalls:
----------------
1. Not handling duplicate characters in t correctly
2. Off-by-one errors in window boundaries
3. Not properly decrementing formed when shrinking
4. Forgetting to check if character is in t_freq before comparing counts
5. Returning wrong indices (remember substring is s[left:right+1])

Why Two Pointers / Sliding Window Works:
-----------------------------------------
- Right pointer expands to find valid windows
- Left pointer contracts to minimize window size
- We never need to move left backwards (monotonic)
- Each character is processed at most twice (add + remove)
- Total time: O(m + n) where m = len(s), n = len(t)

Follow-up Questions:
--------------------
1. What if we needed to return all minimum windows? (Store all with min length)
2. What if order mattered? (Different problem - subsequence matching)
3. Can you solve it with O(1) extra space? (Not really, need to track frequencies)
4. What if s and t can have Unicode characters? (Use hash map, not array)

Expected Time Complexity: O(m + n)
    - O(n) to build t_freq
    - O(m) to slide window (each char added/removed at most once)
    
Expected Space Complexity: O(m + n)
    - O(n) for t_freq (at most 52 unique chars for letters)
    - O(m) for window_freq in worst case
    - Can be O(1) if we count only letters (fixed 52 size)
"""


def min_window(s: str, t: str) -> str:
    """
    Find the minimum window substring of s that contains all characters of t.
    
    Args:
        s: The source string to search in
        t: The target string containing characters we need
    
    Returns:
        The minimum window substring, or "" if no valid window exists
    
    Example:
        >>> min_window("ADOBECODEBANC", "ABC")
        "BANC"
        >>> min_window("a", "a")
        "a"
        >>> min_window("a", "aa")
        ""
    """
    # Write your solution here
    from collections import Counter, defaultdict
    if not s or not t or len(s) < len(t):
        return ""
    t_freq = Counter(t)
    required = len(t_freq)
    window_freq = defaultdict(int)
    formed = 0
    left = 0
    min_len = float('inf')
    result = ""
    for right in range(len(s)):
        char = s[right]
        window_freq[char] += 1
        if char in t_freq and window_freq[char] == t_freq[char]:
            formed += 1
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            left_char = s[left]
            window_freq[left_char] -= 1
            if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                formed -= 1
            left += 1
    return result



# Test cases
if __name__ == "__main__":
    # Test case 1: Basic example
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(f"Test 1: s = '{s1}', t = '{t1}'")
    result1 = min_window(s1, t1)
    print(f"Output: '{result1}'")
    print(f"Expected: 'BANC'\n")
    
    # Test case 2: Exact match single character
    s2 = "a"
    t2 = "a"
    print(f"Test 2: s = '{s2}', t = '{t2}'")
    result2 = min_window(s2, t2)
    print(f"Output: '{result2}'")
    print(f"Expected: 'a'\n")
    
    # Test case 3: Impossible - not enough characters
    s3 = "a"
    t3 = "aa"
    print(f"Test 3: s = '{s3}', t = '{t3}'")
    result3 = min_window(s3, t3)
    print(f"Output: '{result3}'")
    print(f"Expected: ''\n")
    
    # Test case 4: Duplicate characters in t
    s4 = "ADOBECODEBANC"
    t4 = "AABC"
    print(f"Test 4: s = '{s4}', t = '{t4}'")
    result4 = min_window(s4, t4)
    print(f"Output: '{result4}'")
    print(f"Expected: 'ADOBECODEBA'\n")
    
    # Test case 5: Target at end
    s5 = "ab"
    t5 = "b"
    print(f"Test 5: s = '{s5}', t = '{t5}'")
    result5 = min_window(s5, t5)
    print(f"Output: '{result5}'")
    print(f"Expected: 'b'\n")
    
    # Test case 6: Overlapping characters
    s6 = "bba"
    t6 = "ab"
    print(f"Test 6: s = '{s6}', t = '{t6}'")
    result6 = min_window(s6, t6)
    print(f"Output: '{result6}'")
    print(f"Expected: 'ba'\n")
    
    # Test case 7: All same characters
    s7 = "aaaaaaa"
    t7 = "aaa"
    print(f"Test 7: s = '{s7}', t = '{t7}'")
    result7 = min_window(s7, t7)
    print(f"Output: '{result7}'")
    print(f"Expected: 'aaa'\n")
    
    # Test case 8: No valid window
    s8 = "abc"
    t8 = "d"
    print(f"Test 8: s = '{s8}', t = '{t8}'")
    result8 = min_window(s8, t8)
    print(f"Output: '{result8}'")
    print(f"Expected: ''\n")
    
    # Test case 9: t equals s
    s9 = "abc"
    t9 = "abc"
    print(f"Test 9: s = '{s9}', t = '{t9}'")
    result9 = min_window(s9, t9)
    print(f"Output: '{result9}'")
    print(f"Expected: 'abc'\n")
    
    # Test case 10: Window at the beginning
    s10 = "abcdef"
    t10 = "abc"
    print(f"Test 10: s = '{s10}', t = '{t10}'")
    result10 = min_window(s10, t10)
    print(f"Output: '{result10}'")
    print(f"Expected: 'abc'\n")
    
    # Test case 11: Mixed case
    s11 = "aAbBcC"
    t11 = "ABC"
    print(f"Test 11: s = '{s11}', t = '{t11}'")
    result11 = min_window(s11, t11)
    print(f"Output: '{result11}'")
    print(f"Expected: 'AbBcC' or similar containing A, B, C\n")
    
    # Test case 12: Long string with short target
    s12 = "aaflslflsldkalskaaa"
    t12 = "aaa"
    print(f"Test 12: s = '{s12}', t = '{t12}'")
    result12 = min_window(s12, t12)
    print(f"Output: '{result12}'")
    print(f"Expected: 'aaa'\n")
    
    # Test case 13: Empty strings
    s13 = ""
    t13 = "a"
    print(f"Test 13: s = '{s13}', t = '{t13}'")
    result13 = min_window(s13, t13)
    print(f"Output: '{result13}'")
    print(f"Expected: ''\n")
    
    # Test case 14: t longer than s
    s14 = "ab"
    t14 = "abc"
    print(f"Test 14: s = '{s14}', t = '{t14}'")
    result14 = min_window(s14, t14)
    print(f"Output: '{result14}'")
    print(f"Expected: ''\n")
