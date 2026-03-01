"""=============================================================================
MEDIUM (Hash Map): Isomorphic Strings
=============================================================================

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced
to get `t`, with these rules:

    - Each character in `s` maps to exactly one character in `t`.
    - No two different characters in `s` may map to the same character in `t`.

Examples:
    s = "egg", t = "add"   -> True
    s = "foo", t = "bar"   -> False
    s = "paper", t = "title" -> True

Constraints (assume):
    - 0 <= len(s), len(t) <= 200_000

Target:
    - Time:  O(n)
    - Space: O(k)

Hints:
    - Maintain two maps to enforce one-to-one mapping:
        s_to_t and t_to_s

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `is_isomorphic(s: str, t: str) -> bool`.
"""

from __future__ import annotations


def is_isomorphic(s: str, t: str) -> bool:
    """Return True if s and t are isomorphic."""

    # TODO: Implement.
    s_to_t = {}
    t_to_s = {}
    for ch_s, ch_t in zip(s, t):
        if ch_s in s_to_t:
            if s_to_t[ch_s] != ch_t:
                return False
        else:
            s_to_t[ch_s] = ch_t
        if ch_t in t_to_s:
            if t_to_s[ch_t] != ch_s:
                return False
        else:
            t_to_s[ch_t] = ch_s
    return True


def _run_samples() -> None:
    assert is_isomorphic("egg", "add") is True
    assert is_isomorphic("foo", "bar") is False
    assert is_isomorphic("paper", "title") is True

    # Edge cases
    assert is_isomorphic("", "") is True
    assert is_isomorphic("ab", "aa") is False


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
