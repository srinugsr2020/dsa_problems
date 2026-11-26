"""Medium (Pattern Matching): KMP String Search — Knuth-Morris-Pratt

Problem:
Given a text string `text` and a pattern string `pattern`, return the starting
index of the first occurrence of `pattern` in `text`, or -1 if not found.

This file implements the full KMP algorithm — O(n + m) time — which is the
correct answer when an interviewer asks "can you do better than O(n * m)?".

Example:
    text = "aabcaabxaabc",  pattern = "aabc"  -> 0
    text = "hello",         pattern = "ll"    -> 2
    text = "aaaaa",         pattern = "bba"   -> -1

Pattern:
- Build a Longest Proper Prefix which is also Suffix (LPS) table for `pattern`.
- Use the LPS table to skip redundant comparisons during the text scan.

KMP in 2 steps:
    1. _build_lps(pattern)  — preprocess in O(m)
    2. kmp_search(text, pattern) — scan in O(n)

Data Engineering angle:
- Efficient substring search appears in log parsing, schema validation,
  and tokenization of structured text (e.g., detecting a delimiter pattern
  inside CSV/TSV fields without re-scanning already-matched characters).
"""

from __future__ import annotations

from typing import List


def _build_lps(pattern: str) -> List[int]:
    """Build the Longest Proper Prefix-Suffix (LPS) array for pattern.

    lps[i] = length of the longest proper prefix of pattern[:i+1] that is
             also a suffix of pattern[:i+1].

    Time:  O(m)  where m = len(pattern)
    Space: O(m)
    """

    m = len(pattern)
    lps: List[int] = [0] * m

    # `length` tracks the length of the previous longest prefix-suffix.
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            # Extend the current matching prefix-suffix.
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            # Fall back using the previously computed prefix-suffix.
            # Do NOT increment i — re-examine the same position.
            length = lps[length - 1]
        else:
            # No matching prefix-suffix at all.
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text: str, pattern: str) -> int:
    """Return the index of the first occurrence of pattern in text, else -1.

    Time:  O(n + m)  — preprocessing O(m) + scan O(n)
    Space: O(m)      — for the LPS array
    """

    if not pattern:
        return 0
    if not text or len(pattern) > len(text):
        return -1

    n, m = len(text), len(pattern)
    lps = _build_lps(pattern)

    i = 0   # Index into text
    j = 0   # Index into pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            # Full match found at position i - j.
            return i - j

        if i < n and text[i] != pattern[j]:
            if j != 0:
                # Skip characters using the LPS table.
                j = lps[j - 1]
            else:
                i += 1

    return -1


def kmp_find_all(text: str, pattern: str) -> List[int]:
    """Return indices of ALL occurrences of pattern in text.

    Continues searching after each match using the LPS table.

    Time:  O(n + m)
    Space: O(m)
    """

    if not pattern:
        return list(range(len(text) + 1))

    n, m = len(text), len(pattern)
    lps = _build_lps(pattern)
    results: List[int] = []

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            results.append(i - j)
            # Continue from where the LPS table tells us.
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return results


def _run_tests() -> None:
    # _build_lps sanity checks
    assert _build_lps("aabcaab") == [0, 1, 0, 0, 1, 2, 3]
    assert _build_lps("aaaa") == [0, 1, 2, 3]
    assert _build_lps("abcabc") == [0, 0, 0, 1, 2, 3]

    # kmp_search — first occurrence
    assert kmp_search("aabcaabxaabc", "aabc") == 0
    assert kmp_search("hello", "ll") == 2
    assert kmp_search("aaaaa", "bba") == -1
    assert kmp_search("", "a") == -1
    assert kmp_search("abc", "") == 0
    assert kmp_search("aabcaabxaabc", "aabx") == 4

    # kmp_find_all — all occurrences
    assert kmp_find_all("ababab", "ab") == [0, 2, 4]
    assert kmp_find_all("aaaaaa", "aa") == [0, 1, 2, 3, 4]
    assert kmp_find_all("abc", "d") == []


if __name__ == "__main__":
    _run_tests()
    print("OK - medium_kmp_search")
