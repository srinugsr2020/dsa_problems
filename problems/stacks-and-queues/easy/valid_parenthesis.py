"""
Valid Parentheses (LeetCode #20)

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
    Input: s = "()"
    Output: True
    
    Input: s = "()[]{}"
    Output: True
    
    Input: s = "(]"
    Output: False
    
    Input: s = "([])"
    Output: True

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only '()[]{}'
"""

from typing import List


def is_valid(s: str) -> bool:
    """
    Check if parentheses are valid using a stack.
    
    Approach:
    - Use stack to track opening brackets
    - For closing bracket, check if it matches top of stack
    - Valid if stack is empty at the end
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
    ]
    
    for i, (s, expected) in enumerate(test_cases):
        result = is_valid(s)
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} is_valid('{s}') = {result}, expected {expected}")
