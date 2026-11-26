"""Repeated Substring

Problem:
Decide whether a string consists of at least two copies of a shorter, nonempty
string.

Examples:
- "é🙂é🙂é🙂" -> True
- "ababa" -> False
- "" and "a" -> False

Approaches:
- Baseline: Try divisor periods.
- Python / standard library: Search in the doubled string.
- Optimized: Use the longest proper border.
"""


def baseline(text):
    n = len(text)
    for width in range(1, n // 2 + 1):
        if n % width == 0 and all(text[i] == text[i % width] for i in range(width, n)):
            return True
    return False


def pythonic(text):
    if not text:
        return False
    n = len(text)
    return (text + text).find(text, 1, 2 * n - 1) != -1


def optimized(text):
    n = len(text)
    if n < 2:
        return False
    borders = [0] * n
    matched = 0
    for i in range(1, n):
        while matched and text[i] != text[matched]:
            matched = borders[matched - 1]
        if text[i] == text[matched]:
            matched += 1
        borders[i] = matched
    return matched > 0 and n % (n - matched) == 0


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("é🙂é🙂é🙂") and solve("aaaa")
        assert not solve("ababa") and not solve("abcabcab")
        assert not solve("a") and not solve("")
