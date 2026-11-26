"""Medium (Sliding Window): Minimum Window Substring

Problem:
Given strings `s` and `t`, return the shortest substring of `s` that contains
every character in `t` (including duplicates).  Return "" if no such window exists.

Example:
    s = "ADOBECODEBANC",  t = "ABC"  -> "BANC"
    s = "a",              t = "a"    -> "a"
    s = "a",              t = "aa"   -> ""

Pattern:
- Sliding window (expand right, shrink left)
- Two frequency dicts: `need` (required counts from t) and `have` (current window)
- Track how many distinct chars are fully satisfied (`formed`)

Idea:
    Expand `right` until all chars of `t` are covered (formed == required).
    Then shrink from `left` while the window stays valid, recording the minimum.

Data Engineering angle:
- Finding the smallest time window in a log that contains all required event
  types for SLA compliance — e.g., "what is the shortest session that includes
  login, purchase, and logout events?" — a common analytics query pattern.
"""

from __future__ import annotations

from collections import Counter


def min_window_substring(s: str, t: str) -> str:
    """Return the shortest substring of s containing all chars of t.

    Time:  O(|s| + |t|)  — each character enters and leaves the window once
    Space: O(|s| + |t|)  — for the frequency maps
    """

    if not s or not t:
        return ""

    # Build the frequency map for t (what we *need* in the window).
    need: Counter[str] = Counter(t)

    # Number of distinct characters in t that must be fully satisfied.
    required: int = len(need)

    # Sliding window state.
    have: Counter[str] = Counter()
    formed: int = 0   # Number of distinct chars in t currently fully covered

    left = 0
    best_len = float("inf")
    best_left = 0

    for right, ch in enumerate(s):
        # Expand: bring s[right] into the window.
        have[ch] += 1

        # Check if this character's count in the window now meets the requirement.
        if ch in need and have[ch] == need[ch]:
            formed += 1

        # Try to shrink from the left while the window is still valid.
        while formed == required:
            window_len = right - left + 1
            if window_len < best_len:
                best_len = window_len
                best_left = left

            # Remove s[left] from the window.
            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_left : best_left + best_len]


def _run_tests() -> None:
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window_substring("a", "a") == "a"
    assert min_window_substring("a", "aa") == ""
    assert min_window_substring("", "a") == ""
    assert min_window_substring("abc", "") == ""
    assert min_window_substring("aa", "aa") == "aa"          # Duplicates in t
    assert min_window_substring("cabwefgewcwaefgcf", "cae") == "cwae"


if __name__ == "__main__":
    _run_tests()
    print("OK - medium_minimum_window_substring")
