"""=============================================================================
MEDIUM (Sliding Window): Longest Repeating Character Replacement
=============================================================================

You are given a string `s` and an integer `k`.

You can choose any character in the string and change it to any other character
at most `k` times.

Return the length of the longest substring you can obtain that contains the
same character after at most `k` replacements.

Examples:
    s = "ABAB", k = 2 -> 4  (make all 'A' or all 'B')
    s = "AABABBA", k = 1 -> 4

Constraints (assume):
    - 0 <= len(s) <= 200_000

Target:
    - Time:  O(n)
    - Space: O(k)

Hints:
    - Sliding window.
    - Track counts of chars in the window.
    - Keep `max_freq` = maximum frequency of any single char in the window.
    - Window is valid if: (window_len - max_freq) <= k

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `character_replacement(s: str, k: int) -> int`.
"""

from __future__ import annotations


def character_replacement(s: str, k: int) -> int:
    """Return longest length after at most k replacements to make all chars same."""

    counts: dict[str, int] = {}
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        max_freq = max(max_freq, counts[ch])

        # If we need to replace more than k chars, shrink the window.
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)
    return best


def _run_samples() -> None:
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4

    # Edge cases
    assert character_replacement("", 5) == 0
    assert character_replacement("AAAA", 0) == 4
    assert character_replacement("ABCDE", 1) == 2


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
