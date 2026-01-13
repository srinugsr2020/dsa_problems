"""
Reverse String Problem (Two Pointers Approach)

Problem Statement:
------------------
Write a function that reverses a string. The input string is given as an array of 
characters 's'.

You must do this by modifying the input array in-place with O(1) extra memory.

Important Notes:
----------------
1. The input is given as a list/array of characters (not a string)
2. Must modify the array in-place (no return value needed)
3. O(1) extra space - cannot create a new array
4. Each character is a single character string

Constraints:
------------
- 1 <= s.length <= 10^5
- s[i] is a printable ASCII character

Examples:
---------
Example 1:
    Input: s = ["h", "e", "l", "l", "o"]
    Output: ["o", "l", "l", "e", "h"]
    Explanation: Reverse the entire array.

Example 2:
    Input: s = ["H", "a", "n", "n", "a", "h"]
    Output: ["h", "a", "n", "n", "a", "H"]
    Explanation: The reversed string is a palindrome!

Example 3:
    Input: s = ["A"]
    Output: ["A"]
    Explanation: Single character remains the same.

Example 4:
    Input: s = ["A", "B"]
    Output: ["B", "A"]
    Explanation: Simple two-character swap.

Example 5:
    Input: s = ["a", "b", "c", "d", "e", "f"]
    Output: ["f", "e", "d", "c", "b", "a"]
    Explanation: All characters reversed in order.

Visual Transformation:
----------------------
Input:  ["h", "e", "l", "l", "o"]
         ↓              ↓
Swap 1: ["o", "e", "l", "l", "h"]  (swap indices 0 and 4)
               ↓    ↓
Swap 2: ["o", "l", "l", "e", "h"]  (swap indices 1 and 3)
                  ↓
Done:   ["o", "l", "l", "e", "h"]  (middle element stays)

Approach: Two Pointers (Opposite Direction)
--------------------------------------------
This is a classic opposite-direction two-pointers problem.

Algorithm Steps:
1. Initialize two pointers: left at the start (0) and right at the end (len(s)-1)
2. While left < right:
   a. Swap the characters at left and right positions
   b. Move left pointer forward (left += 1)
   c. Move right pointer backward (right -= 1)
3. When left >= right, all swaps are complete

Why This Works:
---------------
- Start from both ends and work toward the middle
- Each swap puts one character from the end at the beginning and vice versa
- Stop when pointers meet or cross in the middle
- For odd-length arrays, the middle character doesn't need to move
- For even-length arrays, all characters get swapped

Key Insights:
-------------
1. Number of swaps needed: len(s) // 2
2. The middle element (if odd length) stays in place
3. Each iteration reduces the unsolved portion by 2 elements
4. In-place swapping means no extra array needed

Swapping Techniques in Python:
-------------------------------
# Method 1: Tuple unpacking (Pythonic)
s[left], s[right] = s[right], s[left]

# Method 2: Temporary variable (traditional)
temp = s[left]
s[left] = s[right]
s[right] = temp

# Method 3: XOR swap (for integers, not recommended for strings)
# Not applicable here since we're swapping character strings

Edge Cases to Consider:
-----------------------
- Single character array (no swap needed)
- Two character array (single swap)
- Empty array (shouldn't happen per constraints)
- Array with all same characters (still needs reversing)
- Palindrome array (result looks the same)

Follow-up Questions:
--------------------
1. What if the input was a string instead of a list? How would you convert it?
2. How would you reverse only a portion of the array (from index i to j)?
3. Can you reverse the array using recursion? What would be the time/space complexity?
4. How would you reverse words in a sentence while keeping word order?

Expected Time Complexity: O(n) where n is the length of the array
Expected Space Complexity: O(1) - only using two pointer variables
"""


def reverse_string(s: list[str]) -> None:
    """
    Reverse a string represented as a list of characters in-place.
    
    Args:
        s: List of single-character strings to reverse in-place
    
    Returns:
        None (modifies s in-place)
    
    Example:
        >>> s = ["h", "e", "l", "l", "o"]
        >>> reverse_string(s)
        >>> s
        ["o", "l", "l", "e", "h"]
    """
    i , j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


# Test cases
if __name__ == "__main__":
    # Test case 1: Classic example
    s1 = ["h", "e", "l", "l", "o"]
    print(f"Test 1: Before = {s1}")
    reverse_string(s1)
    print(f"        After  = {s1}")
    print(f"        Expected: ['o', 'l', 'l', 'e', 'h']\n")
    
    # Test case 2: Palindrome
    s2 = ["H", "a", "n", "n", "a", "h"]
    print(f"Test 2: Before = {s2}")
    reverse_string(s2)
    print(f"        After  = {s2}")
    print(f"        Expected: ['h', 'a', 'n', 'n', 'a', 'H']\n")
    
    # Test case 3: Single character
    s3 = ["A"]
    print(f"Test 3: Before = {s3}")
    reverse_string(s3)
    print(f"        After  = {s3}")
    print(f"        Expected: ['A']\n")
    
    # Test case 4: Two characters
    s4 = ["A", "B"]
    print(f"Test 4: Before = {s4}")
    reverse_string(s4)
    print(f"        After  = {s4}")
    print(f"        Expected: ['B', 'A']\n")
    
    # Test case 5: Even length
    s5 = ["a", "b", "c", "d", "e", "f"]
    print(f"Test 5: Before = {s5}")
    reverse_string(s5)
    print(f"        After  = {s5}")
    print(f"        Expected: ['f', 'e', 'd', 'c', 'b', 'a']\n")
    
    # Test case 6: Odd length
    s6 = ["a", "b", "c", "d", "e"]
    print(f"Test 6: Before = {s6}")
    reverse_string(s6)
    print(f"        After  = {s6}")
    print(f"        Expected: ['e', 'd', 'c', 'b', 'a']\n")
    
    # Test case 7: All same characters
    s7 = ["a", "a", "a", "a"]
    print(f"Test 7: Before = {s7}")
    reverse_string(s7)
    print(f"        After  = {s7}")
    print(f"        Expected: ['a', 'a', 'a', 'a']\n")
    
    # Test case 8: Numbers as strings
    s8 = ["1", "2", "3", "4", "5"]
    print(f"Test 8: Before = {s8}")
    reverse_string(s8)
    print(f"        After  = {s8}")
    print(f"        Expected: ['5', '4', '3', '2', '1']\n")
    
    # Test case 9: Mixed case
    s9 = ["A", "b", "C", "d", "E"]
    print(f"Test 9: Before = {s9}")
    reverse_string(s9)
    print(f"        After  = {s9}")
    print(f"        Expected: ['E', 'd', 'C', 'b', 'A']\n")
    
    # Test case 10: Special characters
    s10 = ["!", "@", "#", "$", "%"]
    print(f"Test 10: Before = {s10}")
    reverse_string(s10)
    print(f"         After  = {s10}")
    print(f"         Expected: ['%', '$', '#', '@', '!']\n")
    
    # Test case 11: Spaces included
    s11 = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
    print(f"Test 11: Before = {s11}")
    reverse_string(s11)
    print(f"         After  = {s11}")
    print(f"         Expected: ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']\n")
    
    # Test case 12: Three characters
    s12 = ["x", "y", "z"]
    print(f"Test 12: Before = {s12}")
    reverse_string(s12)
    print(f"         After  = {s12}")
    print(f"         Expected: ['z', 'y', 'x']\n")
