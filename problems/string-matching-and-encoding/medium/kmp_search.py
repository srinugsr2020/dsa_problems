"""Substring Search

Problem:
Given a text string and a pattern, find the zero-based start of the first exact
match, or -1 if there is none. Also support finding every match, including
overlapping ones. An empty pattern matches at every boundary, including the end.

Examples:
- Text "aaaab", pattern "aab" -> first index 2
- Text "aaaa", pattern "aa" -> starts [0, 1, 2]
- Text "ab", empty pattern -> starts [0, 1, 2]

Approaches:
- Baseline: Check every alignment.
- Python / standard library: Use str.find and advance one.
- Optimized: Knuth-Morris-Pratt.
"""


def baseline(text, pattern):
    """Yield match positions from left to right."""
    for start in range(len(text) - len(pattern) + 1):
        if all(text[start + j] == c for j, c in enumerate(pattern)):
            yield start


def pythonic(text, pattern):
    start = 0
    while start <= len(text):
        match = text.find(pattern, start)
        if match == -1:
            break
        yield match
        start = match + 1


def optimized(text, pattern):
    if not pattern:
        yield from range(len(text) + 1)
        return
    border = [0] * len(pattern)
    matched = 0
    for i in range(1, len(pattern)):
        while matched and pattern[i] != pattern[matched]:
            matched = border[matched - 1]
        if pattern[i] == pattern[matched]:
            matched += 1
        border[i] = matched

    matched = 0
    for i, c in enumerate(text):
        while matched and c != pattern[matched]:
            matched = border[matched - 1]
        if c == pattern[matched]:
            matched += 1
            if matched == len(pattern):
                matched = border[matched - 1]
                yield i - len(pattern) + 1


def first(text, pattern, search=optimized):
    return next(search(text, pattern), -1)


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert first("aaaab", "aab", solve) == 2
        assert first("🙂é🙂é", "é🙂", solve) == 1
        assert first("aaa", "aaaa", solve) == -1
        assert list(solve("aaaa", "aa")) == [0, 1, 2]
        assert list(solve("ab", "")) == [0, 1, 2]
        assert list(solve("", "")) == [0] and list(solve("", "a")) == []
