"""Medium (Hash Map): Word Pattern

Problem:
Given a pattern string `pattern` and a string `s` of space-separated words,
return True if `s` follows the same pattern — i.e., there is a bijection
(one-to-one, onto mapping) between each letter in `pattern` and each word in `s`.

Example:
    pattern = "abba",  s = "dog cat cat dog"   -> True
    pattern = "abba",  s = "dog cat cat fish"  -> False
    pattern = "aaaa",  s = "dog cat cat dog"   -> False
    pattern = "abba",  s = "dog dog dog dog"   -> False

Pattern:
- Bijection check using two dicts (char -> word and word -> char)
- Same fundamental technique as isomorphic strings, applied to whole words

Data Engineering angle:
- Checking structural schema compliance: e.g., verifying that column aliases
  in a query follow a consistent naming convention, or that two streams
  have matching partition key patterns.
"""

from __future__ import annotations

from typing import List


def word_pattern(pattern: str, s: str) -> bool:
    """Return True if s follows the exact same pattern as pattern.

    Time:  O(n)  where n = len(pattern) (= number of words in s)
    Space: O(k)  where k = number of distinct chars in pattern
    """

    words: List[str] = s.split()

    # Pattern and word list must be the same length for a bijection to exist.
    if len(pattern) != len(words):
        return False

    # Two maps to enforce the strict one-to-one correspondence.
    char_to_word: dict[str, str] = {}
    word_to_char: dict[str, str] = {}

    for ch, word in zip(pattern, words):
        # Check char -> word direction.
        if ch in char_to_word:
            if char_to_word[ch] != word:
                return False
        else:
            char_to_word[ch] = word

        # Check word -> char direction (ensures no two chars map to same word).
        if word in word_to_char:
            if word_to_char[word] != ch:
                return False
        else:
            word_to_char[word] = ch

    return True


def _run_tests() -> None:
    assert word_pattern("abba", "dog cat cat dog") is True
    assert word_pattern("abba", "dog cat cat fish") is False   # 'b' maps to two words
    assert word_pattern("aaaa", "dog cat cat dog") is False    # Two chars map to same word
    assert word_pattern("abba", "dog dog dog dog") is False    # Both 'a' and 'b' -> "dog"
    assert word_pattern("a", "dog") is True
    assert word_pattern("ab", "dog dog") is False              # 'a' and 'b' both -> "dog"
    assert word_pattern("ab", "dog cat") is True
    assert word_pattern("aab", "dog dog cat") is True
    # Length mismatch
    assert word_pattern("abc", "dog cat") is False


if __name__ == "__main__":
    _run_tests()
    print("OK - medium_word_pattern")
