"""Longest Consecutive Sequence

Problem:
Find the longest run of consecutive integer values in unsorted input. Duplicates
do not extend a run.

Examples:
- [-1, 2, -3, 0, -1, -2] -> 4 for the run from -3 to 0
- [] -> 0

Approaches:
- Baseline: Scan the list for neighbors.
- Python / standard library: Sort distinct values.
- Optimized: Walk from set run starts.
"""


def baseline(values):
    best = 0
    for start in values:
        if start - 1 not in values:
            end = start + 1
            while end in values:
                end += 1
            best = max(best, end - start)
    return best


def pythonic(values):
    best = run = 0
    previous = None
    for value in sorted(set(values)):
        run = run + 1 if previous == value - 1 else 1
        best = max(best, run)
        previous = value
    return best


def optimized(values):
    pending = set(values)
    best = 0
    for start in pending:
        if start - 1 in pending:
            continue
        end = start + 1
        while end in pending:
            end += 1
        best = max(best, end - start)
    return best


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve([-1, 2, -3, 0, -1, -2]) == 4
        assert solve([3, 3, 3]) == 1 and solve([]) == 0
