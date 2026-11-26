"""Baseball Game

Problem:
Start with an empty score list. Process the commands from left to right:
- An integer string (such as "5" or "-2") appends that score.
- "+" appends the sum of the last two scores.
- "D" appends twice the last score.
- "C" removes the last score.

Assume each command has enough prior scores. Return the sum of the scores
that are still on the list after the final command. There are 1 to 1,000
commands, and integer inputs range from -30,000 to 30,000.

Examples:
- ["5", "2", "C", "D", "+"] returns 30. After recording [5, 2], "C"
  leaves [5], "D" makes [5, 10], and "+" makes [5, 10, 15].
- ["1", "C"] returns 0: the only score is canceled.

Approach:
- Use a list as a stack, then use sum() to total the remaining scores.
"""

from typing import List


def cal_points(operations: List[str]) -> int:
    """
    Calculate final score using a stack.
    
    Approach:
    - Use stack to maintain valid scores
    - Process each operation accordingly
    - Sum all values in stack at the end
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    
    for op in operations:
        if op == 'C':
            stack.pop()
        elif op == 'D':
            stack.append(stack[-1] * 2)
        elif op == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    
    return sum(stack)


# Test cases
if __name__ == "__main__":
    test_cases = [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1", "C"], 0),
        (["1"], 1),
        (["5", "2", "+"], 14),  # 5 + 2 + 7 = 14
    ]
    
    for i, (ops, expected) in enumerate(test_cases):
        result = cal_points(ops)
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} cal_points({ops}) = {result}, expected {expected}")
