"""=============================================================================
EASY (Greedy/Hashing): Longest Palindrome You Can Build
=============================================================================

Given a string `s`, return the length of the longest palindrome that can be
built with the letters of `s`.

You can reorder letters arbitrarily.

Examples:
    s = "abccccdd" -> 7  ("dccaccd")
    s = "a"        -> 1

Constraints (assume):
    - 0 <= len(s) <= 200_000

Target:
    - Time:  O(n)
    - Space: O(k)

Hint:
    - Pairs of characters contribute fully.
    - At most one character with odd count can sit in the center.

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `longest_palindrome_length(s: str) -> int`.
"""

from __future__ import annotations


def longest_palindrome_length(s: str) -> int:
    """Return the length of the longest palindrome buildable from s."""

    # TODO: Implement.
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    length = 0
    odd_found = False
    for count in counts.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True

    if odd_found:
        length += 1

    return length


def _run_samples() -> None:
    assert longest_palindrome_length("abccccdd") == 7
    assert longest_palindrome_length("a") == 1
    assert longest_palindrome_length("") == 0

    # Case-sensitive
    assert longest_palindrome_length("Aa") == 1


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
