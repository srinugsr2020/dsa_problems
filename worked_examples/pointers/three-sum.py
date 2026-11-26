"""List distinct zero-sum value triples from distinct positions."""

from collections import Counter
from itertools import combinations_with_replacement


def baseline(nums):
    """Expected O(n³) time and O(r) extra space for r results."""
    seen = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    seen.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(triple) for triple in seen]


def pythonic(nums):
    """Expected O(n + d log d + d²) time and O(d) extra space."""
    counts = Counter(nums)
    out = []
    for a, b in combinations_with_replacement(sorted(counts), 2):
        c = -(a + b)
        if c < b:
            continue
        triple = (a, b, c)
        if all(counts[value] >= times for value, times in Counter(triple).items()):
            out.append(list(triple))
    return out


def optimized(nums):
    """O(n log n + n²) time, O(n) sorted-copy and sort scratch."""
    ordered = sorted(nums)
    out = []
    for i in range(len(ordered) - 2):
        a = ordered[i]
        if a > 0:
            break
        if i and a == ordered[i - 1]:
            continue
        left, right = i + 1, len(ordered) - 1
        while left < right:
            b, c = ordered[left], ordered[right]
            total = a + b + c
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                out.append([a, b, c])
                while left < right and ordered[left] == b:
                    left += 1
                while left < right and ordered[right] == c:
                    right -= 1
    return out


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        for values, expected in (
            ([3, -2, 1, -2, 0, -1, 0, 0], {(-2, -1, 3), (-1, 0, 1), (0, 0, 0)}),
            ([1, -2, -2], set()),
            ([1, 1, -2, 1], {(-2, 1, 1)}),
            ([], set()),
        ):
            original = values[:]
            out = solve(values)
            assert set(map(tuple, out)) == expected and len(out) == len(expected)
            assert values == original
