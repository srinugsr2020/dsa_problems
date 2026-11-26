"""Longest Palindromic Substring

Problem:
Find the longest substring that reads the same forward and backward. The
characters must be consecutive. Return the leftmost match if several have the
same maximum length, or an empty string if the input is empty.

Examples:
- "cabbad" returns "abba", which reads the same forward and backward.
- "abacdc" returns "aba": "cdc" has the same length but starts later.

Approaches:
- Baseline: Check substring intervals.
- Python / standard library: Compare slices against their reverse.
- Optimized: Expand around odd and even centers.
"""


def is_palindrome(text: str, left: int, right: int) -> bool:
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def baseline(text: str) -> str:
    best_start = best_length = 0
    for start in range(len(text)):
        for stop in range(start + 1, len(text) + 1):
            if stop - start > best_length and is_palindrome(text, start, stop - 1):
                best_start, best_length = start, stop - start
    return text[best_start:best_start + best_length]


def python_reverse(text: str) -> str:
    for length in range(len(text), 0, -1):
        for start in range(len(text) - length + 1):
            candidate = text[start:start + length]
            if candidate == candidate[::-1]:
                return candidate
    return ""


def optimized(text: str) -> str:
    best_start = best_length = 0
    for center in range(len(text)):
        for left, right in ((center, center), (center, center + 1)):
            while left >= 0 and right < len(text) and text[left] == text[right]:
                if right - left + 1 > best_length:
                    best_start, best_length = left, right - left + 1
                left -= 1
                right += 1
    return text[best_start:best_start + best_length]


if __name__ == "__main__":
    for longest in baseline, python_reverse, optimized:
        assert longest("xyz") == "x"
        assert longest("cabbad") == "abba"
        assert longest("abacdc") == "aba"
        assert longest("aaaa") == "aaaa"
        assert longest("") == ""
