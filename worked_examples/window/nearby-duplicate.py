"""Check for distinct equal indices at distance at most k, with k >= 0."""


def baseline(nums, k):
    """O(n*(1 + min(n,k))) time, O(1) auxiliary space."""
    for right, value in enumerate(nums):
        for left in range(max(0, right - k), right):
            if value == nums[left]:
                return True
    return False


def pythonic(nums, k):
    """Expected O(n) time, O(d) auxiliary space for d distinct input values."""
    last_seen = {}
    for i, value in enumerate(nums):
        previous = last_seen.get(value)
        if previous is not None and i - previous <= k:
            return True
        last_seen[value] = i
    return False


def optimized(nums, k):
    """Expected O(n) time, O(min(n,k)) auxiliary space for positive k."""
    if k <= 0:
        return False
    eligible = set()
    for i, value in enumerate(nums):
        if i > k:
            eligible.remove(nums[i - k - 1])
        if value in eligible:
            return True
        eligible.add(value)
    return False


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve([7, -1, 2, 7], 3)
        assert not solve([7, -1, 2, 7], 2)
        assert solve([7, -1, 2, 7, 7], 1)
        assert not solve([7, 7], 0)
        assert not solve([], 999)
