"""Concatenated Words

Problem:
Given a string and a list of words of the same nonzero length, find substrings
made by joining all the words in any order, with no gaps. If a word appears
twice in the list, use it twice. Return the zero-based start indices in any
order. Matches can overlap; an empty word list has no matches.

Examples:
- "aaaaa", ['aa', 'aa'] -> [0, 1] in either order.
- "xabcdab--cdab", ['ab', 'cd'] -> [1, 3, 9] in any order.
- "ababcd", ['ab', 'cd', 'cd'] -> [].

Approaches:
- Baseline: Rebuild counts for each start.
- Python / standard library: Compare sliding Counter objects.
- Optimized: Maintain a capped word window.
"""

from collections import Counter


def _width(words):
    if not words:
        return 0
    width = len(words[0])
    if width == 0 or any(len(word) != width for word in words):
        raise ValueError("all words must have the same positive width")
    return width


def baseline(text, words):
    """Expected O(B*w + n*B*w) time, O(d*w) auxiliary space excluding output."""
    w = _width(words)
    if not w:
        return []
    need = Counter(words)
    span = w * len(words)
    out = []
    for start in range(len(text) - span + 1):
        have = Counter()
        for i in range(start, start + span, w):
            word = text[i:i + w]
            have[word] += 1
            if have[word] > need[word]:
                break
        else:
            out.append(start)
    return out


def pythonic(text, words):
    """Expected O(B*w + n*(w+d)) time, O(B*w) auxiliary space excluding output."""
    w = _width(words)
    span = w * len(words)
    if not w or span > len(text):
        return []
    need = Counter(words)
    out = []
    for offset in range(w):
        have = Counter()
        for i in range(offset, len(text) - w + 1, w):
            have[text[i:i + w]] += 1
            if i - offset >= span:
                old = text[i - span:i - span + w]
                have[old] -= 1
                if have[old] == 0:
                    del have[old]
            start = i + w - span
            if start >= offset and have == need:
                out.append(start)
    return out


def optimized(text, words):
    """Expected O((n+B)*w) time, O(d*w) auxiliary space excluding output."""
    w = _width(words)
    if not w or w * len(words) > len(text):
        return []
    need = Counter(words)
    out = []
    for offset in range(w):
        have = Counter()
        left, size = offset, 0
        for i in range(offset, len(text) - w + 1, w):
            word = text[i:i + w]
            if word not in need:
                have.clear()
                left, size = i + w, 0
                continue
            have[word] += 1
            size += 1
            while have[word] > need[word]:
                have[text[left:left + w]] -= 1
                left += w
                size -= 1
            if size == len(words):
                out.append(left)
    return out


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert sorted(solve("aaaaa", ["aa", "aa"])) == [0, 1]
        assert sorted(solve("xabcdab--cdab", ["ab", "cd"])) == [1, 3, 9]
        assert solve("ababcd", ["ab", "cd", "cd"]) == []
        assert solve("", ["ab"]) == solve("ab", []) == []
        try:
            solve("xabc", ["ab", "c"])
        except ValueError:
            pass
        else:
            raise AssertionError("uneven word widths should be rejected")
