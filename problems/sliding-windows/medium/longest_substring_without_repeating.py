"""Longest Substring without Repeating Characters

Problem:
Find the longest substring in which no character occurs twice. The characters
must be consecutive; spaces count like any other character. Return the length,
or zero if the input is empty.

Examples:
- "abba" -> 2.
- "å βå!" -> 4.
- "a b c a" -> 3.

Approaches:
- Baseline: Search the growing substring.
- Python / standard library: Use set membership for each start.
- Optimized: Jump using last positions.
"""


def baseline(text):
    """O(n³) time, O(n) auxiliary space for a candidate slice."""
    best = 0
    for left in range(len(text)):
        for right in range(left, len(text)):
            if text[right] in text[left:right]:
                break
            best = max(best, right - left + 1)
    return best


def pythonic(text):
    """No direct built-in: use set membership. Expected O(n²) time, O(d) space."""
    best = 0
    for left in range(len(text)):
        seen = set()
        for right in range(left, len(text)):
            char = text[right]
            if char in seen:
                break
            seen.add(char)
        best = max(best, len(seen))
    return best


def optimized(text):
    """Expected O(n) time and O(d) auxiliary space for last indices."""
    last_seen = {}
    left = best = 0
    for right, char in enumerate(text):
        left = max(left, last_seen.get(char, -1) + 1)
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("abba") == 2  # The second a must not move left backward.
        assert solve("å βå!") == 4
        assert solve("a b c a") == 3
        assert solve("") == 0
