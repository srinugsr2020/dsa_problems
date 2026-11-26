"""Maximum Vowels in a Fixed-Length Substring

Problem:
Find the largest number of case-insensitive ASCII vowels (a, e, i, o, u) in an
exact-width substring. Require 0 <= k <= len(text); k=0 returns zero.

Examples:
- "bxAIox", k=3 -> 3.
- "àbEé", k=4 -> 1.
- "yxYz", k=2 -> 0.

Approaches:
- Baseline: Count each window separately.
- Python / standard library: Accumulate vowel indicators.
- Optimized: Roll one count.
"""

from itertools import accumulate

VOWELS = frozenset("aeiouAEIOU")


def _check_width(text, k):
    if not 0 <= k <= len(text):
        raise ValueError("width must be between 0 and the text length")


def baseline(text, k):
    """O((n-k+1)*k) time for k > 0, O(1) auxiliary space."""
    _check_width(text, k)
    if k == 0:
        return 0
    best = 0
    for left in range(len(text) - k + 1):
        count = 0
        for i in range(left, left + k):
            count += text[i] in VOWELS
        best = max(best, count)
    return best


def pythonic(text, k):
    """O(n) time and O(n) auxiliary space for prefix counts."""
    _check_width(text, k)
    if k == 0:
        return 0
    prefix = list(accumulate((char in VOWELS for char in text), initial=0))
    return max(prefix[end] - prefix[end - k] for end in range(k, len(prefix)))


def optimized(text, k):
    """O(n) time and O(1) auxiliary space; stop at the width bound."""
    _check_width(text, k)
    count = sum(text[i] in VOWELS for i in range(k))
    best = count
    for i in range(k, len(text)):
        if best == k:
            break
        count += (text[i] in VOWELS) - (text[i - k] in VOWELS)
        best = max(best, count)
    return best


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("bxAIox", 3) == 3
        assert solve("àbEé", 4) == 1
        assert solve("yxYz", 2) == 0
        assert solve("", 0) == solve("AAAA", 0) == 0
        try:
            solve("a", 2)
        except ValueError:
            pass
        else:
            raise AssertionError("an oversized window should be rejected")
