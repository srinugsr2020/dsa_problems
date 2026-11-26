"""Remove Duplicates from a Sorted Array

Problem:
Compact a nondecreasing integer list in place so its leading entries are its
distinct values in order. Return the length of that prefix. An empty list
returns zero, and suffix values do not matter.

Examples:
- [-5, -5, -2, 3, 3, 9] returns 4 and leaves [-5, -2, 3, 9] in the first four
  positions.
- [4, 4, 4] returns 1.

Approaches:
- Baseline: Scan the written prefix.
- Python / standard library: Use insertion-ordered keys.
- Optimized: Compare with the last retained value.
"""


def baseline(nums):
    """O(n²) time, O(1) extra space: search the compacted prefix."""
    size = 0
    for value in nums:
        for i in range(size):
            if nums[i] == value:
                break
        else:
            nums[size] = value
            size += 1
    return size


def pythonic(nums):
    """Expected O(n) time, O(u) extra space for u distinct integers."""
    unique = dict.fromkeys(nums)
    for i, value in enumerate(unique):
        nums[i] = value
    return len(unique)


def optimized(nums):
    """O(n) time, O(1) extra space: compare to the last retained value."""
    size = 0
    for value in nums:
        if size == 0 or value != nums[size - 1]:
            nums[size] = value
            size += 1
    return size


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        for values, expected in (
            ([-5, -5, -2, 3, 3, 9], [-5, -2, 3, 9]),
            ([4, 4, 4], [4]),
            ([-8, 0, 1], [-8, 0, 1]),
            ([], []),
        ):
            alias = values
            k = solve(values)
            assert k == len(expected) and alias[:k] == expected
