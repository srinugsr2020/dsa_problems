"""=============================================================================
EASY (Sliding Window): Maximum Vowels in a Substring of Length k
=============================================================================

Given a string `s` and an integer `k`, return the maximum number of vowels in
any substring of `s` with length exactly `k`.

Vowels are: a, e, i, o, u (both lowercase and uppercase).

Examples:
    s = "abciiidef", k = 3 -> 3  ("iii")
    s = "aeiou", k = 2     -> 2
    s = "leetcode", k = 3  -> 2  ("lee")

Constraints (assume):
    - 0 <= len(s) <= 200_000
    - 0 <= k <= len(s)

Target:
    - Time:  O(n)
    - Space: O(1)

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `max_vowels(s: str, k: int) -> int`.
"""

from __future__ import annotations


def _is_vowel(ch: str) -> bool:
    """Return True if ch is a vowel (case-insensitive)."""

    return ch.lower() in {"a", "e", "i", "o", "u"}


def max_vowels(s: str, k: int) -> int:
    """Return the maximum number of vowels in any length-k substring."""

    # TODO: Implement using a fixed-size sliding window.
    # Suggested steps:
    #   - Count vowels in the first window s[:k]
    #   - Slide: remove s[i-k], add s[i]
    #   - Track the max
    count = sum(1 for ch in s[:k] if _is_vowel(ch))
    max_count = count
    for i in range(k, len(s)):
        count += _is_vowel(s[i]) - _is_vowel(s[i - k])
        max_count = max(max_count, count)
    return max_count


def _run_samples() -> None:
    assert max_vowels("abciiidef", 3) == 3
    assert max_vowels("aeiou", 2) == 2
    assert max_vowels("leetcode", 3) == 2

    # Edge cases
    assert max_vowels("", 0) == 0
    assert max_vowels("bcd", 1) == 0
    assert max_vowels("AeiOu", 5) == 5


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
