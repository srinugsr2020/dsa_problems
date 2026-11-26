"""
Valid Palindrome Problem (Two Pointers Approach)

Problem Statement:
------------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and 
backward. Alphanumeric characters include letters and numbers.

Given a string 's', return True if it is a palindrome, or False otherwise.

Constraints:
------------
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters

Examples:
---------
Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: False
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: True
    Explanation: After removing non-alphanumeric characters, s becomes an empty string "".
                 Since an empty string reads the same forward and backward, it is a palindrome.

Example 4:
    Input: s = "A"
    Output: True
    Explanation: Single character is always a palindrome.

Example 5:
    Input: s = "0P"
    Output: False
    Explanation: "0p" is not a palindrome.

Example 6:
    Input: s = "ab_a"
    Output: True
    Explanation: After removing underscore, "aba" is a palindrome.

Hints:
------
1. Use two pointers: one at the start and one at the end of the string
2. Skip non-alphanumeric characters by moving pointers appropriately
3. Compare characters case-insensitively
4. Move both pointers toward the center
5. If pointers cross or meet, you've checked the entire string
6. Use built-in methods: isalnum() to check if a character is alphanumeric,
   and lower() to convert to lowercase

Expected Time Complexity: O(n) where n is the length of the string
Expected Space Complexity: O(1) - using two pointers without extra string storage
"""


def is_palindrome(s: str) -> bool:
    """
    Determine if a string is a palindrome after preprocessing.
    
    Args:
        s: A string that may contain uppercase, lowercase, numbers, and special characters
    
    Returns:
        True if the string is a palindrome after removing non-alphanumeric characters
        and converting to lowercase, False otherwise
    
    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
    """
    # Write your solution here
    left , right = 0, len(s) - 1
    if len(s) == 0 or len(s) == 1:
        return True
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        elif not s[right].isalnum():
            right -= 1
            continue
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True


# Test cases
if __name__ == "__main__":
    # Test case 1: Classic palindrome with mixed case and punctuation
    test1 = "A man, a plan, a canal: Panama"
    print(f"Test 1: s = \"{test1}\"")
    print(f"Output: {is_palindrome(test1)}")
    print(f"Expected: True\n")
    
    # Test case 2: Not a palindrome
    test2 = "race a car"
    print(f"Test 2: s = \"{test2}\"")
    print(f"Output: {is_palindrome(test2)}")
    print(f"Expected: False\n")
    
    # Test case 3: Empty/whitespace string
    test3 = " "
    print(f"Test 3: s = \"{test3}\"")
    print(f"Output: {is_palindrome(test3)}")
    print(f"Expected: True\n")
    
    # Test case 4: Single character
    test4 = "A"
    print(f"Test 4: s = \"{test4}\"")
    print(f"Output: {is_palindrome(test4)}")
    print(f"Expected: True\n")
    
    # Test case 5: Alphanumeric with special chars
    test5 = "0P"
    print(f"Test 5: s = \"{test5}\"")
    print(f"Output: {is_palindrome(test5)}")
    print(f"Expected: False\n")
    
    # Test case 6: Palindrome with underscores
    test6 = "ab_a"
    print(f"Test 6: s = \"{test6}\"")
    print(f"Output: {is_palindrome(test6)}")
    print(f"Expected: True\n")
    
    # Test case 7: Numbers and letters
    test7 = "A1b2B1a"
    print(f"Test 7: s = \"{test7}\"")
    print(f"Output: {is_palindrome(test7)}")
    print(f"Expected: True\n")
    
    # Test case 8: All special characters
    test8 = ".,!@#"
    print(f"Test 8: s = \"{test8}\"")
    print(f"Output: {is_palindrome(test8)}")
    print(f"Expected: True\n")
