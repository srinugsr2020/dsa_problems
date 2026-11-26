"""Return the first index at which the character occurs only once."""

from collections import Counter


def baseline(text):
    return next((i for i, c in enumerate(text) if text.count(c) == 1), -1)


def pythonic(text):
    counts = Counter(text)
    return next((i for i, c in enumerate(text) if counts[c] == 1), -1)


def optimized(text):
    first = {}
    for i, c in enumerate(text):
        first[c] = -1 if c in first else i
    return next((i for i in first.values() if i >= 0), -1)


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("ééAaa") == 2
        assert solve("baabç") == 4
        assert solve("") == solve("abab") == -1
