"""Sorted Squares

Problem:
Given nondecreasing integers, return a fresh nondecreasing list of their
squares, including duplicates. Do not mutate the input.

Examples:
- [-7, -4, 0, 4, 5] -> [0, 16, 16, 25, 49].
- [-8, -2, -2] -> [4, 4, 64].

Approaches:
- Baseline: Insert each square in order.
- Python / standard library: Sort a generator of squares.
- Optimized: Fill from the right.
"""


def baseline(nums):
    """O(n²) time, O(1) auxiliary space excluding output."""
    out = []
    for value in nums:
        square = value * value
        pos = len(out)
        while pos and out[pos - 1] > square:
            pos -= 1
        out.insert(pos, square)
    return out


def pythonic(nums):
    """O(n log n) time, O(n) worst-case sort scratch excluding output."""
    return sorted(value * value for value in nums)


def optimized(nums):
    """O(n) time, O(1) auxiliary space excluding output."""
    out = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for write in range(right, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            value = nums[left]
            left += 1
        else:
            value = nums[right]
            right -= 1
        out[write] = value * value
    return out


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        for values, expected in (
            ([-7, -4, 0, 4, 5], [0, 16, 16, 25, 49]),
            ([-8, -2, -2], [4, 4, 64]),
            ([0, 3], [0, 9]),
            ([], []),
        ):
            original = values[:]
            result = solve(values)
            assert result == expected and result is not values and values == original
