"""Search Insert Position

Problem:
Find the first index in a sorted list whose value is at least the target.
Duplicates are allowed. Return the length if the target belongs after every
item.

Examples:
- [2, 4, 4, 8], target 4 returns 1.
- [2, 4], target 9 returns 2.

Approaches:
- Baseline: Scan for the first qualifying value.
- Python / standard library: Use bisect_left.
- Optimized: Implement lower-bound search.
"""

from __future__ import annotations

from bisect import bisect_left


def baseline(values: list[int], target: int) -> int:
    for index in range(len(values)):
        if values[index] >= target:
            return index
    return len(values)


def python_bisect(values: list[int], target: int) -> int:
    return bisect_left(values, target)


def optimized(values: list[int], target: int) -> int:
    low, high = 0, len(values)
    while low < high:
        mid = (low + high) // 2
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == "__main__":
    for lower_bound in baseline, python_bisect, optimized:
        assert lower_bound([], 4) == 0
        assert lower_bound([2, 4, 4, 4, 8], 4) == 1
        assert lower_bound([2, 4, 8], 6) == 2
        assert lower_bound([2, 4, 8], 0) == 0
        assert lower_bound([2, 4, 8], 9) == 3
