"""Compact a sorted integer list; only the returned-length prefix matters."""


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
