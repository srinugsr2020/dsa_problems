"""Valid Anagram

Problem:
Decide whether two strings have exactly the same character counts. Case matters.

Examples:
- "ÉaÉ" and "ÉÉa" -> True
- "aaB" and "aBB" -> False

Approaches:
- Baseline: Sort and compare.
- Python / standard library: Compare two Counters.
- Optimized: Consume one frequency table.
"""

from collections import Counter


def baseline(first, second):
    return sorted(first) == sorted(second)


def pythonic(first, second):
    return Counter(first) == Counter(second)


def optimized(first, second):
    if len(first) != len(second):
        return False
    remaining = {}
    for c in first:
        remaining[c] = remaining.get(c, 0) + 1
    for c in second:
        count = remaining.get(c, 0)
        if count == 0:
            return False
        if count == 1:
            del remaining[c]
        else:
            remaining[c] = count - 1
    return True


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("ÉaÉ", "ÉÉa") and solve("", "")
        assert not solve("aaB", "aBB") and not solve("a", "A")
        assert not solve("", "x")
