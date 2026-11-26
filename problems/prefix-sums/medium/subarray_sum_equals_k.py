"""Subarray Sum

Problem:
Count nonempty contiguous ranges whose sum is the target. Values may be negative
or zero.

Examples:
- [1, -1, 0], target 0 -> 3
- [0, 0, 0], target 0 -> 6

Approaches:
- Baseline: Extend each starting position.
- Python / standard library: Accumulate and count earlier prefixes.
- Optimized: Dense prefix counts when practical.
"""

from collections import Counter
from itertools import accumulate


def baseline(values, target):
    count = 0
    for start in range(len(values)):
        running = 0
        for end in range(start, len(values)):
            running += values[end]
            count += running == target
    return count


def pythonic(values, target):
    counts = Counter({0: 1})
    result = 0
    for prefix in accumulate(values):
        result += counts[prefix - target]
        counts[prefix] += 1
    return result


def optimized(values, target):
    low = high = 0
    for prefix in accumulate(values):
        low, high = min(low, prefix), max(high, prefix)
    width = high - low + 1
    if width > max(256, 2 * len(values)):
        return pythonic(values, target)
    counts = [0] * width
    counts[-low] = 1
    result = 0
    for prefix in accumulate(values):
        wanted = prefix - target
        if low <= wanted <= high:
            result += counts[wanted - low]
        counts[prefix - low] += 1
    return result


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve([0, 0, 0], 0) == 6 and solve([], 0) == 0
        assert solve([1, -1, 0], 0) == 3
        assert solve([1000, -1000, 2], 2) == 2
        assert solve([2, -1, 2], -7) == 0
