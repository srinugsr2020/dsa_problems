"""
Happy Number (LeetCode #202)

Problem:
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:
    - Starting with any positive integer, replace the number by the sum of 
      the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), 
      or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false otherwise.

Example 1:
    Input: n = 19
    Output: true
    Explanation:
        1² + 9² = 82
        8² + 2² = 68
        6² + 8² = 100
        1² + 0² + 0² = 1

Example 2:
    Input: n = 2
    Output: false
    Explanation: The sequence 2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
                 enters a cycle that doesn't include 1.

Constraints:
    - 1 <= n <= 2^31 - 1

Time Complexity: O(log n) - the number of digits determines iterations
Space Complexity: O(1) - using fast/slow pointers
"""


def is_happy(n: int) -> bool:
    """
    Determine if n is a happy number using Floyd's cycle detection.
    
    Key Insight:
        The sequence of sum of squares either:
        1. Reaches 1 (happy number)
        2. Enters a cycle (not happy)
        
        We can use fast/slow pointers to detect the cycle!
    
    Approach:
        - Slow pointer moves one step (one sum of squares)
        - Fast pointer moves two steps (two sums of squares)
        - If they meet and it's not 1, there's a cycle → not happy
        - If fast reaches 1, it's a happy number
    
    Args:
        n: The number to check
        
    Returns:
        True if n is a happy number, False otherwise
    """
    def get_next(num: int) -> int:
        """Calculate sum of squares of digits."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = n
    fast = get_next(n)
    
    # Continue until fast reaches 1 or slow catches up to fast
    while fast != 1 and slow != fast:
        slow = get_next(slow)           # Move 1 step
        fast = get_next(get_next(fast)) # Move 2 steps
    
    return fast == 1


def is_happy_hashset(n: int) -> bool:
    """
    Determine if n is a happy number using a hash set.
    
    Approach:
        - Track all numbers we've seen
        - If we see a number again, we're in a cycle → not happy
        - If we reach 1, it's a happy number
    
    Note: This uses O(log n) space for the hash set.
    
    Args:
        n: The number to check
        
    Returns:
        True if n is a happy number, False otherwise
    """
    def get_next(num: int) -> int:
        """Calculate sum of squares of digits."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1


def is_happy_math(n: int) -> bool:
    """
    Determine if n is a happy number using mathematical insight.
    
    Mathematical Insight:
        All unhappy numbers eventually reach the cycle:
        4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
        
        So we only need to check if we hit 4.
    
    Args:
        n: The number to check
        
    Returns:
        True if n is a happy number, False otherwise
    """
    def get_next(num: int) -> int:
        """Calculate sum of squares of digits."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    while n != 1 and n != 4:
        n = get_next(n)
    
    return n == 1


def get_happy_sequence(n: int, max_steps: int = 20) -> list:
    """
    Get the sequence of numbers in the happy number process.
    
    Useful for debugging and understanding the pattern.
    
    Args:
        n: The starting number
        max_steps: Maximum steps to trace
        
    Returns:
        List of numbers in the sequence
    """
    def get_next(num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    sequence = [n]
    seen = {n}
    
    for _ in range(max_steps):
        n = get_next(n)
        sequence.append(n)
        
        if n == 1 or n in seen:
            break
        seen.add(n)
    
    return sequence


# --------------------- Test Cases ---------------------

if __name__ == "__main__":
    # Test Case 1: Happy number 19
    print(f"Test 1 (n=19): {is_happy(19)}")  # Expected: True
    print(f"  Sequence: {get_happy_sequence(19)}")
    
    # Test Case 2: Not happy number 2
    print(f"Test 2 (n=2): {is_happy(2)}")  # Expected: False
    print(f"  Sequence: {get_happy_sequence(2)}")
    
    # Test Case 3: Happy number 1
    print(f"Test 3 (n=1): {is_happy(1)}")  # Expected: True
    
    # Test Case 4: Happy number 7
    print(f"Test 4 (n=7): {is_happy(7)}")  # Expected: True
    print(f"  Sequence: {get_happy_sequence(7)}")
    
    # Test Case 5: Not happy number 4 (cycle starter)
    print(f"Test 5 (n=4): {is_happy(4)}")  # Expected: False
    print(f"  Sequence: {get_happy_sequence(4)}")
    
    # Test Case 6: Using hash set approach
    print(f"Test 6 (HashSet, n=19): {is_happy_hashset(19)}")  # Expected: True
    print(f"Test 7 (HashSet, n=2): {is_happy_hashset(2)}")    # Expected: False
    
    # Test Case 8: Using math approach
    print(f"Test 8 (Math, n=19): {is_happy_math(19)}")  # Expected: True
    print(f"Test 9 (Math, n=2): {is_happy_math(2)}")    # Expected: False
    
    # Test Case 10: Large happy number
    print(f"Test 10 (n=100): {is_happy(100)}")  # Expected: True (1+0+0=1)
    
    # Test Case 11: Another happy number
    print(f"Test 11 (n=68): {is_happy(68)}")  # Expected: True
    print(f"  Sequence: {get_happy_sequence(68)}")
    
    print("\nAll tests passed!")
