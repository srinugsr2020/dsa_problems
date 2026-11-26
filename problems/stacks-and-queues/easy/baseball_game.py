"""
Baseball Game (LeetCode #682)

Problem:
You are keeping the scores for a baseball game with strange rules.
At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith
operation you must apply to the record and is one of the following:
- An integer x: Record a new score of x.
- '+': Record a new score that is the sum of the previous two scores.
- 'D': Record a new score that is double of the previous score.
- 'C': Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

Examples:
    Input: ops = ["5","2","C","D","+"]
    Output: 30
    Explanation:
    "5" - Add 5 to the record, record is now [5].
    "2" - Add 2 to the record, record is now [5, 2].
    "C" - Invalidate and remove the previous score, record is now [5].
    "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
    "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
    The total sum is 5 + 10 + 15 = 30.

    Input: ops = ["5","-2","4","C","D","9","+","+"]
    Output: 27

    Input: ops = ["1","C"]
    Output: 0

Constraints:
    - 1 <= operations.length <= 1000
    - operations[i] is "C", "D", "+", or a string representing an integer
      in the range [-3 * 10^4, 3 * 10^4].
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
