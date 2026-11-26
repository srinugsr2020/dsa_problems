"""Isomorphic Strings

Problem:
Decide whether one string can become the other by consistently renaming its
characters. Each character must always map to the same character, and two
different characters cannot map to the same one. Strings of different lengths
return False.

Examples:
- "ååb" and "雪雪s" -> True
- "ab" and "abb" -> False
- "ab" and "aa" -> False

Approaches:
- Baseline: Compare pairwise equality.
- Python / standard library: Compare canonical IDs.
- Optimized: Compare last-seen indices.
"""


def baseline(first, second):
    return len(first) == len(second) and all(
        (first[i] == first[j]) == (second[i] == second[j])
        for j in range(len(first)) for i in range(j)
    )


def pythonic(first, second):
    def signature(text):
        ids = {}
        return [ids.setdefault(c, len(ids)) for c in text]

    return signature(first) == signature(second)


def optimized(first, second):
    if len(first) != len(second):
        return False
    seen_first, seen_second = {}, {}
    for i, (a, b) in enumerate(zip(first, second)):
        if seen_first.get(a) != seen_second.get(b):
            return False
        seen_first[a] = seen_second[b] = i
    return True


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("ååb", "雪雪s") and solve("", "")
        assert not solve("", "x") and not solve("ab", "abb")
        assert not solve("abb", "ccc") and not solve("xx", "xy")
