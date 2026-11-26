"""=============================================================================
EASY (Hash Map): Valid Anagram
=============================================================================

Given two strings `s` and `t`, return True if `t` is an anagram of `s`.

An anagram uses the same characters with the same counts.

Examples:
    s = "anagram", t = "nagaram" -> True
    s = "rat", t = "car"         -> False

Constraints (assume):
    - 0 <= len(s), len(t) <= 200_000
    - strings may contain any characters

Target:
    - Time:  O(n)
    - Space: O(k)

Hints:
    - Use a dictionary count, or collections.Counter.

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `is_anagram(s: str, t: str) -> bool`.
"""

from __future__ import annotations

# from sklearn.base import defaultdict
from collections import defaultdict

def is_anagram(s: str, t: str) -> bool:
    """Return True if t is an anagram of s."""

    # TODO: Implement.
    default_dict = defaultdict(int)
    for ch in s:
        default_dict[ch] += 1
    for ch in t:
        default_dict[ch] -= 1
    return all(count == 0 for count in default_dict.values())


def _run_samples() -> None:
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False

    assert is_anagram("", "") is True
    assert is_anagram("a", "A") is False  # case-sensitive by default


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
