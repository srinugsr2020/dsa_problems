"""Longest Substring with at Most k Distinct Characters

Problem:
Find the longest substring containing at most k different characters. A
substring must be contiguous. Return its length, or zero when the input string
is empty or k is not positive.

Examples:
- "aabaacc", k=2 -> 5.
- "abcbbba", k=2 -> 5.
- "abc", k=0 -> 0.

Approaches:
- Baseline: Restart the set at every left edge.
- Python / standard library: Evict the least recent last occurrence.
- Optimized: Shrink a frequency window.
"""

from collections import OrderedDict


def baseline(text, k):
    """Expected O(n²) time and O(min(d,k+1)) auxiliary space for k > 0."""
    if k <= 0:
        return 0
    best = 0
    for left in range(len(text)):
        seen = set()
        for right in range(left, len(text)):
            seen.add(text[right])
            if len(seen) > k:
                break
            best = max(best, right - left + 1)
    return best


def pythonic(text, k):
    """Expected O(n) time and O(min(d,k+1)) auxiliary space for k > 0."""
    if k <= 0:
        return 0
    last_seen = OrderedDict()
    left = best = 0
    for right, char in enumerate(text):
        last_seen[char] = right
        last_seen.move_to_end(char)
        if len(last_seen) > k:
            _, last_index = last_seen.popitem(last=False)
            left = last_index + 1
        best = max(best, right - left + 1)
    return best


def optimized(text, k):
    """Expected O(n) time and O(min(d,k+1)) auxiliary space for k > 0."""
    if k <= 0:
        return 0
    counts = {}
    left = best = 0
    for right, char in enumerate(text):
        counts[char] = counts.get(char, 0) + 1
        while len(counts) > k:
            outgoing = text[left]
            counts[outgoing] -= 1
            if counts[outgoing] == 0:
                del counts[outgoing]
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("aabaacc", 2) == 5
        assert solve("abcbbba", 2) == 5
        assert solve("😀😀ββ", 1) == 2
        assert solve("abc", 9) == 3
        assert solve("abc", 0) == solve("abc", -1) == solve("", 2) == 0
