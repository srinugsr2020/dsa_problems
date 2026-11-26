"""Find a zero-based pair in sorted integers; return None if absent."""

from bisect import bisect_left


def baseline(nums, target):
    """O(n²) time and O(1) extra space."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def pythonic(nums, target):
    """O(n log n) time and O(1) extra space; bisect bounds do not copy."""
    for i, value in enumerate(nums):
        complement = target - value
        j = bisect_left(nums, complement, lo=i + 1)
        if j < len(nums) and nums[j] == complement:
            return [i, j]
    return None


def optimized(nums, target):
    """O(n) time and O(1) extra space."""
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return None


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve([-9, -4, 3, 8], -6) == [0, 2]
        assert solve([0, 2, 2, 9], 4) == [1, 2]
        assert solve([2, 6, 9], 4) is None
        assert solve([], 0) is None
