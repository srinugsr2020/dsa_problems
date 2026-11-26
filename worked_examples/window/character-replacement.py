"""Return the longest length repairable with at most k substitutions, k >= 0."""

from collections import Counter


def baseline(text, k):
    """Expected O(n²) time and O(d) auxiliary space for d distinct characters."""
    best = 0
    for left in range(len(text)):
        counts = {}
        most = 0
        for right in range(left, len(text)):
            char = text[right]
            counts[char] = counts.get(char, 0) + 1
            most = max(most, counts[char])
            width = right - left + 1
            if width - most > k:
                break
            best = max(best, width)
    return best


def pythonic(text, k):
    """Expected O(n*d) time, O(d) auxiliary space: recompute the live mode."""
    counts = Counter()
    left = best = 0
    for right, char in enumerate(text):
        counts[char] += 1
        while right - left + 1 - counts.most_common(1)[0][1] > k:
            outgoing = text[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
        best = max(best, right - left + 1)
    return best


def optimized(text, k):
    """Expected O(n) time, O(d) auxiliary space: keep the historical mode count."""
    counts = {}
    left = best = peak = 0
    for right, char in enumerate(text):
        counts[char] = counts.get(char, 0) + 1
        peak = max(peak, counts[char])
        # A stale peak may keep an invalid window, but cannot grow the record.
        while right - left + 1 - peak > k:
            counts[text[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("AAAABXYZ", 1) == 5
        assert solve("BBAABBB", 2) == 7
        assert solve("XAYZZZ", 0) == 3
        assert solve("aAa", 0) == 1
        assert solve("", 4) == 0
