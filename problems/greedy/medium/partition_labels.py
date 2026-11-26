"""Partition Labels

Problem:
Split a string into as many contiguous parts as possible without using any
character in two different parts. Return the lengths.

Examples:
- "abacdd" returns [3, 1, 2]: split it into "aba", "c", and "dd".
- "abcbca" returns [6]: the first and last "a" must stay in the same part.

Approaches:
- Baseline: Test every cut using membership scans.
- Python / standard library: Use set.isdisjoint.
- Optimized: Jump to last occurrences.
"""

from __future__ import annotations


def baseline(text: str) -> list[int]:
    lengths = []
    start = 0
    for end in range(1, len(text) + 1):
        suffix = text[end:]
        if not any(char in suffix for char in text[start:end]):
            lengths.append(end - start)
            start = end
    return lengths


def python_sets(text: str) -> list[int]:
    lengths = []
    start = 0
    for end in range(1, len(text) + 1):
        if set(text[start:end]).isdisjoint(text[end:]):
            lengths.append(end - start)
            start = end
    return lengths


def optimized(text: str) -> list[int]:
    last_seen = {char: index for index, char in enumerate(text)}
    lengths = []
    start = end = 0
    for index, char in enumerate(text):
        end = max(end, last_seen[char])
        if index == end:
            lengths.append(end - start + 1)
            start = index + 1
    return lengths


if __name__ == "__main__":
    for partition in baseline, python_sets, optimized:
        assert partition("abacdd") == [3, 1, 2]
        assert partition("abcbca") == [6]
        assert partition("xyz") == [1, 1, 1]
        assert partition("") == []
