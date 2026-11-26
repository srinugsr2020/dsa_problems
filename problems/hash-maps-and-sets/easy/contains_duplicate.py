"""Contains Duplicate

Problem:
Return whether two different positions in an integer list hold the same value.

Examples:
- [7, -1, 0, -1] -> True
- [] -> False

Approaches:
- Baseline: Compare each pair.
- Python / standard library: Compare set and list sizes.
- Optimized: Stop on a repeat.
"""


def baseline(values):
    return any(values[i] == values[j]
               for j in range(len(values)) for i in range(j))


def pythonic(values):
    return len(set(values)) < len(values)


def optimized(values):
    seen = set()
    for value in values:
        if value in seen:
            return True
        seen.add(value)
    return False


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert not solve([]) and not solve([0])
        assert solve([7, -1, 0, -1]) and not solve([7, -1, 0])
