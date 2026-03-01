"""Easy (Hash Map): First Non-Repeating Character

Problem:
Given a string `s`, return the index of the first character that does not
repeat anywhere in the string.  Return -1 if every character repeats.

Example:
    s = "leetcode"   -> 0   ('l' appears only once)
    s = "loveleetcode" -> 2  ('v' is the first unique char)
    s = "aabb"       -> -1

Pattern:
- Two-pass hash map: count frequencies, then find first char with count == 1.
- OR single-pass with an ordered dict to maintain insertion order.

Data Engineering angle:
- Finding the first non-duplicate key in an event stream or log file —
  a lightweight early-exit quality check before heavier dedup joins.
"""

from __future__ import annotations

from collections import OrderedDict


def first_non_repeating_char(s: str) -> int:
    """Return the index of the first non-repeating character, or -1.

    Two-pass approach: O(n) time, O(k) space (k = alphabet size).
    """

    # First pass: count every character's frequency.
    freq: dict[str, int] = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Second pass: return the index of the first character with count 1.
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1


def first_non_repeating_index_ordered(s: str) -> int:
    """Single-pass variant using an OrderedDict.

    Stores (first_index, count) for each character in insertion order.
    After one scan, find the first entry whose count is 1.

    Useful when you process characters one at a time (streaming context).

    Time:  O(n)  — one pass + one ordered dict scan (bounded by alphabet size)
    Space: O(k)
    """

    # Map each char to a tuple: (first_seen_index, occurrence_count).
    seen: OrderedDict[str, list[int]] = OrderedDict()

    for i, ch in enumerate(s):
        if ch not in seen:
            # [index_of_first_occurrence, count]
            seen[ch] = [i, 0]
        seen[ch][1] += 1

    # Iterate in insertion order (Python 3.7+ dicts preserve order too, but
    # OrderedDict makes the intent explicit for interview settings).
    for ch, (idx, count) in seen.items():
        if count == 1:
            return idx

    return -1


def _run_tests() -> None:
    # Two-pass version
    assert first_non_repeating_char("leetcode") == 0
    assert first_non_repeating_char("loveleetcode") == 2
    assert first_non_repeating_char("aabb") == -1
    assert first_non_repeating_char("") == -1
    assert first_non_repeating_char("z") == 0

    # Single-pass ordered variant
    assert first_non_repeating_index_ordered("leetcode") == 0
    assert first_non_repeating_index_ordered("loveleetcode") == 2
    assert first_non_repeating_index_ordered("aabb") == -1
    assert first_non_repeating_index_ordered("") == -1
    assert first_non_repeating_index_ordered("aab") == 2  # 'b' at index 2


if __name__ == "__main__":
    _run_tests()
    print("OK - easy_first_non_repeating_char")
