"""=============================================================================
MEDIUM (Prefix/Suffix Trick): Repeated Substring Pattern
=============================================================================

Given a string `s`, return True if it can be constructed by taking a substring
of it and appending multiple copies of the substring together.

Examples:
    s = "abab"      -> True   ("ab" + "ab")
    s = "aba"       -> False
    s = "abcabcabc" -> True   ("abc" repeated)

Constraints (assume):
    - 0 <= len(s) <= 200_000

Target:
    - Time:  O(n)
    - Space: O(n)

Hints:
    - Classic trick: if s is a repeated pattern, then s is a substring of
      (s + s)[1:-1].
    - Careful with small strings.

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `repeated_substring_pattern(s: str) -> bool`.
"""

from __future__ import annotations


def repeated_substring_pattern(s: str) -> bool:
    """Return True if s is made by repeating some non-empty substring."""

    if not s:
        return False
    ss = s + s
    return s in ss[1:-1]


def _run_samples() -> None:
    assert repeated_substring_pattern("abab") is True
    assert repeated_substring_pattern("aba") is False
    assert repeated_substring_pattern("abcabcabc") is True

    # Edge cases
    assert repeated_substring_pattern("") is False
    assert repeated_substring_pattern("a") is False
    assert repeated_substring_pattern("aaaa") is True


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
