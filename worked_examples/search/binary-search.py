"""Find a target in a strictly increasing list, or return -1."""

from __future__ import annotations

from bisect import bisect_left


def baseline(values: list[int], target: int) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def python_index(values: list[int], target: int) -> int:
    try:
        return values.index(target)
    except ValueError:
        return -1


def optimized(values: list[int], target: int) -> int:
    low, high = 0, len(values)
    while low < high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid
    return -1


if __name__ == "__main__":
    for search in baseline, python_index, optimized:
        values = [-4, 0, 7, 11]
        for target in range(-5, 13):
            position = bisect_left(values, target)
            expected = position if position < len(values) and values[position] == target else -1
            assert search(values, target) == expected
        assert search([], 9) == -1
