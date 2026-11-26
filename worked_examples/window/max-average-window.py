"""Find the greatest average among exact-width windows of an integer list."""

from itertools import accumulate


def _check_width(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("width must be between 1 and the list length")


def baseline(nums, k):
    """O((n-k+1)*k) time, O(1) auxiliary space."""
    _check_width(nums, k)
    best = None
    for left in range(len(nums) - k + 1):
        total = 0
        for i in range(left, left + k):
            total += nums[i]
        if best is None or total > best:
            best = total
    return best / k


def pythonic(nums, k):
    """O(n) time and O(n) auxiliary space for prefix totals."""
    _check_width(nums, k)
    prefix = list(accumulate(nums, initial=0))
    best = max(prefix[end] - prefix[end - k] for end in range(k, len(prefix)))
    return best / k


def optimized(nums, k):
    """O(n) time and O(1) auxiliary space; no initial slice."""
    _check_width(nums, k)
    total = sum(nums[i] for i in range(k))
    best = total
    for right in range(k, len(nums)):
        total += nums[right] - nums[right - k]
        best = max(best, total)
    return best / k


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve([6, -8, 11, 0, 9], 3) == 20 / 3
        assert solve([-4, -7, -3, -2], 2) == -2.5
        assert solve([7], 1) == 7.0
        assert solve([6, -2, 2], 3) == 2.0
        for k in (0, 3):
            try:
                solve([1, 2], k)
            except ValueError:
                pass
            else:
                raise AssertionError("an invalid width should be rejected")
