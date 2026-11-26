"""Jewels And Stones

Problem:
Count stone occurrences whose case-sensitive character appears in the jewel
string.

Examples:
- "aAz" and "aAAZZzz" -> 5
- "éé🙂" and "é🙂eé" -> 3

Approaches:
- Baseline: Search the jewel string.
- Python / standard library: Set plus generator.
- Optimized: Use a bounded membership mask.
"""

from string import ascii_letters


def baseline(jewels, stones):
    return sum(stone in jewels for stone in stones)


def pythonic(jewels, stones):
    prized = set(jewels)
    return sum(stone in prized for stone in stones)


def optimized(jewels, stones):
    if any(c not in ascii_letters for c in jewels):
        return pythonic(jewels, stones)
    mask = 0
    for jewel in jewels:
        mask |= 1 << (ord(jewel) - ord("A"))
    total = 0
    for stone in stones:
        slot = ord(stone) - ord("A")
        if 0 <= slot <= ord("z") - ord("A"):
            total += (mask >> slot) & 1
    return total


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("aAz", "aAAZZzz]9") == 5
        assert solve("éé🙂", "é🙂eé") == 3
        assert solve("", "aaa") == solve("a", "") == 0
