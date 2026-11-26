"""Longest Duplicate Substring

Problem:
Find any longest substring appearing at two distinct starting positions.
Overlaps count.

Examples:
- "tanana" -> "ana" at positions 1 and 3
- "aaaa" -> "aaa"
- "abcd" -> ""

Approaches:
- Baseline: Compare every pair of suffix starts.
- Python / standard library: Sort suffix strings.
- Optimized: Rank doubling and adjacent LCP.
"""

from itertools import islice


def baseline(text):
    best_start = best_length = 0
    for left in range(len(text)):
        for right in range(left + 1, len(text)):
            length = 0
            while right + length < len(text) and text[left + length] == text[right + length]:
                length += 1
            if length > best_length:
                best_start, best_length = left, length
    return text[best_start:best_start + best_length]


def pythonic(text):
    suffixes = sorted(text[i:] for i in range(len(text)))
    best_suffix, best_length = "", 0
    for left, right in zip(suffixes, islice(suffixes, 1, None)):
        length = 0
        for a, b in zip(left, right):
            if a != b:
                break
            length += 1
        if length > best_length:
            best_suffix, best_length = left, length
    return best_suffix[:best_length]


def optimized(text):
    n = len(text)
    if n < 2:
        return ""
    suffixes = list(range(n))
    ranks = [ord(c) for c in text]
    width = 1
    while width < n:
        def rank_pair(i):
            return ranks[i], ranks[i + width] if i + width < n else -1

        suffixes.sort(key=rank_pair)
        new_ranks = [0] * n
        for pos in range(1, n):
            left, right = suffixes[pos - 1], suffixes[pos]
            new_ranks[right] = new_ranks[left] + (rank_pair(left) != rank_pair(right))
        ranks = new_ranks
        if ranks[suffixes[-1]] == n - 1:
            break
        width *= 2

    best_length = best_start = common = 0
    for i in range(n):
        r = ranks[i]
        if r == 0:
            common = 0
            continue
        j = suffixes[r - 1]
        while i + common < n and j + common < n and text[i + common] == text[j + common]:
            common += 1
        if common > best_length:
            best_length, best_start = common, i
        # Dropping the leading character leaves at least common - 1 matched.
        common = max(0, common - 1)
    return text[best_start:best_start + best_length]


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("tanana") == "ana" and solve("aaaa") == "aaa"
        assert solve("é🙂é🙂é") == "é🙂é"
        assert solve("ababcxcdcd") in {"ab", "cd"}
        assert solve("abcd") == solve("x") == solve("") == ""
