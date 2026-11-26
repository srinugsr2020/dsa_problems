"""Minimum Window Substring

Problem:
Return the shortest contiguous part of a source that covers all target
characters, including repetitions, with case-sensitive matching. Break ties by
earliest start. Return an empty string when the target is empty or no window
covers it.

Examples:
- "xcaabyybaca", target "aac" -> "caa".
- "abxxba", target "ab" -> "ab".
- "xay", target "aa" -> "".

Approaches:
- Baseline: Recheck counts as each start grows.
- Python / standard library: Check coverage by Counter subtraction.
- Optimized: Track the number of missing occurrences.
"""

from collections import Counter


def baseline(text, target):
    """Expected O(m + n²*d) time, O(d) auxiliary space excluding the result."""
    need = Counter(target)
    if not need:
        return ""
    best_start, best_width = 0, len(text) + 1
    for left in range(len(text)):
        have = {}
        for right in range(left, len(text)):
            char = text[right]
            if char in need:
                have[char] = have.get(char, 0) + 1
            if all(have.get(char, 0) >= count for char, count in need.items()):
                width = right - left + 1
                if width < best_width:
                    best_start, best_width = left, width
                break
    return "" if best_width > len(text) else text[best_start:best_start + best_width]


def pythonic(text, target):
    """Expected O(m + n*d) time and O(d) auxiliary space excluding the result."""
    need = Counter(target)
    if not need:
        return ""
    have = Counter()
    left = best_start = 0
    best_width = len(text) + 1
    for right, char in enumerate(text):
        if char in need:
            have[char] += 1
        while not (need - have):
            width = right - left + 1
            if width < best_width:
                best_start, best_width = left, width
            outgoing = text[left]
            if outgoing in need:
                have[outgoing] -= 1
            left += 1
    return "" if best_width > len(text) else text[best_start:best_start + best_width]


def optimized(text, target):
    """Expected O(n + m) time and O(d) auxiliary space excluding the result."""
    if not target:
        return ""
    deficit = Counter(target)
    missing = len(target)
    left = best_start = 0
    best_width = len(text) + 1
    for right, char in enumerate(text):
        if char in deficit:
            if deficit[char] > 0:
                missing -= 1
            deficit[char] -= 1
        while missing == 0:
            width = right - left + 1
            if width < best_width:
                best_start, best_width = left, width
            outgoing = text[left]
            if outgoing in deficit:
                deficit[outgoing] += 1
                if deficit[outgoing] > 0:
                    missing += 1
            left += 1
    return "" if best_width > len(text) else text[best_start:best_start + best_width]


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("xcaabyybaca", "aac") == "caa"
        assert solve("abxxba", "ab") == "ab"
        assert solve("xxA-a", "Aa") == "A-a"
        assert solve("xay", "aa") == ""
        assert solve("abc", "") == solve("", "a") == ""
