"""
Happy Number Problem

Problem Statement:
------------------
Write an algorithm to determine if a number 'n' is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a 
  cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if 'n' is a happy number, and false if not.

Constraints:
------------
- 1 <= n <= 2^31 - 1

Examples:
---------
Example 1:
    Input: n = 19
    Output: true
    Explanation:
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1

Example 2:
    Input: n = 2
    Output: false
    Explanation: The sequence is 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> ...
                 This loops forever without reaching 1.

Hints:
------
1. The key insight is detecting a cycle (infinite loop)
2. Use a hash set to track numbers we've already seen
3. If we see a number again, we're in a cycle -> return False
4. If we reach 1, it's a happy number -> return True
5. Alternative: Floyd's cycle detection (slow/fast pointer) works too

Expected Time Complexity: O(log n) per step, total depends on cycle length
Expected Space Complexity: O(log n) for the set (or O(1) with Floyd's algorithm)
"""


def is_happy(n: int) -> bool:
    """
    Determine if a number is a happy number using a hash set.
    
    Args:
        n: A positive integer
    
    Returns:
        True if n is a happy number, False otherwise
    
    Example:
        >>> is_happy(19)
        True
    """
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = _sum_of_squares(n)
    
    return n == 1


def _sum_of_squares(n: int) -> int:
    """
    Helper function to calculate the sum of squares of digits.
    
    Args:
        n: A positive integer
    
    Returns:
        Sum of squares of all digits in n
    """
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def is_happy_floyd(n: int) -> bool:
    """
    Alternative approach using Floyd's cycle detection (O(1) space).
    
    Uses slow and fast pointers to detect cycles without extra storage.
    
    Args:
        n: A positive integer
    
    Returns:
        True if n is a happy number, False otherwise
    """
    slow = n
    fast = _sum_of_squares(n)
    
    while fast != 1 and slow != fast:
        slow = _sum_of_squares(slow)
        fast = _sum_of_squares(_sum_of_squares(fast))
    
    return fast == 1


# Test cases
if __name__ == "__main__":
    # Test case 1: Happy number
    n1 = 19
    print(f"Test 1: n = {n1}")
    print(f"Output: {is_happy(n1)}")
    print(f"Expected: True\n")
    
    # Test case 2: Not a happy number
    n2 = 2
    print(f"Test 2: n = {n2}")
    print(f"Output: {is_happy(n2)}")
    print(f"Expected: False\n")
    
    # Test case 3: n = 1 (trivially happy)
    n3 = 1
    print(f"Test 3: n = {n3}")
    print(f"Output: {is_happy(n3)}")
    print(f"Expected: True\n")
    
    # Test case 4: Another happy number
    n4 = 7
    print(f"Test 4: n = {n4}")
    print(f"Output: {is_happy(n4)}")
    print(f"Expected: True\n")
    
    # Test case 5: Not happy
    n5 = 116
    print(f"Test 5: n = {n5}")
    print(f"Output: {is_happy(n5)}")
    print(f"Expected: False\n")
    
    # Test Floyd's algorithm
    print("--- Testing Floyd's cycle detection approach ---")
    print(f"Floyd Test 1 (n=19): {is_happy_floyd(19)}")
    print(f"Floyd Test 2 (n=2): {is_happy_floyd(2)}")
    print(f"Floyd Test 3 (n=7): {is_happy_floyd(7)}")
