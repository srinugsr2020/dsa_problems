"""Compute trapped water above nonnegative heights of unit-width columns."""

from itertools import accumulate


def baseline(height):
    """O(n²) time, O(1) extra space: rescan the two sides."""
    total = 0
    for i, bar in enumerate(height):
        left_max = right_max = bar
        for j in range(i):
            left_max = max(left_max, height[j])
        for j in range(i + 1, len(height)):
            right_max = max(right_max, height[j])
        total += min(left_max, right_max) - bar
    return total


def pythonic(height):
    """O(n) time and O(n) extra space for right-side maxima."""
    left_levels = accumulate(height, max)
    right_levels = list(accumulate(reversed(height), max))
    return sum(
        min(left, right) - bar
        for left, right, bar in zip(left_levels, reversed(right_levels), height)
    )


def optimized(height):
    """O(n) time, O(1) extra space: settle the lower known boundary."""
    left, right = 0, len(height) - 1
    left_max = right_max = total = 0
    while left <= right:
        if left_max <= right_max:
            left_max = max(left_max, height[left])
            total += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total += right_max - height[right]
            right -= 1
    return total


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve([6, 0, 2, 1, 4]) == 9
        assert solve([2, 0, 2, 0, 2]) == 4
        assert solve([1, 5, 3, 0]) == 0
        assert solve([2, 0]) == solve([]) == 0
