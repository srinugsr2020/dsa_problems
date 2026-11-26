"""Four Sum

Problem:
Return every unique nondecreasing quadruplet of integers that totals the target,
with each entry taken from a different input position. The result order does not
matter. Leave input unchanged.

Examples:
- [4, -2, 0, 5, -2, 1], target 1 -> [[-2, -2, 0, 5], [-2, -2, 1, 4]] in either
  order.
- [2, 2, 2, 2, 2], target 8 -> [[2, 2, 2, 2]].

Approaches:
- Baseline: Enumerate four positions.
- Python / standard library: Enumerate value multisets.
- Optimized: Sort and scan after two anchors.
"""

from collections import Counter
from itertools import combinations_with_replacement


def baseline(nums, target):
    """Expected O(n⁴) time, O(r) extra space for r results."""
    seen = set()
    n = len(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for last in range(k + 1, n):
                    quad = (nums[i], nums[j], nums[k], nums[last])
                    if sum(quad) == target:
                        seen.add(tuple(sorted(quad)))
    return [list(quad) for quad in seen]


def pythonic(nums, target):
    """Expected O(n + d log d + d⁴) time, O(d) extra space for d distinct values."""
    counts = Counter(nums)
    out = []
    for quad in combinations_with_replacement(sorted(counts), 4):
        if sum(quad) != target:
            continue
        if all(counts[value] >= times for value, times in Counter(quad).items()):
            out.append(list(quad))
    return out


def optimized(nums, target):
    """O(n log n + n³) time, O(n) copy and sort scratch, excluding output."""
    ordered = sorted(nums)
    n = len(ordered)
    out = []
    for i in range(n - 3):
        if i and ordered[i] == ordered[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and ordered[j] == ordered[j - 1]:
                continue
            remaining = target - ordered[i] - ordered[j]
            left, right = j + 1, n - 1
            while left < right:
                a, b = ordered[left], ordered[right]
                if a + b < remaining:
                    left += 1
                elif a + b > remaining:
                    right -= 1
                else:
                    out.append([ordered[i], ordered[j], a, b])
                    while left < right and ordered[left] == a:
                        left += 1
                    while left < right and ordered[right] == b:
                        right -= 1
    return out


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        for values, target, expected in (
            ([4, -2, 0, 5, -2, 1], 1, {(-2, -2, 0, 5), (-2, -2, 1, 4)}),
            ([2] * 5, 8, {(2, 2, 2, 2)}),
            ([-8, -8, -8], -32, set()),
            ([], 0, set()),
        ):
            original = values[:]
            out = solve(values, target)
            assert set(map(tuple, out)) == expected and len(out) == len(expected)
            assert values == original
