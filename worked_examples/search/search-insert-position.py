"""Find the first index at which a value could be inserted before equals."""

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
