"""=============================================================================
MEDIUM (Sliding Window): Longest Substring with At Most K Distinct Characters
=============================================================================

Given a string `s` and an integer `k`, return the length of the longest
substring that contains at most `k` distinct characters.

Examples:
    s = "eceba", k = 2 -> 3  ("ece")
    s = "aa", k = 1    -> 2  ("aa")

Constraints (assume):
    - 0 <= len(s) <= 200_000
    - 0 <= k <= 200_000

Target:
    - Time:  O(n)
    - Space: O(k)

Hints:
    - Sliding window with counts of characters.
    - Expand right; while distinct_count > k, shrink left.

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `longest_substring_at_most_k_distinct(s: str, k: int) -> int`.
"""

from __future__ import annotations


def _dec_count(counts: dict[str, int], ch: str) -> None:
    """Decrement counts[ch] and delete the key when its count reaches 0."""

    counts[ch] -= 1
    if counts[ch] == 0:
        del counts[ch]


def longest_substring_at_most_k_distinct(s: str, k: int) -> int:
    """Return the max length of a substring with <= k distinct chars."""

    # If k == 0, no characters are allowed in the window.
    if k <= 0 or not s:
        return 0

    # Sliding window [left..right]
    # `counts` stores character frequencies inside the current window.
    counts: dict[str, int] = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        # Expand the window to include s[right].
        counts[ch] = counts.get(ch, 0) + 1

        # If we have too many distinct characters, shrink from the left
        # until the window becomes valid again.
        while len(counts) > k:
            left_ch = s[left]
            _dec_count(counts, left_ch)
            left += 1

        # Window is valid here: update the best length.
        best = max(best, right - left + 1)

    return best


def _run_samples() -> None:
    assert longest_substring_at_most_k_distinct("eceba", 2) == 3
    assert longest_substring_at_most_k_distinct("aa", 1) == 2

    # Edge cases
    assert longest_substring_at_most_k_distinct("", 2) == 0
    assert longest_substring_at_most_k_distinct("abc", 0) == 0
    assert longest_substring_at_most_k_distinct("abc", 10) == 3


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
