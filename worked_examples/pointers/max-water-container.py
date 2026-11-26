"""Maximize (right - left) times the shorter nonnegative line height."""


def baseline(height):
    """O(n²) time, O(1) extra space."""
    best = 0
    for left in range(len(height)):
        for right in range(left + 1, len(height)):
            best = max(best, (right - left) * min(height[left], height[right]))
    return best


def pythonic(height):
    """O(n log n) time and O(n) sort/order storage."""
    eligible = sorted(range(len(height)), key=height.__getitem__, reverse=True)
    left, right = len(height), -1
    best = 0
    for i in eligible:
        left, right = min(left, i), max(right, i)
        best = max(best, (right - left) * height[i])
    return best


def optimized(height):
    """O(n) time and O(1) extra space."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        limit = min(height[left], height[right])
        best = max(best, (right - left) * limit)
        if height[left] == limit:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve([1, 9, 2, 7, 1]) == 14
        assert solve([4, 0, 0, 4]) == 12
        assert solve([0, 5, 0]) == 0
        assert solve([10]) == solve([]) == 0
