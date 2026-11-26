"""First Unique Character

Problem:
Return the index of the first character that occurs exactly once, or -1.

Examples:
- "ééAaa" -> 2
- "abab" -> -1

Approaches:
- Baseline: Rescan for each candidate.
- Python / standard library: Counter then scan.
- Optimized: Ordered first positions.
"""

from collections import Counter


def baseline(text):
    return next((i for i, c in enumerate(text) if text.count(c) == 1), -1)


def pythonic(text):
    counts = Counter(text)
    return next((i for i, c in enumerate(text) if counts[c] == 1), -1)


def optimized(text):
    first = {}
    for i, c in enumerate(text):
        first[c] = -1 if c in first else i
    return next((i for i in first.values() if i >= 0), -1)


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("ééAaa") == 2
        assert solve("baabç") == 4
        assert solve("") == solve("abab") == -1
