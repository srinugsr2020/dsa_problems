"""Ignore ASCII punctuation, whitespace and case; keep digits."""

import re


def baseline(text):
    """O(n) time and O(n) auxiliary space for the normalized list."""
    normalized = []
    for char in text:
        if char.isalnum():
            normalized.append(char.lower())
    for i in range(len(normalized) // 2):
        if normalized[i] != normalized[-i - 1]:
            return False
    return True


def pythonic(text):
    """O(n) time and O(n) auxiliary space for normalized and reversed strings."""
    normalized = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return normalized == normalized[::-1]


def optimized(text):
    """O(n) time and O(1) auxiliary space for ASCII input."""
    left, right = 0, len(text) - 1
    while left < right:
        if not text[left].isalnum():
            left += 1
        elif not text[right].isalnum():
            right -= 1
        else:
            if text[left].lower() != text[right].lower():
                return False
            left += 1
            right -= 1
    return True


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("R2, d_ D-2r")
        assert not solve("R2, D-3r")
        assert solve(" _!? ")
        assert solve("!A..")
        assert solve("")
