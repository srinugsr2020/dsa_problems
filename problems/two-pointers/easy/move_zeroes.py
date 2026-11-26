"""Move Zeroes

Problem:
Modify an integer list so all zeroes are at the end and all other entries keep
their original relative order. Return None. The strict solution uses constant
auxiliary space.

Examples:
- [0, 4, 0, -2, 4, 0, 1] becomes [4, -2, 4, 1, 0, 0, 0].
- [0, 0] and [] are unchanged.

Approaches:
- Baseline: Remove and append.
- Python / standard library: Stable sort by zero status.
- Optimized: Compact and fill.
"""


def baseline(nums):
    """O(n²) time, O(1) algorithmic extra space: shift after each removal."""
    i = 0
    for _ in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
        else:
            i += 1


def pythonic(nums):
    """O(n log n) time, O(n) sort scratch: relax the strict space limit."""
    nums.sort(key=lambda value: value == 0)


def optimized(nums):
    """O(n) time and O(1) extra space: compact, then fill."""
    write = 0
    for value in nums:
        if value != 0:
            nums[write] = value
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        for values, expected in (
            ([0, 4, 0, -2, 4, 0, 1], [4, -2, 4, 1, 0, 0, 0]),
            ([0, 0], [0, 0]),
            ([6, -1], [6, -1]),
            ([], []),
        ):
            alias = values
            assert solve(values) is None
            assert alias == expected
